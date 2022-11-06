setup: requirements.txt
	pip install -r requirements.txt

start-database:
	docker build -t postgres-db ./postgres/
	docker run -d --name postgres-db -p 5432:5432 postgres-db

end-database:
	docker container stop $(shell docker ps -aq)
	docker container rm $(shell docker ps -aq)
run: 
	python3 application/main.py