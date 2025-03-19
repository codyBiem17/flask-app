#!/bin/bash
echo "Starting Flask application..."
cd /home/ec2-user/flask-app-deploy
nohup python app.py > app.log 2>&1 &
