from Primavera_REST_Api import Primavera
from test_0_app import app, test_project_data, get_project_ObjectId


class TestProject:
    TEST_PROJECT_ID = test_project_data.get('TEST_PROJECT_ID')

    def test_project_delete(self, app: Primavera):
        existing_test_project_object_id = get_project_ObjectId(app=app, id=self.TEST_PROJECT_ID)
        if existing_test_project_object_id:
            app.project.delete(objectIdsList=[existing_test_project_object_id])
