inplace:
	python3 setup.py build_ext -i

test: inplace
	nosetests

clean:
	@rm -fr build dist
	@rm -fr hdmedians/*.so
	@rm -fr hdmedians/*.c

doc: README_.md
	python3 -m readme2tex --output README.md --svgdir docs --project hdmedians README_.md --rerender --bustcache

dist:
	python3 setup.py register sdist upload
