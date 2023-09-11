from Primavera_REST_Api import Primavera
from dotenv import load_dotenv
import os
import json


load_dotenv()

EPPM_LOGIN = os.getenv('eppm_login')
EPPM_PASSWORD = os.getenv('eppm_password')
EPPM_DATABASE = os.getenv('eppm_database')
EPPM_PREFIX = os.getenv('eppm_prefix')


PROJECT_SHORT_CODE = "testproj"
EXPORT_TABLES_TO_CSV = False  # Export Tables to CSV file


app = Primavera(rest_api_prefix=EPPM_PREFIX,
                database_name=EPPM_DATABASE,
                login=EPPM_LOGIN,
                password=EPPM_PASSWORD)


# # print(app.project.read(['Name', 'ParentEPSObjectId']))
# print(json.dumps(app.eps.read(), indent=2))

# epss = app.eps.read(fields=['ParentObjectId'])
# root_eps = [e for e in epss if e.get('ParentObjectId') == None]
# print(root_eps)

# app.select_project(projectId=PROJECT_SHORT_CODE)

if EXPORT_TABLES_TO_CSV:
    # Export tables to CSV files
    directory = 'csv'

    app.project.export_to_CSV(directory=directory, fields=['Id', 'Name'])
    app.wbs.export_to_CSV(fields=['ParentObjectId', 'ObjectId', 'Name', 'Code'], directory=directory)
    app.activity.export_to_CSV(fields=['ObjectId', 'Id', 'Name', 'PlannedDuration',
                                       'StartDate', 'FinishDate', 'ActualDuration'], directory=directory)
    app.resource.export_to_CSV(fields=['ObjectId', 'Id', 'Name'], directory=directory)
    app.resourceAssignment.export_to_CSV(
        fields=['ActivityObjectId', 'ResourceObjectId', 'PlannedUnits', 'ActivityId', 'ResourceId'], directory=directory)
    app.resourceRole.export_to_CSV(directory=directory)
    app.role.export_to_CSV(directory=directory)

# app.activity.import_CSV_to_EPPM(directory='csv', filename='import - activity.csv', delimiter=',')
