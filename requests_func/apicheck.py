import requests
import re
import logging
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from requests_func.decorator import errorCheck

# Define the retry strategy
retry_strategy = Retry(
    total=3,  # Maximum number of retries
    backoff_factor=2, # Exponential backoff factor (e.g., 2 means 1, 2, 4, 8 seconds, 
    status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry on
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount('http://', adapter)
session.mount('https://', adapter)

@errorCheck
# Define GET Method
def get(url, **kwargs):
    
    #try:
    response = session.get(url, timeout=30)    
    if re.search('^2', str(response.status_code)):
        return response
    else:
        logging.warn(f'Status Code Error: {response.status_code}')
        raise(f'Status Code Error')
    
    '''
    except requests.exceptions.Timeout:
        logging.warn(f'TimeOut Error: {response.status_code}')
        raise
    
    except requests.ConnectionError:
        logging.critical(f'ConnectionError: {url}')
        raise
    '''
        
# Define POST Method
def post(url, **kwargs):
    
    try:
        response = session.post(url, timeout=30)
        
        if re.search('^2', str(response.status_code)):
            return response
        else:
            logging.warn(f'Status Code Error: {response.status_code}')
            raise(f'Status Code Error')
        
    except requests.exceptions.Timeout:
        logging.warn(f'TimeOut Error: {response.status_code}')
        raise
    
    except requests.ConnectionError:
        logging.critical(f'ConnectionError: {url}')
        raise