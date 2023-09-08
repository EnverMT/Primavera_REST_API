from dotenv import load_dotenv
from Primavera_REST_Api import Primavera
import os
import pytest


@pytest.fixture(scope='module')
def app() -> Primavera:
    load_dotenv()

    EPPM_LOGIN = os.getenv('eppm_login')
    EPPM_PASSWORD = os.getenv('eppm_password')
    EPPM_DATABASE = os.getenv('eppm_database')
    EPPM_PREFIX = os.getenv('eppm_prefix')

    app = Primavera(rest_api_prefix=EPPM_PREFIX,
                    database_name=EPPM_DATABASE,
                    login=EPPM_LOGIN,
                    password=EPPM_PASSWORD)

    return app


test_project_data = {
    'TEST_PROJECT_NAME': 'test web service',
    'TEST_PROJECT_ID': 'testws1',
    'TEST_ParentEPSObjectId': 3667
}


def get_project_ObjectId(app: Primavera, id: int) -> int | None:
    projects = app.project.read(['Id'])
    if id in [p['Id'] for p in projects]:
        return [p['ObjectId'] for p in projects if p['Id'] == id][0]
    return None