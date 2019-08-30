SHELL := /bin/bash

compile:
	# pushd to the blag and compile it
	cd blag && npm run build

	# move it to the place we want
	rm -rf public/blag/*
	cp -r blag/{dist,res} public/blag/
	cp blag/index.html public/blag/
	cp blag/res/page_images/* public/res/page_images/

map:
	./bin/mapGen.py > public/sitemap.html

deploy: compile map

	# npm build
	firebase deploy
