clean:
	find . -name '*.pyc' -exec rm --force {} \;
	find . -name '*.pyo' -exec rm --force {} \;
	find . -name '*.orig' -exec rm --force {} \;
	find . -name '*~' -exec rm --force {} \;

