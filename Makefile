install:
    #install commands
    pip install --upgrade pip &&\
        pip install -r requirements.txt
format:
    #format code
test:
    #test
deploy:
    #deploy
all: install lint deploy test