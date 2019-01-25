#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y install nginx
sudo apt-get -y install emacs

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo "I AM A FAKE HTML DOC" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

file="/etc/nginx/sites-available/default"

sudo sed -i '/^\tserver_name localhost;/a\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;}\n' $file

sudo service nginx reload
sudo service nginx restart
