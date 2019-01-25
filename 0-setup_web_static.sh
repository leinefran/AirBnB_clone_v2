#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "I AM A FAKE HTML DOC" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

file="/etc/nginx/sites-available/default"

sed -i '/^\tserver_name localhost;/a\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;}\n' $file

service nginx restart
