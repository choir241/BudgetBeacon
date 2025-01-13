from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.services.account import Account
from appwrite.id import ID
import os
from .env import init_env

init_env()

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project(os.environ['PROJECT_ID'])
client.set_key(os.environ['API_KEY'])

account = Account(client)

def register(user_data):
    account.create(
        user_id=ID.unique(),
        email=user_data["email"],
        password=user_data["password"],
        name=user_data["name"]
    )
    login(user_data)

def login(user_data):
    account.create_email_password_session(
        email=user_data["email"],
        password=user_data["password"]
    )
    print(get_account())

def get_account():
    account.get()

def logout():
    account.delete_sessions()