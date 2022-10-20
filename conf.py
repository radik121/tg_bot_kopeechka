from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

TG_API = os.environ.get('TG_API')
KP_API = os.getenv('KP_API')