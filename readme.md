*** 
before starting there is a few steps that you need to follow

1-) add your local database credentials on settings file
2-) run command: py manage.py makemigrations
3-) run command: py manage.py migrate

4-)run command: py manage.py createsuperuser
5-) run command: py manage.py makemigrations
6-) run command: py manage.py migrate
 
 
URLS :
Admin -> http://127.0.0.1:8000/admin/
Admin CarsApp -> http://127.0.0.1:8000/admin/carsapp/
Admin CarsApp-Cars -> http://127.0.0.1:8000/admin/carsapp/cars/
Admin Cars Detail -> http://127.0.0.1:8000/admin/carsapp/cars/5/Change
Admin : Related Cars History -> http://127.0.0.1:8000/admin/carsapp/cars/5/history/
Admin : To add new car -> http://127.0.0.1:8000/admin/carsapp/cars/add/

API:
All Cars Data -> http://127.0.0.1:8000/api/list/
Specific Car Data -> http://127.0.0.1:8000/api/list/5/
Specific Car Data Raw Json -> http://127.0.0.1:8000/api/list/5/?format=json
Request a query on url -> http://127.0.0.1:8000/api/list/?year=2018

