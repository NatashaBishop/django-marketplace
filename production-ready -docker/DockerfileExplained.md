# bash 

```
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
```
# we are in the project root, but working in enother /app derectory  
set the current working directory inside the container to /app:
```WORKDIR /app ```
from this point onward, all commands will run inside the folder /app, in case there is no app directory, it will be created  
#Installs only the explicitly listed packages, without pulling in optional recommended packages, which keeps the image smaller and avoids unnecessary dependencies: 
```
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*  
```
Step-by-step explanation for the last line:  
- && — chains commands together. The second runs only if the first succeeds.  
- rm -rf — forcefully removes files/directories (-r = recursive, -f = force).  
- /var/lib/apt/lists/* — this directory stores cached metadata about available packages (downloaded during apt-get update).  
As a result: It deletes the package list cache after installation is complete.  
```

```
save copy of requirements.txt to app directory:
```
COPY requirements.txt /app/
```
# "--no-cache-dir" This is the important part for Docker. 
It tells pip:  
Do not store downloaded package files in pip’s cache.  
Using --no-cache-dir keeps the image much smaller and cleaner (cache can add tens or hundreds of MB to your final image).  
It reproduces a Python environment in Docker:  
```
RUN pip install --no-cache-dir -r requirements.txt 
```
 It copies everything in my current build (the directory where I run docker build) into the /app directory inside the container image:
```
COPY . /app

RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000
CMD ["gunicorn", "marketplace.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
```
