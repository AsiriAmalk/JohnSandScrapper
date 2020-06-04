## John Sand Scrapper
#### This uses python 3.6 <
####### Go to root "JohnSandScrapper" folder and open cmd/terminal
#### Create Virtualenv
pip install virtualenv\
virtualenv johnscrapper

#### Activate Virtualenv (Windows)
johnscrapper\Scripts\activate

#### Activate Virtualenv (Mac OS \ Linux)
source johnscrapper/bin/activate

### Install Requirements
pip install -r requirements.txt

### Open Django
python manage.py runserver

###### Go to `http://127.0.0.1:8000/`

### Admin Panal
python manage.py makemigrations\
python manage.py migrate\
python manage.py createsuperuser
###### Set `User Name` and `Password`

### DataBase used `Sqlite3`

