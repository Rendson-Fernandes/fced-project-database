setup: requirements.txt
	pip install -r requirements.txt

start-database:
	docker build -t postgres-db ./postgres/
	docker run -d --name postgres-db -p 5432:5432 postgres-db

end-database:
	docker container stop $(shell docker ps -aq)
	docker container rm $(shell docker ps -aq)
	#docker container stop $(shell docker ps -q --filter ancestor=postgres-db )
	# docker rm $$(docker ps -q --filter ancestor=postgres-db )
