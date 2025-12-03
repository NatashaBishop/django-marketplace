# files for docker enclude:  

✔️ Dockerfile  
- Python 3.12 slim  
- Installs requirements  
- Copies project files  
- Uses entrypoint for migrations on container start  

✔️ docker-compose.yml  
- web service (Django)  
- db service (PostgreSQL 15)  
- Automatic environment variable wiring  
- Persistent volume pgdata  

✔️ entrypoint.sh  
- Runs Django migrations automatically  
- Starts the server  

# To run this app in Docker:  
```ruby
unzip barter-marketplace-docker.zip
docker compose up --build
```
The app will be available at:
👉 http://localhost:8000
Postgres will be running at:
👉 localhost:5433 (mapped to container’s 5432)
