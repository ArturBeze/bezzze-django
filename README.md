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
