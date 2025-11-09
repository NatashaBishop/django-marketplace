# marketplace with Django
with the following stack: Django (Python framework), some JS framework on the front end, PostgreSQL (looking for a reliable Posrgres hosting at the moment)  
This directory contains:  
- Complete project folder structure
- Configured PostgreSQL .env
- Split settings (base/dev/prod)
- DRF setup + dependencies in requirements.txt
- Ready-to-run manage.py
## Test API  
```
Run:
python manage.py runserver
``` 
Then visit these API endpoints:  
- http://127.0.0.1:8000/api/products/  
- http://127.0.0.1:8000/api/orders/  
- http://127.0.0.1:8000/api/payments/  

## How to run  
clone barter-marketplace directory to your machine
```
Bash  
cd barter-marketplace
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
``` 


