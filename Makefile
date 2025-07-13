make install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

make format:
	black hello.py

make lint:
	pylint hello.py

make test:
	python -m pytest -vv --cov=hello test_hello.py