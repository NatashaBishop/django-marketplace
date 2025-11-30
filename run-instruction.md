# Notes & Quick run instructions  
1] Install dependencies (from project root):  
```ruby
#bash
pip install -r requirements.txt
```
2] Migrations for token_blacklist  
Since rest_framework_simplejwt.token_blacklist is enabled, run migrations:  
```ruby
#bash
python manage.py makemigrations
python manage.py migrate
```
3] Run tests (pytest will pick up the DJANGO_SETTINGS_MODULE from pytest.ini):  
```ruby
#bash
pytest -q
```
4] Test the endpoints manually:  

- Register: POST /api/auth/register/ (JSON: username, email, password, password2)  
- Token obtain: POST /api/auth/token/ (username, password) → returns access & refresh  
- Token refresh: POST /api/auth/token/refresh/ (refresh)  
- Logout/blacklist: POST /api/auth/logout/ (body { "refresh": <refresh_token> }) — must be authenticated (send Authorization: Bearer <access>)  


```
# I dont' know when  
# Run:  
python manage.py runserver  
```
#########################################  
# ChatGPT version of Quick start:  
```ruby
#bash
unzip barter-marketplace-full-runable.zip
cd barter-marketplace-full-runable
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# create Postgres DB/user per .env or change .env to SQLite if preferred
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# run tests
pytest -q
```



