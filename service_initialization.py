import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from apiclient.discovery import build
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_PATH = parentdir + "\Build\service_account.json" 


def get_service_account(SCOPES, API_NAME, API_VERSION):
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_PATH, scopes=SCOPES)
    service = build(API_NAME, API_VERSION, credentials=credentials)
    
    return service