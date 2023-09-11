from Primavera_REST_Api import Primavera
from test_0_app import app, test_project_data
import os
import csv


class TestActivity:
    TEST_PROJECT_ID = test_project_data.get('TEST_PROJECT_ID')
    TEST_DIRECTORY = test_project_data.get('TEST_DIRECTORY')
    TEST_CSV_DELIMITER = test_project_data.get('TEST_CSV_DELIMITER')

    def test_create_empty_csv_file(self):
        filename = 'empty_file.csv'
        current_directory = os.getcwd()
        full_path = os.path.join(current_directory, self.TEST_DIRECTORY)

        file = os.path.join(full_path, filename)
        if not os.path.isdir(full_path):
            os.mkdir(full_path)

        with open(file=file, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=self.TEST_CSV_DELIMITER)
            writer.writerow("")

        assert os.path.isfile(file)

    def test_csv_activity_export(self, app: Primavera):
        app.select_project(projectId=self.TEST_PROJECT_ID)
        app.activity.export_to_CSV(directory=self.TEST_DIRECTORY, delimiter=self.TEST_CSV_DELIMITER)

        filename = 'export - Activity.csv'
        current_directory = os.getcwd()
        full_path = os.path.join(current_directory, self.TEST_DIRECTORY)
        file = os.path.join(full_path, filename)

        with open(file=file, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=self.TEST_CSV_DELIMITER)
            writer.writerow("")

        # assert os.path.isfile(file)
