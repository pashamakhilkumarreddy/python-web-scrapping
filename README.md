# Web Scrapping using Python

### Steps to run the project
1. sudo apt-get update -y && sudo apt-get upgrade -y
2. sudo apt install python3-pip -y
3. pip install --user pipenv
4. python3 -m venv env
5. source env/bin/activate
6. pipenv install | pipenv install -r requirements.txt | pip install -r requirements.txt

### Some usefull Pipenv commands

1. pipenv shell - Activate virtual environment
2. pipenv install package_name | pipenv install package_name==0.12.1 - Install a dependency
3. pipenv install -e git+https://github.com/requests/requests.git#egg=requests - Install from VCS
4. pipenv install package_name --dev - Install a dev dependency
5. pipenv lock - Lock the dependencies
6. pipenv install --ignore-pipfile - Use Pipfile.lock to install the dependencies
7. pipenv install - Install all the dependencies in Pipfile
8. pipenv install --dev - Install dev dependencies in Pipfile
9. pipenv graph
10. pipenv open package_name
11. pipenv check - Check for security vulnerabilities
12. pipenv uninstall numpy - Uninstall a dependency 
13. pipenv uninstall --all - Uninstall all dependencies
14. pipenv uninstall --all-dev - Uninstall all dev dependencies
15. pipenv lock -r > requirements.txt
16. pipenv lock -r -d > dev-requirements.txt