deploy:
	./bin/mapGen.py > public/sitemap.html
	# npm build
	firebase deploy