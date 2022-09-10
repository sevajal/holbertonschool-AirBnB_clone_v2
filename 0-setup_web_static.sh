#!/usr/bin/env bash
# Script that sets up my web servers for the deployment of web_static.
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i 's/^\tlocation \/ {/\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;/' /etc/nginx/sites-available/default
sudo nginx -t
sudo service nginx restart
