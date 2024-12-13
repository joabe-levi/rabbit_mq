from dotenv import load_dotenv
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

load_dotenv()

host = os.getenv('host')
port = os.getenv('port')
username = os.getenv('username')
password = os.getenv('password')
