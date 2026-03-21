import os
import sys

# Activate the virtual environment
venv_path = os.path.join(os.path.dirname(__file__), 'venv')
site_packages = os.path.join(venv_path, 'lib', 'python3.6', 'site-packages')  # replace 3.X with your version
sys.path.insert(0, site_packages)

from app import app

application = app

if __name__ == '__main__':
    application.run()

