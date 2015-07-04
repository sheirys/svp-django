##! make

all: migrations migrate syncdb

migrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

syncdb:
	./manage.py syncdb

# End Makefile
