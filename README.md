![alt text](https://sigarra.up.pt/feup/pt/imagens/LogotipoSI)
# Database Project (FCED Project 2022)

This project was made by Bárbara Zanetti, Diogo Cruz and Rendson Fernandes

Job division:

Files:
- At the UML.png we divided the dataset to have the less amount of repeated informationas possible. Due to the amount of repeated data, we dicided to create sequential keys to almost every table (only excpetions are runner_teams and ranking_event). 
- We also created a RelationalModel.txt, that, as the nome says, it is found our relational model.
- In the races.sql we create the tables, set the types of each field and created the foreing and primary keys.
- We buil the load_races.py to load the information in the tables. In this file we also analyse some inconsistences, divide the dataset (creating dataframes to each table) and populate the data (after cleaning the tables in case that has some residual information).
- We created a question.sql to answer some questions regarding the dataset.


## Repository
[Github](https://github.com/Rendson-Fernandes/fced-project-database)
