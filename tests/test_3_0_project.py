from dotenv import load_dotenv
from Primavera_REST_Api import Primavera
import os
from test_0_app import app
import json


class TestProject:
    TEST_PROJECT_NAME = "test web service"
    TEST_PROJECT_ID = "testws1"
    TEST_ParentEPSObjectId = 76528

    def check_if_already_exists_test_project(self, app: Primavera) -> int:
        projects = app.project.read(['Id'])
        if self.TEST_PROJECT_ID in [p['Id'] for p in projects]:
            return [p['ObjectId'] for p in projects if p['Id'] == self.TEST_PROJECT_ID][0]

    def test_project_create(self, app: Primavera):
        if self.check_if_already_exists_test_project(app=app):
            app.project.delete()

        app.project.create([{
            "Name": self.TEST_PROJECT_NAME,
            "Id": self.TEST_PROJECT_ID,
            "ParentEPSObjectId": self.TEST_ParentEPSObjectId
        }])
        print(json.dumps(obj=app.project.read(['Name', 'Id', 'ParentEPSObjectId']), indent=2))
