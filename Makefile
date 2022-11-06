setup: requirements.txt
	pip install -r requirements.txt

start-database:
	docker build -t postgres-db ./postgres/
	docker run -d --name my-postgresdb-container -p 5432:5432 postgres-db

end-database:
	docker stop $(docker ps -q --filter ancestor=postgres-db )
