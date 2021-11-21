reqs:
ifeq ($(OS),Windows_NT) 
	pip install -r requirements.txt
else
	python3.9 -m pip install -r requirements.txt
endif
	