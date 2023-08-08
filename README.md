# Primavera EPPM Web Services programming

Primavera allows to use REST API. 
---

### Plans to implement:
#### CRUD operations:
- [x] Read objects
- [x] Create objects
- [x] Update objects
- [x] Delete object

#### Import/Export
- [x] Activities
- [x] Activity Codes
- [x] Activity Code Assignments
- [x] Resources
- [x] Resource Assignments
- [x] WBS
- [ ] Relationships
- [ ] Risks
- [x] Role

---

### System requirements:
- Primavera EPPM v22
- Access to P6WebServices

---

RestAPI documentation: [REST API Documentation](https://docs.oracle.com/cd/F37125_01/English/Integration_Documentation/rest_api/D100079.html)

---

### How to use:
1. Create Python virtual enviroment
```
python -m venv venv
```
2. Install the package 
```
pip install Primavera-REST-Api
```
3. Example code
```
from Primavera_REST_Api import Primavera

EPPM_LOGIN = "testuser"
EPPM_PASSWORD = "testuser1903"
EPPM_DATABASE = "EPPM"
EPPM_PREFIX = "http://10.1.10.203:8206/p6ws/restapi"


PROJECT_SHORT_CODE = "testproj"
EXPORT_TABLES_TO_CSV = True  # Export Tables to CSV file


app = Primavera(rest_api_prefix=EPPM_PREFIX,
                database_name=EPPM_DATABASE,
                login=EPPM_LOGIN,
                password=EPPM_PASSWORD)


app.select_project(projectId=PROJECT_SHORT_CODE)

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


```
