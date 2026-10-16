#!/bin/bash
echo "--- Đang cập nhật hệ thống Mentiq ---"
cd /var/www/mentiq
source venv/bin/activate
#python manage.py makemessages -l vi -l en
python manage.py compilemessages
python manage.py collectstatic --noinput
sudo pkill gunicorn
gunicorn --bind 127.0.0.1:8000 config.wsgi:application --daemon
sudo systemctl restart nginx
echo "--- Hoàn tất cập nhật thành công! ---"
