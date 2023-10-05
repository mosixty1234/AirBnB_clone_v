#!/usr/bin/env bash
#Bash script that sets up web servers for the deployment of web_static

if ! command -v nginx &>/dev/null;
then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm -f /data/web_static/current
ln -s  /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config="/etc/nginx/sites-available/default"
line_add="location /hbnb_static/ { alias /data/web_static/current/; }"

sudo sed -i "/location \/ {/a $line_add" "$config"

sudo nginx -t
sudo service nginx restart
