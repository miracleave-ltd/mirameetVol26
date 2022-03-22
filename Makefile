migrate-run:
	python manage.py makemigrations product && python manage.py migrate && python manage.py runserver 0.0.0.0:7000
batch:
	python manage.py product_data
incron-set:
	echo "root" > /etc/incron.allow
	incrontab -l | { cat; echo '/meetup/csv/ IN_MOVED_TO /bin/sh /meetup/sh/product.sh >& /meetup/logs/batch.log'; } | incrontab -
