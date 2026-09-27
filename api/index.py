import os
import sys

# Ensure root directory is on the Python path so retailsync_app can be imported
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from retailsync_app.main import app

# Vercel Serverless entrypoint exports the ASGI app
