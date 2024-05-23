# Project Overview
This project involves writing SQL queries to manage a MySQL database, focusing on creating users, managing privileges, and performing various data manipulation tasks.

## Technologies
- Ubuntu 20.04 LTS
- MySQL 8.0

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase
- A README.md file, at the root of the project folder, is mandatory

### Directory Structure
```
0x0E-SQL_more_queries/
|-- 0-privileges.sql
|-- 1-create_user.sql
|-- 2-create_read_user.sql
|-- 3-force_name.sql
|-- 4-never_empty.sql
|-- 5-unique_id.sql
|-- 6-states.sql
|-- 7-cities.sql
|-- 8-cities_of_california_subquery.sql
|-- 9-cities_by_state_join.sql
|-- 10-genre_id_by_show.sql
|-- 11-genre_id_all_shows.sql
|-- 12-no_genre.sql
|-- 13-count_shows_by_genre.sql
|-- 14-my_genres.sql
|-- 15-comedy_only.sql
|-- 16-shows_by_genre.sql
|-- 17-not_my_genre.sql
|-- README.md
```

### Tasks

| Task Number | File Name                        | Description                                                  |
|-------------|----------------------------------|--------------------------------------------------------------|
| 0           | 0-privileges.sql                 | Lists all privileges of specified MySQL users                |
| 1           | 1-create_user.sql                | Creates a MySQL server user with all privileges              |
| 2           | 2-create_read_user.sql           | Creates a database and a user with SELECT privilege          |
| 3           | 3-force_name.sql                | Creates a table with a non-null name field                   |
| 4           | 4-never_empty.sql               | Creates a table with a non-null ID field                     |
| 5           | 5-unique_id.sql                 | Creates a table with a unique ID field                       |
| 6           | 6-states.sql                    | Creates a database and a table for states                   |
| 7           | 7-cities.sql                    | Creates a table for cities with a foreign key to states      |
| 8           | 8-cities_of_california_subquery.sql | Lists cities in California without using JOIN          |
| 9           | 9-cities_by_state_join.sql      | Lists all cities with their corresponding states             |
| 10          | 10-genre_id_by_show.sql         | Lists shows with at least one genre linked                   |
| 11          | 11-genre_id_all_shows.sql       | Lists all shows and their genres                             |
| 12          | 12-no_genre.sql                 | Lists shows without a genre linked                           |
| 13          | 13-count_shows_by_genre.sql     | Lists genres with the number of shows linked to each          |
| 14          | 14-my_genres.sql                | Lists genres of the show "Dexter"                            |
| 15          | 15-comedy_only.sql              | Lists all comedy shows                                        |
| 16          | 16-shows_by_genre.sql           | Lists all shows and their linked genres                      |
| 17          | 17-not_my_genre.sql             | Lists genres not linked to the show "Dexter"                 |

## Author :black_nib:
* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
