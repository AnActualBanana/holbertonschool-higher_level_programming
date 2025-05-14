# 0x0B. Python - Object-relational mapping

This project explores how Python interacts with relational databases (MySQL) using both raw SQL and Object Relational Mapping (ORM) via SQLAlchemy.

---

## 📚 Learning Objectives

- Understand the differences between SQL and ORM.
- How to connect to a MySQL database from a Python script.
- Execute SQL queries in Python using the `MySQLdb` module.
- Use SQLAlchemy to map Python classes to MySQL tables.
- Prevent SQL injection with safe queries.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all states from the database `hbtn_0e_0_usa`. |
| `1-filter_states.py` | Lists all states with names starting with 'N'. |
| `2-my_filter_states.py` | Takes an argument and displays matching state values. |
| `3-my_safe_filter_states.py` | Like task 2 but safe from SQL injection. |
| `4-cities_by_state.py` | Lists all cities grouped by state. |
| `5-filter_cities.py` | Displays cities of a given state using safe SQL. |
| `7-model_state_fetch_all.py` | Lists all `State` objects using SQLAlchemy ORM. |
| `8-model_state_fetch_first.py` | Prints the first `State` object from the database. |
| `9-model_state_filter_a.py` | Lists all `State` objects containing the letter 'a'. |
| `10-model_state_my_get.py` | Prints the `State` object with the given name. |
| `11-model_state_insert.py` | Adds a new `State` to the database via SQLAlchemy. |
| `12-model_state_update_id_2.py` | Updates the name of a `State` with `id=2`. |
| `13-model_state_delete_a.py` | Deletes all `State` objects with 'a' in the name. |
| `14-model_city_fetch_by_state.py` | Lists all `City` objects with their state names. |
| `model_state.py` | SQLAlchemy model for the `states` table. |
| `model_city.py` | SQLAlchemy model for the `cities` table. |
| `0-select_states.sql`, `4-cities_by_state.sql` | SQL scripts for creating and populating test tables. |

---

## 🧪 Usage

All scripts accept MySQL credentials as command-line arguments:

```bash
./0-select_states.py <username> <password> <database_name>
./2-my_filter_states.py <username> <password> <database_name> "Arizona"
```

## Author
Logan McClain
