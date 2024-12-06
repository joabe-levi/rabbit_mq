from dotenv import load_dotenv
import os

load_dotenv()

host = os.get_env('host')
port = os.get_env('port')
username = os.get_env('username')
password = os.get_env('password')
