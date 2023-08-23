from dotenv import load_dotenv
from Primavera_REST_Api import Primavera
import os


class TestSession:
    load_dotenv()

    EPPM_LOGIN = os.getenv('eppm_login')
    EPPM_PASSWORD = os.getenv('eppm_password')
    EPPM_DATABASE = os.getenv('eppm_database')
    EPPM_PREFIX = os.getenv('eppm_prefix')

    def test_primavera(self):
        app = Primavera(rest_api_prefix=self.EPPM_PREFIX,
                    database_name=self.EPPM_DATABASE,
                    login=self.EPPM_LOGIN,
                    password=self.EPPM_PASSWORD)
        
        assert app != None
        assert app.eppmSession != None

    
        
