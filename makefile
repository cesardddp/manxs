SHELL := /bin/bash

gera:
	# poetry shell;\
	source ./.venv/bin/activate;\
	# cd src;\
	python freeze.py

push:
	rm -rf deploy/*;\
	mv build/* deploy/;\
	cp README.md deploy/;\
	cd deploy/;\
	git add .;git commit -m "autoupload";\
	git push;
	
flask:
	# source ../.venv/bin/activate;\
	python -m poetry shell;\
	# cd src;\
	export FLASK_APP=app.py;\
	export FLASK_ENV=development;\
	flask run -p 5001

teste:
	cd src/build;python -m http.server

purge:
	purgecss --css ./static/css/*.css\
	--content build/*/*.html\
	--out ./purged
