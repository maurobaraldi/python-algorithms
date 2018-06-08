clean:
	find . -name '*.pyc' -exec rm --force {} \;
	find . -name '*.pyo' -exec rm --force {} \;
	find . -name '*.orig' -exec rm --force {} \;
	find . -name '*~' -exec rm --force {} \;
	find . -depth -name '__pycache__' -exec rm --force --recursive {} \;

test: clean
	pytest 
