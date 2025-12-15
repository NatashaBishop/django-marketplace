## Adding production-ready Docker (Gunicorn + Nginx + static files)  

Full production-ready Docker setup with:  

✅ Gunicorn (process manager for Django)  
✅ Nginx reverse proxy  
✅ Static file collection & serving  
✅ Updated Dockerfile, docker-compose.prod.yml, nginx.conf  
✅ Separate production entrypoint  
✅ Proper volumes for /static/ and /media/  
✅ Secure production settings overrides  

## Ready in 2 containers (recommended)  
nginx (public-facing, serves static files + proxies requests)  
web (Django + Gunicorn)  
