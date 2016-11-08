#ampere_health

Set up Virtual Env first. Follow steps given at http://docs.python-guide.org/en/latest/dev/virtualenvs/

1. Update mysql database credentials in settings.py under 'DATABASES'.
2. Login into https://dev.fitbit.com/apps/new
3. Register an app.
4. Get OAuth 2.0 Client ID & Secret key
5. Add/Edit Fitbit cosumer Keys in settings.py
6. pip install -r requirements.txt
7. create database ampere
8. python manage.py makemigrate
9. pip install django-fitbit
10. pip install -r requirements.txt
11. python manage.py runserver 0.0.0.0:8082
12. Go to http://127.0.0.1:8082/ and click on given link
13. Login as your fitbit account
14. Click on 'Ok' when ask for permissions.
