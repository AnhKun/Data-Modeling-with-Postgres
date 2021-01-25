# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id serial primary key,
    start_time bigint not null,
    user_id int NOT NULL, 
    level varchar, 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location text, 
    user_agent text
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
    user_id int PRIMARY KEY, 
    first_name varchar, 
    last_name varchar, 
    gender varchar(1), 
    level varchar
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id varchar PRIMARY KEY, 
    title text, 
    artist_id varchar, 
    year int, 
    duration numeric
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar PRIMARY KEY, 
    name varchar, 
    location text, 
    latitude decimal, 
    longitude decimal
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time bigint PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday varchar
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)\
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level) \
VALUES(%s,%s,%s,%s,%s)
on conflict(user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration) \
VALUES(%s,%s,%s,%s,%s)
on conflict(song_id) do nothing
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude, longitude) \
VALUES(%s,%s,%s,%s,%s)
on conflict(artist_id) do nothing
""")


time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday) \
VALUES(%s,%s,%s,%s,%s,%s,%s)
on conflict(start_time) do nothing
""")

# FIND SONGS

song_select = ("""
SELECT song_id, a.artist_id 
FROM songs s join artists a
    on s.artist_id = a.artist_id 
WHERE title = %s and name = %s and duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]