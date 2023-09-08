from Primavera_REST_Api import Primavera
from test_0_app import app, test_project_data, get_project_ObjectId
import pytest


class TestProject:
    TEST_PROJECT_NAME = test_project_data.get('TEST_PROJECT_NAME')
    TEST_PROJECT_ID = test_project_data.get('TEST_PROJECT_ID')
    TEST_ParentEPSObjectId = test_project_data.get('TEST_ParentEPSObjectId')

    def test_project_create(self, app: Primavera):
        existing_test_project_object_id = get_project_ObjectId(app=app, id=self.TEST_PROJECT_ID)
        if existing_test_project_object_id:
            app.project.delete(objectIdsList=[existing_test_project_object_id])

        app.project.create([{
            "Name": self.TEST_PROJECT_NAME,
            "Id": self.TEST_PROJECT_ID,
            "ParentEPSObjectId": self.TEST_ParentEPSObjectId
        }])

    def test_select_project_fails(self, app: Primavera):
        with pytest.raises(Exception):
            app.select_project('asdfasd24')
