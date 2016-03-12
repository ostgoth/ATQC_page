Grey text it’s alternative and more advanced way, so might be skipped.

Installing software:
sudo apt-get install python3.5 
sudo apt-get install python-pip
sudo apt-get install python-pip3
sudo apt-get install python-dev 
sudo apt-get install libjpeg8-dev
sudo apt-get install libpq-dev
sudo apt-get install python-psycopg2
sudo apt-get install postgresql postgresql-contrib
( sudo pip install virtualenvwrapper )


Launching postgre:
sudo -i -u postgres
psql
CREATE DATABASE sharing_dev;
CREATE USER sharing_user WITH password 'sharing_password';
GRANT ALL privileges ON DATABASE sharing_dev TO sharing_user;
\q

Deploying environment:
cd /path/to/new/virtual/environment  ( or mkproject sharing && workon sharing )
virtualenv sharingENV
source ./sharingENV/bin/activate
pip install -r requirements.txt

Migrate: 
python manage.py migrate

Load simple data from fixtures:
python3.5 manage.py loaddata initial_data.json




