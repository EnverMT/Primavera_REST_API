from Primavera_REST_Api.__eppmSession import EppmSession
from Primavera_REST_Api.__method import Method
from Primavera_REST_Api.__endpointsEnum import EndpointEnum


class Primavera:
    def __init__(self, rest_api_prefix: str | None,
                 database_name: str | None,
                 login: str | None,
                 password: str | None):
        """"
             Usual prefix is IP + p6ws + restapi as String http://10.1.10.203:8206/p6ws/restapi
        """

        self.eppmSession = EppmSession(rest_api_prefix=rest_api_prefix,
                                       database_name=database_name,
                                       login=login,
                                       password=password)

        # Methods
        self.project = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.project)
        self.activity = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.activity)
        self.activityCode = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.activityCode)
        self.activityCodeAssignment = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.activityCodeAssignment)
        self.wbs = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.wbs)
        self.resource = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.resource)
        self.resourceRole = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.resourceRole)
        self.resourceAssignment = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.resourceAssignment)
        self.role = Method(eppmSession=self.eppmSession, endpoint=EndpointEnum.role)

        self.__projectList = self.project.read(fields=['ObjectId', 'Name', 'Id'])

    def select_project(self, projectId: str) -> bool:
        """
            Select project for further filtering of objects

            Returns:
            json: Is project exists in database
        """
        if projectId not in [project['Id'] for project in self.__projectList]:
            raise Exception("Project Code doesn't exist in database")

        self.eppmSession.selectedProjectObjectId = [
            project['ObjectId'] for project in self.__projectList if project['Id'] == projectId
        ][0]
        return self.eppmSession.selectedProjectObjectId
