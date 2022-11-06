![alt text](https://sigarra.up.pt/feup/pt/imagens/LogotipoSI)
# Database Project (FCED Project 2022)

This project was made by Bárbara Zanetti, Diogo Cruz and Rendson Fernandes

Job division:
We worked togheter almost the entire time, but some parts of the work were done mainly by one of the groups. We divided this due to each member group skills. 
- Barbara Silva: responsible to do the load_races.py
- Diogo Cruz: responsible to create the RelationalModel.txt and the races.sql to create the tables
- Rendson Fernandes: responsible to the User Interface and its queries.

Regarding the UML and the questions, we did it togheter. The first one to better understand the model, since it was the center of the work. And, the second one to optimize the data and the time to build one the query,

![alt text](https://i.ibb.co/f0S8SGx/Captura-de-ecra-2022-11-06-a-s-13-44-30.png)

Files:
- At the UML.png we divided the dataset to have the less amount of repeated informationas possible. Due to the amount of repeated data, we dicided to create sequential keys to almost every table (only excpetions are runner_teams and ranking_event). 
- We also created a RelationalModel.txt, that, as the nome says, it is found our relational model.
- In the races.sql we create the tables, set the types of each field and created the foreing and primary keys.
- We buil the load_races.py to load the information in the tables. In this file we also analyse some inconsistences, divide the dataset (creating dataframes to each table) and populate the data (after cleaning the tables in case that has some residual information). The table was populated in the fcde_barbara_silva.
- We created a question.sql to answer some questions regarding the dataset.
- We also create a folder named races to be the User Interface:
  - To execute the UI you must install docker, Makefile and the requirements.txt.
  - To run the application you can execute the command "make run", it will gide to interface. 
  - Check if the requirements are installed as listed in the requirements folder.
  - And enjoy your experience :)


## Repository
[Github](https://github.com/Rendson-Fernandes/fced-project-database)
