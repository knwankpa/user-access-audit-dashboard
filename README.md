## User Access Audit Dashboard

This project demonstrates how to use SQL and data visualization to audit user access across multiple systems.  It simulates a small organisation where employees are assigned roles on different systems, and builds a dashboard highlighting users with high‑level privileges, distribution of access by system and department, and optional row‑level security for auditors.

### Project features

* **Normalised database schema:** A set of SQL tables (`Users`, `Systems`, `Roles`, `UserRoles`, and `SecurityMapping`) models the relationships between people, systems and access levels.
* **Sample data:** Scripts populate the database with 30 fictional users, three systems and five roles.  Random assignments create realistic combinations of high, medium and low access levels.
* **Reusable SQL queries:** Several queries extract insights, such as which users hold high‑level roles, how many privileged users exist on each system, and which departments have the most high‑level privileges.
* **Visualisations:** Example charts show the distribution of privileged users per system and per department.  These charts can be recreated in Tableau or any other visualisation tool.
* **Row‑Level Security (optional):** A `SecurityMapping` table demonstrates how to restrict an auditor’s view to a particular region or department.

### Files

| File | Description |
|------|-------------|
| `create_tables.sql` | SQL commands to create all tables. |
| `insert_data.sql` | Insert statements to populate the tables with sample data. |
| `queries.sql` | Example queries used for the analysis. |
| `high_users_per_system.png` | Bar chart showing the number of high‑level users for each system. |
| `dept_high_counts.png` | Bar chart showing the distribution of high‑level roles by department. |
| `high_user_details.csv` | CSV file listing every user with a high‑level role (name, department, system, role). |
| `data_generation.py` (optional) | Python script that generated the sample data and charts. |

### How to use

1. **Set up the database.** Install a SQL database management system (e.g., SQLite or PostgreSQL).  Create a new database and run `create_tables.sql` to set up the schema.  Then run `insert_data.sql` to load the sample data.
2. **Run the queries.** Use your preferred SQL client to execute the queries in `queries.sql`.  These queries answer questions such as:
   - Which users have high‑level access?  (See query 1.)
   - How many unique users have high‑level access on each system?  (See query 2.)
   - Which departments have the most high‑level privileges?  (See query 3.)
3. **Visualise the results.** Import the SQL results or the provided CSV into Tableau or another visualisation tool.  Recreate the example charts or design your own dashboard with filters for system and department.  Use the `SecurityMapping` table and Tableau’s `USERNAME()` function to implement row‑level security if deploying to Tableau Server.

