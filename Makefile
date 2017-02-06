
inplace:
	python3 setup.py build_ext -i

test: inplace
	nosetests

clean:
	@rm -fr build dist
	@rm -fr hdmedians/*.so
	@rm -fr hdmedians/*.c

doc: docs/README_.md
	@python3 -m readme2tex --output README.md --svgdir . --project hdmedians --usepackage "stix" --rerender docs/README_.md
# hack to make images work
	@for f in $(wildcard docs/*.svg); do cairosvg -d 300 $$f -o $${f/svg/png}; done
	@sed -i~ -e 's/svg/png/g; s/rawgit/github/g; s/master/raw\\\/master/g' README.md
	@rm -fr *~
	git rm --cached $(wildcard docs/*.svg) $(wildcard docs/*.png)
	git add $(wildcard docs/*.svg) $(wildcard docs/*.png)
	git add README.md docs/README_.md
	git commit -m 'Update README'
	git push

dist:
	python3 setup.py register sdist upload
