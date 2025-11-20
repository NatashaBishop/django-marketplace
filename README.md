# marketplace with Django
Building market place with the following stack: Django (Python framework), some JS framework on the front end, PostgreSQL (looking for a reliable Posrgres hosting at the moment)  
This directory contains:  
- Complete project folder structure
- Configured PostgreSQL .env
- Split settings (base/dev/prod)
- DRF setup + dependencies in requirements.txt
- Ready-to-run manage.py
- All the files needed to run the project functionality
- README file
## How To Test API  
```
Run:
python manage.py runserver
``` 
Then visit these API endpoints:  
- http://127.0.0.1:8000/api/products/  
- http://127.0.0.1:8000/api/orders/  
- http://127.0.0.1:8000/api/payments/  

## How to run project  
Clone or download barter-marketplace directory to your machine  
Quick start after download:  
unzip barter-marketplace-full.zip  

```
# cd barter-marketplace
Bash  

python -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt  
# create DB & user in PostgreSQL per .env, or change .env to use local settings  
# Run migrations and create a superuser:  
python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  
``` 
Test the API endpoints: 
- POST /api/auth/register/ with JSON:
```
{
  "username": "alice",
  "email": "alice@example.com",
  "password": "SuperSecret123!",
  "password2": "SuperSecret123!"
}
```
- POST /api/auth/token/ with username+password to get access & refresh tokens.  
- POST /api/auth/token/refresh/ to refresh access token.  
