<h1>Project: Data Modeling with Postgres</h1>
<h3>Introduction</h3>
<p>This is a partial project of Udacity Data Engineering Nanodegree. Suppose a startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

</p>
<p>They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

</p>
<h3>Project Description</h3>
<p>In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

</p>
<h3>Song Dataset</h3>
<p>The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID.</p>

#### Fact Table

**Table songplays**

| COLUMN  	| TYPE  	| CONSTRAINT  	|
|---	|---	|---	|	
|   songplay_id	| SERIAL  	|   PRIMARY KEY	| 
|   start_time	|   bigint	|   NOT NULL	| 
|   user_id	|   int	|   NOT NULL	| 
|   level	|   varchar |   	| 
|   song_id	|   varchar	|   	| 
|   artist_id	|   varchar	|   	| 
|   session_id	|   int	|   	| 
|   location	|   text	|   	| 
|   user_agent	|   text	|   	| 

The songplay_id field is the primary key and it is an auto-incremental value.

The query to insert data on this table is:

``songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)\
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""") ``
 
 #### Dimensions Tables

 
 **Table users**
 
 | COLUMN  	| TYPE  	| CONSTRAINT  	|
|---	|---	|---	|	
|   user_id	| int  	|   PRIMARY KEY	| 
|   first_name	|   varchar	|  	| 
|   last_name	|   varchar	|  	| 
|   gender	|   varchar(1) |   	| 
|   level	|   varchar	|   	| 

 **Table songs**
  | COLUMN  	| TYPE  	| CONSTRAINT  	|
|---	|---	|---	|	
|   song_id	| varchar	|   PRIMARY KEY	| 
|   title	|   text	|  	| 
|   artist_id	|   varchar	|  	| 
|   year	|   int |   	| 
|   duration	|   numeric	|   	| 

**Table artists**
| COLUMN  	| TYPE  	| CONSTRAINT  	|
|---	|---	|---	|	
|   artist_id	| varchar	|   PRIMARY KEY	| 
|   location	|   text	|  	| 
|   latitude	|   decimal	|  	| 
|   longitude	|   decimal |   	| 
 
**Table time**
 | COLUMN  	| TYPE  	| CONSTRAINT  	|
|---	|---	|---	|	
|   start_time	| bigint	|   PRIMARY KEY	| 
|   hour	|   int	|  	| 
|   day	|   int	|  	| 
|   week	|   int |   	| 
|   month	|   int	|   	| 
|   year	|   int	|   	| 
|   weekday	|   varchar	|   	| 

The query to insert data on these tables is:

With **Table users**:

``user_table_insert = ("""
 INSERT INTO users(user_id, first_name, last_name, gender, level) \
 VALUES(%s,%s,%s,%s,%s)
 on conflict(user_id) do nothing
 """)``

With **Table songs**:

``song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration) \
VALUES(%s,%s,%s,%s,%s)
""")``

With **Table Artists**:

``artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude, longitude) \
VALUES(%s,%s,%s,%s,%s)
on conflict(artist_id) do nothing
 """)``

With **Table time**:

``time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday) \
VALUES(%s,%s,%s,%s,%s,%s,%s)
on conflict(start_time) do nothing``

## Project process
### Create tables
1. Write ``CREATE`` statements in ``sql_queries.py`` to create each table.
2. Write ``DROP`` statements in ``sql_queries.py`` to drop each table if it exists.
3. Run ``create_tables.py`` to create your database and tables.
4. Run ``test.ipynb`` to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.

### Build ETL process

Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table. Remember to rerun create_tables.py to reset your tables before each time you run this notebook.
 __REMEMBER TO RUN TEST.PY WHENEVER CREATE AND INSERT DATA__
1. Process `song_data`

In this first part, you'll perform ETL on the first dataset, `song_data`, to create the `songs` and `artists` dimensional tables.

Let's perform ETL on a single song file and load a single record into each table to start.
- Use the `get_files` function provided above to get a list of all song JSON files in `data/song_data`
- Select the first song in this list
- Read the song file and view the data

2. Repeatedly extract Data for Songs, Artists tables
3. Process `log_data`

In this part, you'll perform ETL on the second dataset, `log_data`, to create the `time` and `users` dimensional tables, as well as the `songplays` fact table.

Let's perform ETL on a single log file and load a single record into each table.
- Use the `get_files` function provided above to get a list of all log JSON files in `data/log_data`
- Select the first log file in this list
- Read the log file and view the data

4. Again Extract Data for Users, Time, Songplays tables:

- With time tables: we use:

``
df['datetime'] = pd.to_datetime(df['ts'], unit='ms')

``
- With songplays: 
##### Extract Data and Songplays Table
This one is a little more complicated since information from the songs table, artists table, and original log file are all needed for the `songplays` table. Since the log file does not specify an ID for either the song or the artist, you'll need to get the song ID and artist ID by querying the songs and artists tables to find matches based on song title, artist name, and song duration time.
- Implement the `song_select` query in `sql_queries.py` to find the song ID and artist ID based on the title, artist name, and duration of a song.
- Select the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent and set to `songplay_data`

##### Insert Records into Songplays Table
- Implement the `songplay_table_insert` query and run the cell below to insert records for the songplay actions in this log file into the `songplays` table. Remember to run `create_tables.py` before running the cell below to ensure you've created/resetted the `songplays` table in the sparkify database.
### Build ETL pipelines

- Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets. Remember to run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.
- We implement : in insert data of <code>sql_queries.py</code> with:
`` INSERT INTO.... ON CONFLICT(xxx) do nothing``
when receive error `already exist ` the value.

## How to run the project
Below are steps you have to follow to achieve the project's target:
1. Run ``create_tables.py`` to create your database and tables. You run this file to reset your tables before each time you run your ETL scripts.
2. Run ``sql_queries.py``.
3. Run ``test.ipynb`` to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.
4. Run ``etl.ipynb`` to  to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run ``test.ipynb`` to confirm that records were successfully inserted into each table. **Remember to rerun ``create_tables.py`` to reset your tables before each time you run this notebook.**
5. Run ``etl.py`` to process the entire datasets. **Remember to run ``create_tables.py`` before running ``etl.py`` to reset your tables. Run ``test.ipynb`` to confirm your records were successfully inserted into each table.**