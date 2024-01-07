import hvac
from logger_setup import logger


class Vault:
    def __init__(self, token: str, url: str):
        self.client = self.authenticate_client(token, url)

    def authenticate_client(self, token: str, url: str):
        client = hvac.Client(url=url, token=token)

        if not client.is_authenticated():
            logger.error("Vault client could not authenticate.")

        return client

    def create_or_update_secret(self, username: str, password: str):
        self.client.secrets.kv.v2.create_or_update_secret(
            path="secret/website_credentials",
            secret=dict(username=username, password=password),
        )

    # path = "secret/website_credentials"
    def get_credentials(self, path: str):
        data = self.client.secrets.kv.v2.read_secret_version(path=path)

        if data and "data" in data:
            username = data["data"]["data"]["username"]
            password = data["data"]["data"]["password"]
            return (username, password)
        else:
            logger.error("Credentials not found in Vault")
