#!/usr/bin/env bash
# Script that sets up a web server for deploying static web content

# to install nginx
apt-get -y update
apt-get -y install nginx
# set up nginx to listen on port 80
ufw allow 'Nginx HTTP'
# set up nginx default landing page
echo "Hello World!" > /var/www/html/index.nginx-debian.html


# Create the directories
paths=(
        "/data/"
        "/data/web_static/"
        "/data/web_static/releases/"
        "/data/web_static/shared/"
        "/data/web_static/releases/test/"
)
for path in "${paths[@]}"
do
        if [[ ! -d "$path" ]]; then
                mkdir -p "$path"
        fi
done


touch /data/web_static/releases/test/index.html
echo "<html>
        <head>
        </head>
        <body>Welcome to the home page</body>
</html>" > /data/web_static/releases/test/index.html


# Create the symlink
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"
if [[ -L "$link_path" ]]; then
        rm "$link_path"
fi
ln -s "$target_path" "$link_path"


# Gives ownership of the folder to user and group
chown -R ubuntu:ubuntu /data/

# Check if the /hbnb_static exists in the configuration file
if ! grep -q "location /hbnb_static {" /etc/nginx/sites-available/default; then
	# Add /hbnb_static vlock if it does not exist
	sed -i "/error_page 404 \/404.html;/a \\\n\tlocation /hbnb_static { \
        	\n\t\talias /data/web_static/current/; \
	        \n\t\tautoindex off; \
        	\n\t}" /etc/nginx/sites-available/default
fi

service nginx restart
