
all: py_tests
	echo "to be completed if necessary"

configure:
	pip install -r requirements.txt


py_tests:
	python3 -m unittest discover -v
