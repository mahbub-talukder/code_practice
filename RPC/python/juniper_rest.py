import requests
from requests.exceptions import ConnectionError,Timeout,RequestException
from base64 import b64encode
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def is_xml(text):
    try:
        ET.fromstring(text)
        return True
    except ET.ParseError:
        return False
    
def is_html(text):
    try:
        soup = BeautifulSoup(text, 'html.parser')
        return True
    except:
        return False

BASE_URL = "http://10.172.16.4:3000/rpc"
END_POINT_NAME = "get-software-informations"
URL = f"{BASE_URL}/{END_POINT_NAME}"
USERNAME = 'devops'
PASSWORD = 'devOps@321#'

headers = {
    "Content-Type": "application/xml",
    "Accept": "application/json"
}
auth = (USERNAME, PASSWORD)

# Create a Basic Authentication header with base64 encryption text value
# credentials = f'{USERNAME}:{PASSWORD}'
# credentials_encoded = b64encode(credentials.encode('utf-8')).decode('utf-8')
# print("credentials_encoded-->", credentials_encoded) # ZGV2b3BzOmRldk9wc0AzMjEj
# headers = {
#     "Content-Type": "application/xml",
#     "Accept": "application/json",
#     "Authorization": f"Basic {credentials_encoded}"
# }
try:
    response = requests.get(URL, headers=headers,auth=auth)

    try:

        response_content = response.json()

    except Exception as e:
        
        response_content = response.text

        if is_xml(response_content):
            soup = BeautifulSoup(response_content, 'lxml')
            response_content = soup.find('message').text
            token_url = soup.find('token').text
            if token_url:
                 response_content = f'{response_content} with token_url : {token_url}'

    print("Response Code:", response.status_code)
    print("Response Content:", response_content)

except ConnectionError as connerr:
        print("connerr-->", str(connerr))
    
except Timeout as timeout:
        print("timeout-->", timeout)
     
except RequestException as req_ex:
        print("req_ex-->", req_ex)



