# Primavera EPPM Web Services programming

Primavera allows to use REST API. 
---

### Plans to implement:
#### CRUD operations:
- [x] Read objects
- [x] Create objects
- [x] Update objects
- [ ] Delete object

#### Import/Export
- [x] Activities
- [ ] Activity Codes
- [ ] Activity Code Assignments
- [ ] Resources
- [x] Resource Assignments
- [ ] WBS
- [ ] Relationships
- [ ] Risks
- [ ] Role

---

### System requirements:
- Primavera EPPM v22
- P6WebServices

---

RestAPI documentation: [REST API Documentation](https://docs.oracle.com/cd/F37125_01/English/Integration_Documentation/rest_api/D100079.html)

---

### How to use:
1. [Instal python](https://www.python.org/downloads/)
2. Clone this repository 
```
git clone https://github.com/EnverMT/PrimaveraREST_API.git
```
3. Enter to directory 
```
cd PrimaveraREST_API
```
4. Create python virtual enviroment
```
python -m venv venv
```
5. Install required packages from list
```
pip install -r requirements.txt
```
6. Rename **.env.example** to **.env**
7. Edit **.env** and update *login* and *password*. 
8. Give access to module **Web Services** in Primavera
9. Give **Project Access** to appropriate OBS
10. Update variables in **main.py**
```
EPPM_DATABASE = <Your database name>
EPPM_PREFIX = <Primavera REST API base endpoint>
PROJECT_SHORT_CODE = <Primavera Project's ID>
EXPORT_TABLES_TO_CSV = <True/False>
```
