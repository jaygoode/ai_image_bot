import hvac
import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)


token = ""
url = ""
client = hvac.Client(url=url, token=token)

if not client.is_authenticated():
    print
