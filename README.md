# Create virtual environment
python -m venv venv

# Activate virtual environment
## For windows
.\venv\Scripts\activate.bat

## For ubuntu
source ./venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run 
flask run
