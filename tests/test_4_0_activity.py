from Primavera_REST_Api import Primavera
from test_0_app import app, test_project_data


class TestActivity:
    TEST_PROJECT_NAME = test_project_data.get('TEST_PROJECT_NAME')
    TEST_PROJECT_ID = test_project_data.get('TEST_PROJECT_ID')
    TEST_ParentEPSObjectId = test_project_data.get('TEST_ParentEPSObjectId')

    def test_activity_create(self, app: Primavera):
        app.select_project(self.TEST_PROJECT_ID)
        objectList = [{'Id': "T1000", 'Name': "Test1000"},
                      {'Id': "T1001", 'Name': "Test1001"},
                      {'Id': "G1000", 'Name': "TestG1000"},
                      {'Id': "B1000", 'Name': "TestB1000"},
                      {'Id': "B1001", 'Name': "TestB1001"}]
        app.activity.create(objectList=objectList, chunkSize=10)

    def test_activity_update(self, app: Primavera):
        app.select_project(self.TEST_PROJECT_ID)
        activity = app.activity.read()[0]
        objectList = [{
            'Id': "T2000",
            'Name': "Test2000",
            'ObjectId': activity.get('ObjectId')
        }]
        app.activity.update(objectList=objectList)
        activity = app.activity.read(['Id', 'Name'])
        length = app.activity.getFieldLength('Id')
        print("activity: ", activity)
        print("length:", length)

    def test_activity_filter(self, app: Primavera):
        app.select_project(self.TEST_PROJECT_ID)

        activity = app.activity.read(filters="Id :like: '%B1000%'")
        assert activity[0].get('Name') == 'TestB1000'

        activity = app.activity.read(filters="Id :like: '%G1000%'")
        assert activity[0].get('Name') == 'TestG1000'
