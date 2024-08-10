#!/bin/bash

REPO_DIR="/var/www/html"
GITHUB_REPO="https://github.com/devopsaziz/htmlassignment.git"

# Pull the latest changes from GitHub
cd $REPO_DIR
sudo git pull $GITHUB_REPO

# Restart Nginx
sudo systemctl restart nginx

