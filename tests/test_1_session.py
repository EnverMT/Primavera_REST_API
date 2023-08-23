from dotenv import load_dotenv
from Primavera_REST_Api.__eppmSession import EppmSession
import os
import pytest


class TestSession:
    load_dotenv()

    EPPM_LOGIN = os.getenv('eppm_login')
    EPPM_PASSWORD = os.getenv('eppm_password')
    EPPM_DATABASE = os.getenv('eppm_database')
    EPPM_PREFIX = os.getenv('eppm_prefix')

    def test_session_correct(self):
        eppmSession = EppmSession(rest_api_prefix=self.EPPM_PREFIX,
                                  database_name=self.EPPM_DATABASE,
                                  login=self.EPPM_LOGIN,
                                  password=self.EPPM_PASSWORD)

        assert eppmSession != None
        assert eppmSession.selectedProjectObjectId == None
    
    def test_session_incorrect_1(self):

        with pytest.raises(Exception):            
            self.EPPM_LOGIN = ""
            eppmSession = EppmSession(rest_api_prefix=self.EPPM_PREFIX,
                                    database_name=self.EPPM_DATABASE,
                                    login=self.EPPM_LOGIN,
                                    password=self.EPPM_PASSWORD)
    
    def test_session_incorrect_2(self):

        with pytest.raises(Exception):            
            self.EPPM_LOGIN = None
            eppmSession = EppmSession(rest_api_prefix=self.EPPM_PREFIX,
                                    database_name=self.EPPM_DATABASE,
                                    login=self.EPPM_LOGIN,
                                    password=self.EPPM_PASSWORD)




    

        

