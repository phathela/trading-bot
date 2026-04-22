#!/bin/bash
set -e

PORT=${PORT:-5000}
echo "Starting trading bot on port $PORT..."

exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 120 app:app
