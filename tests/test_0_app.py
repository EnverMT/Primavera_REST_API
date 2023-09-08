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
