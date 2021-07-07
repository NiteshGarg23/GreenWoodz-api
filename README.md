# Create virtual environment
python -m venv venv

# Activate virtual environment
## For windows
.\venv\Scripts\actiavte.bat

## For ubuntu
source ./venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run 
flask run
