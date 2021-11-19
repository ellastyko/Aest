reqs:
	pip3 install -r requirements.txt

all: ser cli

cl: 
ifeq ($(OS),Windows_NT) 
	python ./client/client.py
else
	python3.9 ./client/client.py
endif
	

srv: 
ifeq ($(OS),Windows_NT) 
	python ./server/server.py
else
	python3.9 ./server/server.py
endif
	
	
