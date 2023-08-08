from Primavera_REST_Api import Primavera
from dotenv import load_dotenv
import os


load_dotenv()

EPPM_LOGIN = os.getenv('eppm_login')
EPPM_PASSWORD = os.getenv('eppm_password')
EPPM_DATABASE = os.getenv('eppm_database')
EPPM_PREFIX = os.getenv('eppm_prefix')


PROJECT_SHORT_CODE = "testproj"
EXPORT_TABLES_TO_CSV = True  # Export Tables to CSV file


app = Primavera(rest_api_prefix=EPPM_PREFIX,
                database_name=EPPM_DATABASE,
                login=EPPM_LOGIN,
                password=EPPM_PASSWORD)


app.select_project(projectId=PROJECT_SHORT_CODE)

if EXPORT_TABLES_TO_CSV:
    app.export_to_CSV()

app.activity.import_CSV_to_EPPM(directory='csv', filename='import - activity.csv', delimiter=',')
