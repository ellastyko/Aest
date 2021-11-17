reqs:
	pip install -r requirements.txt

cli: 
ifeq ($(OS),Windows_NT) 
	python ./client/client.py
else
	python3.9 ./client/client.py
endif
	

ser: 
ifeq ($(OS),Windows_NT) 
	python ./server/server.py
else
	python ./server/server.py
endif
	
	
