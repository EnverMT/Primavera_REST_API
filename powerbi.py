from Primavera_REST_Api import Primavera
import pandas as pd


EPPM_LOGIN = "powerWeb"
EPPM_PASSWORD = "Power-Web1"
EPPM_DATABASE = "eppm"
EPPM_PREFIX = "http://10.1.20.186:8206/p6ws/restapi"

PROJECT_SHORT_CODE = "T24" #Project ID

app = Primavera(rest_api_prefix=EPPM_PREFIX,
                database_name=EPPM_DATABASE,
                login=EPPM_LOGIN,
                password=EPPM_PASSWORD)

app.select_project(projectId=PROJECT_SHORT_CODE)

# Get data from server and convert them to DataFrame
wbs = pd.DataFrame(app.wbs.read())
activity = pd.DataFrame(app.activity.read())
resource = pd.DataFrame(app.resource.read())
resourceAssignment = pd.DataFrame(app.resourceAssignment.read())

