import json
import csv
import os
from Primavera_REST_Api.__eppmSession import EppmSession
from Primavera_REST_Api.__endpointsEnum import EndpointEnum


class Method:
    def __init__(self, eppmSession: EppmSession, endpoint: EndpointEnum):
        self.context = eppmSession
        self.endpoint = endpoint
        self.endpointValue = endpoint.value

        # These endpoints don't require ProjectObjectId field
        # if endpoint in ['project', 'resource', 'role', 'resourceRole']:
        if endpoint in [EndpointEnum.project,
                        EndpointEnum.resource,
                        EndpointEnum.role,
                        EndpointEnum.resourceRole]:
            self.__ignoreProjectId = True
        else:
            self.__ignoreProjectId = False

    def read(self, fields: list[str] | None = None, filters: str | None = None) -> list[dict]:
        """
        Read object from database
        """
        url = f"{self.context.prefix}/{self.endpointValue}"

        if fields == None:
            fields = self.fields()
        params = {"Fields": ','.join(fields)}

        # To be refactored to use filters parameter!!!
        if self.context.selectedProjectObjectId is not None and not self.__ignoreProjectId:
            params.update({"Filter": f"ProjectObjectId :eq: {self.context.selectedProjectObjectId}"})

        result = self.context.session.get(url=url, params=params)
        return json.loads(result.text)

    def update(self, objectList: list[dict], chunkSize: int = 100):
        """
        Update object in database. JSON always should have key ObjectId.
        ObjectList will be divided to chunks default size of 100 elements
        """

        url = f"{self.context.prefix}/{self.endpointValue}"
        currentSize = 0

        for objectListChunk in list(self.__chunk(list=objectList, chunkSize=chunkSize)):
            result = self.context.session.put(url=url, json=objectListChunk)
            if result.status_code != 200:
                raise Exception(f"""
                                Error on UpdateObject: {result.text}
                                Object: {objectListChunk} 
                                """)

            currentSize += len(objectListChunk)
            print(f"{self.endpointValue} update progress ({currentSize} of {len(objectList)}) = {round(currentSize/len(objectList)*100,2)}%")

    def delete(self, objectIdsList: list[str]):
        if len(objectIdsList) == 0:
            raise Exception("ObjectIds List cannot be empty")

        url = f"{self.context.prefix}/{self.endpointValue}"
        params = {"ObjectId": ','.join(objectIdsList)}
        result = self.context.session.delete(url=url, params=params)
        if result.status_code != 200:
            raise Exception(f"""
                                Error on DeleteObject: {result.text}
                                Object: {objectIdsList} 
                                """)
        print("Deleted: ", objectIdsList)

    def create(self, objectList: list[dict], chunkSize: int = 100):
        url = f"{self.context.prefix}/{self.endpointValue}"
        currentSize = 0

        if not self.__ignoreProjectId:
            for obj in objectList:
                obj['ProjectObjectId'] = self.context.selectedProjectObjectId

        for objectListChunk in list(self.__chunk(list=objectList, chunkSize=chunkSize)):
            result = self.context.session.post(url=url, json=objectListChunk)
            if result.status_code != 201:
                raise Exception(f"""
                                Error on CreateObject: {result.text}
                                Object: {objectListChunk} 
                                """)

            currentSize += len(objectListChunk)
            print(f"{self.endpointValue} create progress ({currentSize} of {len(objectList)}) = {round(currentSize/len(objectList)*100,2)}%")

    def getFieldLength(self, fieldName: str) -> int:
        """
        Send a request to this endpoint to load length of variable character fields for a BO.

        Parameters:
            fieldName: Field name

        Returns:
            json: Field name length 
        """
        url = f"{self.context.prefix}/{self.endpointValue}/getFieldLength/{fieldName}"
        result = self.context.session.get(url=url)
        if result.status_code != 200:
            raise Exception(f'ERROR: getFieldLength: {result.text}')
        return int(result.text)

    def fields(self) -> list[str]:
        """
        Get all available object fields from database

        Returns:
            json: List of all available fields 
        """
        url = f"{self.context.prefix}/{self.endpointValue}/fields"
        result = self.context.session.get(url=url)
        return result.text.split(sep=",")

    def __chunk(self, list: list, chunkSize: int):
        for i in range(0, len(list), chunkSize):
            yield list[i:i+chunkSize]

    def export_to_CSV(self, directory: str = "csv", filename: str | None = None, fields: list[str] | None = None, delimiter: str = ','):
        if fields == None:
            fields = self.fields()
        if filename == None:
            filename = f"export - {self.endpointValue}.csv"

        objectList = self.read(fields=fields)
        self.__write_to_CSV_file(directory=directory, filename=filename, objectList=objectList, delimiter=delimiter)

    def __write_to_CSV_file(self, directory: str, filename: str, objectList: list[dict], delimiter: str = ','):
        if len(objectList) == 0:
            print(f"Not exported, empty file: {filename}")
            return

        try:
            current_directory = os.getcwd()
            full_path = os.path.join(current_directory, directory)

            file = os.path.join(full_path, filename)
            if not os.path.isdir(full_path):
                os.mkdir(full_path)

            with open(file=file, mode='w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=delimiter)
                writer.writerow(list(objectList[0]))
                for row in objectList:
                    writer.writerow(list(row.values()))
            print(f"EXPORT -> file exported: {filename}")
        except:
            print(f"Error during export to CSV: {filename}")

    def parse_CSV(self, filename: str, delimiter: str = ',', newline: str = '', directory: str = 'csv') -> list[dict]:
        current_directory = os.getcwd()
        full_path = os.path.join(current_directory, directory)

        file = os.path.join(full_path, filename)

        with open(file=file, mode='r', newline=newline) as csvfile:
            importedDictList: list[dict] = list(csv.DictReader(csvfile, delimiter=delimiter))

        if len(importedDictList) == 0:
            raise Exception("parse CSV failed, empty file")

        endpointFields = self.fields()
        if not all(elem in endpointFields for elem in list(importedDictList[0].keys())):
            unsupportedNames = set(importedDictList[0].keys()) - set(endpointFields)
            raise Exception(f'ERROR: import file has unsupported Column Names: {unsupportedNames}')
        return importedDictList

    def import_CSV_to_EPPM(self,
                           directory: str = "csv",
                           filename: str = 'import - activity.csv',
                           delimiter: str = ',',
                           newline: str = ''):

        parsed = self.parse_CSV(directory=directory, filename=filename, delimiter=delimiter, newline=newline)
        objIdList = [o['ObjectId'] for o in self.read(fields=['ObjectId'])]

        updateList = []
        createList = []

        for p in parsed:
            if p.get('ObjectId', False) in objIdList:
                updateList.append(p)
            else:
                createList.append(p)
        self.update(objectList=updateList)
        self.create(objectList=createList)
