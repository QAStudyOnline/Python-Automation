# virtual env in is technology for create isolated namespace for project
# it is required to avoid issues when we have two projects what use same libs but with different versions
# how to create virtual environment
python -m venv .env
# how to activate virtual environment
# Windows
\.env\Scripts\activate.bat
# Shell (MacOS and Linux)
source .env/bin/activate

# pip it is a python package\dependency manager
# pip can install lib into the os or virtual environment to allow usages\import
# how to install some lib
pip install request

# requirements.txt it is a standard file with list of libs what should be installed before run software

pip install -r requirements.txt