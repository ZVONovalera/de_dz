import requests
import ssl
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def fetch_data_from_opendota_api(endpoint, **context):
    response = requests.get(f"https://api.opendota.com/api/{endpoint}",verify=False)
    data = response.json()
    return data

