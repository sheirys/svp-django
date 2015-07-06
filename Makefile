##! make

all: migrations migrate syncdb

install: pips-install migrations migrate syncdb

migrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

syncdb:
	./manage.py syncdb

pips-install:
	pip install -r requirements.txt

# End Makefile
