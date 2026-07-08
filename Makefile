SHELL := /bin/bash

compile:
	# pushd to the cookbook and compile it
	cd vue-src/totk-cookbook && npm run build

	# move it to the place we want
	rm -rf public/totk-cookbook/*
	mkdir -p public/totk-cookbook
	cp -r vue-src/totk-cookbook/dist/* public/totk-cookbook/

run:
	firebase emulators:start

map:
	./bin/mapGen.py > public/sitemap.html

deploy: map

	# npm build
	firebase deploy
