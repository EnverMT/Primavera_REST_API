import requests


class EppmSession:
    def __init__(self, rest_api_prefix: str | None,
                 database_name: str | None,
                 login: str | None,
                 password: str | None):
        if rest_api_prefix == None or database_name == None or login == None or password == None:
            raise Exception("Creditionals to connect database cannot be None")

        self.session = requests.Session()
        self.prefix = rest_api_prefix

        url = f"{self.prefix}/login"
        headers = {"username": login, "password": password}
        params = {"DatabaseName": database_name}
        res = self.session.post(url, headers=headers, params=params)
        if res.status_code != 200:
            raise Exception(f"ERROR on LOGIN: {res.text}") 

        self.selectedProjectObjectId: int | None = None   
