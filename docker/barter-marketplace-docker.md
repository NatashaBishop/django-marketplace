# files for docker enclude:  

✔️ Dockerfile  
- Python 3.12 slim  
- Installs requirements  
- Copies project files  
- Uses entrypoint for migrations on container start  

✔️ docker-compose.yml  
- ```web``` service (Django)  
- ```db``` service (PostgreSQL 15)  
- Automatic environment variable wiring  
- Persistent volume ```pgdata```

✔️ entrypoint.sh  
- Runs Django migrations automatically  
- Starts the server  

Despite I have doker files in a separate folder here, it is better to place all 3 files in the root:  
```
barter-marketplace/  
│  
├── Dockerfile  
├── docker-compose.yml  
├── entrypoint.sh  
├── manage.py  
├── marketplace/  
├── apps/  
├── requirements.txt  
├── .env  
└── ...  
```
This is why:  
✔ Clean  
✔ Standard Django deployment layout  
✔ Works with Render, Railway, AWS, DigitalOcean, etc.  
# To run this app in Docker:  
Quick start (Docker)  
```ruby
unzip barter-marketplace-unified.zip
cd barter-marketplace-unified
docker compose up --build
```
The app will be available at:  
👉 http://localhost:8000  
Postgres will be running at:  
👉 localhost:5433 (mapped to container’s 5432)  
