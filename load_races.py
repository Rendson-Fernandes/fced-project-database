import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import psycopg2
import psycopg2.extras as extras

# Reading the Dataset
df = pd.read_csv("~/Downloads/all_races.csv",sep=",", low_memory=False)

# Preprossesing and Cleaning the data
#identify on the line 146929 an header duplicate in the middle of the dataset
df = df.drop(axis=0, labels=146929)
print(df.describe())

#counting duplicated
print('# of duplicates:',len(df)-len(df.drop_duplicates()))
print('size of df:',len(df))

#removing the duplicates
df = df.drop_duplicates()
#writing file without duplicates
df.to_csv('~/Downloads/all_races_no_duplicates.csv', index=False)
#Checking the types of the colunms
print(df.dtypes)

#checking the nulls in the df
sns.heatmap(df.isnull(),cbar=False,cmap='rocket',yticklabels=False)
plt.title('Missing values on the split dataset');

#treating the nulls in the net time. When net time is null, net_time = official_time
df.loc[df['net_time'].isnull(), 'net_time'] = df[df['net_time'].isnull()]['official_time']

#treating the nulls in the team. When net team is null, team= Individual
df.loc[df['team'].isnull(), 'team'] = 'Individual'

#Converting columns type
df['birth_date'] = pd.to_datetime(df['birth_date'])
df['net_time'] = pd.to_timedelta(df['net_time'])
df['official_time'] = pd.to_timedelta(df['official_time'])
df['event_year'] = pd.to_numeric(df['event_year'])

## Searching for irregularities
#In this section we will search for irregularities in the dataset such as:
#- Men that runned in a female run;
#- Women that runned in a masculine run;
#- People that were above the legal age

#To perform that we searched that for instance, if a age class is M50, that means tha are running only men in the 50ths.

#creating new columns to perform the check
df['class_gender']=df['age_class'].astype(str).str[0]
df['class_age']=df['age_class'].str[-2:]
df['age']= df['event_year'] - pd.DatetimeIndex(df['birth_date']).year

#removing man that run in a fem. class
df = df.drop(index=df[(df['sex']=='M') & (df['class_gender']=='F')].index)
#removing women that runned in a masc. class
df = df.drop(index=df[(df['sex']=='F') & (df['class_gender']=='M')].index)
#removing people ith no legal age to run more than 10km (less than 14 yo), this will also remove inconsistance like (born in the year of the event)
df = df.drop(index=df[df['age']<14].index)

# Spliting our dataset
#For each database we have, we will split in different dataset.
# This will help to select the data correctly, and allow the code to me more organized.
# We previously created the databases that did not have any foreing key,
# than, we merged then to the main df to split their foreing keys to the other tables.
#We need to assure that our merges does not duplicate the main table,
# creating more records than previous stated.
# So, we decided to perform a lef join with the left table being always (in this case) the main df.

# Team: team name, team id.
df_team = pd.DataFrame([])
df_team['team'] = df['team'].unique()
df_team.insert(0, 'id_team', range(0, 0 + len(df_team)))

# Athlete: id, name, sex, nation, birth_date
df_athlete = df[['name', 'sex','nation','birth_date']].drop_duplicates()
df_athlete.insert(0, 'id_athlete', range(0, 0 + len(df_athlete)))

# Events: event_id, event, event_year, distance
df_events = df[['event', 'event_year', 'distance']].drop_duplicates()
df_events.insert(0, 'id_event', range(0, 0 + len(df_events)))

# populate id_athlete on df
df = pd.merge(df,df_athlete[['name','birth_date','sex','nation','id_athlete']], how='left', on=['name','birth_date','sex','nation'])

#populate id_team on df
df = pd.merge(df,df_team[['team','id_team']], how='left', on=['team'])

#populate id_event on df
df = pd.merge(df,df_events[['event','event_year', 'distance','id_event']], how='left', on=['event', 'event_year', 'distance'])

# Runner: id_runner, bib, age_class, id_event, id_athlete
df_runner = df[['bib','age_class','id_athlete','id_event']].drop_duplicates()
df_runner.insert(0, 'id_runner', range(0, 0 + len(df_runner)))

# populate runner_id
df = pd.merge(df,df_runner[['bib','age_class','id_athlete','id_event','id_runner']], how='left', on=['bib','age_class','id_athlete','id_event'])

df_runner_team = df[['id_team','id_runner']].drop_duplicates()
df_runner_team['id_team'] = df_runner_team['id_team'].astype(str)
df_runner_team['id_runner'] = df_runner_team['id_runner'].astype(str)
df_runner_team.dtypes

# Event_ranking: id_event, id_runner, place, place_in_class, official_time, net_time
df_ranking = df[['place','place_in_class', 'official_time', 'net_time','id_runner','id_event']].drop_duplicates()

# Overview of Data
#a histogram of the participants' age.
df['age'].hist(range=[10,80])

#connecting with Postgrees
con = psycopg2.connect(
  database="fced_barbara_silva",             # your database is the same as your username
  user="fced_barbara_silva",                 # your username
  password="teste123",              # your password
  host="dbm.fe.up.pt",                    # the database host
  options='-c search_path=public',
  port="5433"                            # use the schema you want to connect to
)

#cleaning all databases
cursor = con.cursor()
cursor.execute("TRUNCATE events CASCADE")
print("Table event dropped... ")
cursor.execute("TRUNCATE runner CASCADE")
print("Table runner dropped... ")
cursor.execute("TRUNCATE athlete CASCADE")
print("Table athlete dropped... ")
cursor.execute("TRUNCATE teams CASCADE")
print("Table teams dropped... ")
cursor.execute("TRUNCATE runner_teams CASCADE")
print("Table runner_teams dropped... ")
cursor.execute("TRUNCATE event_ranking CASCADE")
print("Table event_ranking dropped... ")
con.commit()

#Populating all tables
#event
cur = con.cursor()
table="events"
cols = ','.join(list(df_events.columns))
query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
tuples = [tuple(x) for x in df_events.to_numpy()]

try:
    extras.execute_values(cur, query, tuples)
    con.commit()
    print("the dataframe is inserted")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    con.rollback()
    cur.close()
cur.close()

#athlete
cur = con.cursor()
table="athlete"
cols = ','.join(list(df_athlete.columns))
query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
tuples = [tuple(x) for x in df_athlete.to_numpy()]

try:

    extras.execute_values(cur, query, tuples)
    con.commit()
    print("the dataframe is inserted")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    con.rollback()
    cur.close()
cur.close()

#team
cur = con.cursor()
table="teams"
cols = ','.join(list(df_team.columns))
query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
tuples = [tuple(x) for x in df_team.to_numpy()]

try:

    extras.execute_values(cur, query, tuples)
    con.commit()
    print("the dataframe is inserted")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    con.rollback()
    cur.close()
cur.close()

#runner
cur = con.cursor()
table="runner"
cols = ','.join(list(df_runner.columns))
query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
tuples = [tuple(x) for x in df_runner.to_numpy()]

try:
    extras.execute_values(cur, query, tuples)
    con.commit()
    print("the dataframe is inserted")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    con.rollback()
    cur.close()
cur.close()

#runner_team
cur = con.cursor()
table="runner_teams"
cols = ','.join(list(df_runner_team.columns))
query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
tuples = [tuple(x) for x in df_runner_team.to_numpy()]

try:
    extras.execute_values(cur, query, tuples)
    con.commit()
    print("the dataframe is inserted")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    con.rollback()
    cur.close()
cur.close()

#event_ranking
cur = con.cursor()
table="event_ranking"
cols = ','.join(list(df_ranking.columns))
query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
tuples = [tuple(x) for x in df_ranking.to_numpy()]

try:
    extras.execute_values(cur, query, tuples)
    con.commit()
    print("the dataframe is inserted")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    con.rollback()
    cur.close()
cur.close()