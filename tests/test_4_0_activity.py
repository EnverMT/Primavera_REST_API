from Primavera_REST_Api import Primavera
from test_0_app import app, test_project_data


class TestActivity:
    TEST_PROJECT_NAME = test_project_data.get('TEST_PROJECT_NAME')
    TEST_PROJECT_ID = test_project_data.get('TEST_PROJECT_ID')
    TEST_ParentEPSObjectId = test_project_data.get('TEST_ParentEPSObjectId')

    def test_activity_create(self, app: Primavera):
        app.select_project(self.TEST_PROJECT_ID)
        objectList = [{
            'Id': "T1000",
            'Name': "Test1000"
        }]
        app.activity.create(objectList=objectList)
