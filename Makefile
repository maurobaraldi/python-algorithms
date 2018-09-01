clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*.orig' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;
	find . -depth -name '__pycache__' -exec rm -rf {} \;

test: clean
	pytest -v tests/$(categ)/$(sub)
