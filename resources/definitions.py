import os
from dotenv import load_dotenv


# application environment variables
load_dotenv()
SERVICE_PORT = os.getenv("FLASK_SERVICE_PORT")
SWAGGER_DIR = os.getenv("SWAGGER_DIR")
SWAGGER_CONF = os.getenv("SWAGGER_CONF")

# application global scope references
DEFAULT_TESSERACT_CONFIG = "--psm 6"


# application specific helper functions
valid_mimetype = (
    lambda abstract_file:(
        True if abstract_file.mimetype == 'image/png' else False
    )
)
