SHELL := /bin/bash

build:
	poetry shell;\
	cd src;\
	python freeze.py

push:
	rm -rf deploy/*;\
	mv src/build/* deploy/;\
	cd deploy/;\
	git add .;git commit -m "autoupload";\
	git push;
	
flask:
	# source ../.venv/bin/activate;\
	poetry shell;\
	# cd src;\
	export FLASK_APP=app.py;\
	export FLASK_ENV=development;\
	flask run

teste:
	cd build;python -m http.server