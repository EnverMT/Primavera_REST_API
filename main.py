from Primavera_REST_Api import Primavera
import pandas as pd


EPPM_LOGIN = "powerWeb"
EPPM_PASSWORD = "Power-Web1"
EPPM_DATABASE = "eppm"
EPPM_PREFIX = "http://10.1.20.186:8206/p6ws/restapi"

PROJECT_SHORT_CODE = "T24"

app = Primavera(rest_api_prefix=EPPM_PREFIX,
                database_name=EPPM_DATABASE,
                login=EPPM_LOGIN,
                password=EPPM_PASSWORD)

app.select_project(projectId=PROJECT_SHORT_CODE)

# Get data from server and convert them to DataFrame
wbs_df = pd.DataFrame(app.wbs.read())
activity_df = pd.DataFrame(app.activity.read())
resource_df = pd.DataFrame(app.resource.read())
resourceAssignment_df = pd.DataFrame(app.resourceAssignment.read())


EXPORT_TO_EXCEL = True  # Export to file if True

if EXPORT_TO_EXCEL:
    excel_file = "excel/Project24.xlsx"

    # write dataframes to Excel file
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        wbs_df.to_excel(writer, sheet_name='wbs', index=False)
        activity_df.to_excel(writer, sheet_name='activity', index=False)
        resource_df.to_excel(writer, sheet_name='resource', index=False)
        resourceAssignment_df.to_excel(writer, sheet_name='resourceAssignment', index=False)