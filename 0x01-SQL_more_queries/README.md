# 0x01. SQL - More Queries

## Description
This project dives deeper into SQL by introducing more advanced queries and database operations. Topics include user management, constraints, joins, subqueries, and aggregation functions. These SQL scripts are designed to strengthen your understanding of relational databases and help build proficiency in writing effective and efficient SQL code.

## Learning Objectives
By completing this project, you will:
- Understand and apply user privileges in SQL.
- Create and manage users and their permissions.
- Use constraints like `NOT NULL`, `UNIQUE`, and `DEFAULT`.
- Work with joins and subqueries to combine and filter data.
- Perform queries involving aggregation and filtering.

## Project Files
Each file in this project is an SQL script that performs a specific database task.

| File | Description |
|------|-------------|
| `0-privileges.sql` | Lists all privileges of the MySQL users |
| `1-create_user.sql` | Creates a new MySQL user |
| `2-create_read_user.sql` | Creates a user with read-only access to a database |
| `3-force_name.sql` | Creates a table with a `name` field that cannot be null |
| `4-never_empty.sql` | Creates a table where a field has a default value if not provided |
| `5-unique_id.sql` | Creates a table with a unique constraint on an ID field |
| `6-states.sql` | Creates a `states` table with `id` and `name` |
| `7-cities.sql` | Creates a `cities` table linked to `states` by foreign key |
| `8-cities_of_california_subquery.sql` | Lists all cities of California using a subquery |
| `9-cities_by_state_join.sql` | Lists all cities by state using a `JOIN` |
| `10-genre_id_by_show.sql` | Lists show titles and their genre IDs |
| `11-genre_id_all_shows.sql` | Lists all shows and their genre IDs, including those without genre |
| `12-no_genre.sql` | Lists all shows with no genre linked |
| `13-count_shows_by_genre.sql` | Counts the number of shows linked to each genre |
| `14-my_genres.sql` | Lists genres liked by a specific user based on show history |
| `15-comedy.only.sql` | Lists all comedy shows only |
| `16-shows_by_genre.sql` | Lists all shows by genre, sorted by genre and title |

## Usage
To execute a SQL script, use the following command:
```sh
mysql -u <username> -p < database_name < script_name.sql
```
Example:
```sh
mysql -u root -p < hbtn_0d_tvshows < 16-shows_by_genre.sql
```

## Author
Logan McClain
