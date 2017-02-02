inplace:
	python3 setup.py build_ext -i

test: inplace
	nosetests

clean:
	@rm -fr build dist
	@rm -fr hdmedians/*.so
