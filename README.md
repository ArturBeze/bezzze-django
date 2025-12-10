# ReadMe

Install certbot and create certificates

    sudo apt update

    sudo apt install certbot python3-certbot-nginx -y

    sudo certbot --nginx -d bezzze.ru -d www.bezzze.ru

    sudo certbot --nginx -d bezzze.ru -d www.bezzze.ru


Certificate location

    ssl_certificate_key /etc/letsencrypt/live/


Check nginx status

    sudo systemctl status nginx

...or

    sudo nginx -t
    
Stop nginx

    sudo systemctl stop nginx

... if don't work

    sudo pkill -f nginx & wait $! sudo systemctl start nginx

Start nginx

    sudo systemctl start nginx
    
Restart nginx

    sudo systemctl restart nginx

To delete all containers including its volumes

    docker rm -vf $(docker ps -aq)

To delete all the images

    docker rmi -f $(docker images -aq)

Create django project

    cd project/django
    mkdir app
    cd app
    django-admin startproject app .

Setup work with PostgreSQL in django/app/app/settings.py

    import os

    SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
    DEBUG = os.environ.get("DJANGO_DEBUG") == "1"
    
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": 5432,
        }
    }
    
    ALLOWED_HOSTS = ["bezzze.ru"]

Create django migration

    docker compose exec django python manage.py migrate

Create django admin

    docker compose exec django python manage.py createsuperuser

If error - Error: EACCES: permission denied, mkdir '/home/node/.n8n'

    mkdir -p n8n_data
    sudo chown -R 1000:1000 n8n_data

    
