from dotenv import load_dotenv
import os


def test_envVariables():
    load_dotenv()
    assert os.getenv('eppm_login') != "" and os.getenv('eppm_login') != None
    assert os.getenv('eppm_password') != "" and os.getenv('eppm_password') != None
    assert os.getenv('eppm_database') != "" and os.getenv('eppm_database') != None
    assert os.getenv('eppm_prefix') != "" and os.getenv('eppm_prefix') != None
