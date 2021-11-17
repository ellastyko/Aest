reqs:
	pip install -r requirements.txt

client: 
	python3 ./client/client.py

server: 
	python3 ./server/server.py
