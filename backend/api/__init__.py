import os
import sys

# Tambahkan folder project ke Python path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Import FastAPI app dari backend
from backend.main import app