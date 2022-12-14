install:
    #install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
    #format code
	black *.py mylib/*.py
lint:
    #flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py
deploy:
    #deploy
build:
	# build container
all: install lint test  deploy