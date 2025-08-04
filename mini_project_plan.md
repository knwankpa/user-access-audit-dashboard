# Mini SQL–Tableau Project for Portfolio

This mini project is designed around the work you already do – using SQL to audit user access in an Oracle database and visualising the results in Tableau.  The project will show that you can design a dataset, write SQL to answer security questions, and build dashboards that make access reviews efficient and transparent.  It combines database modelling, SQL querying and Tableau visualisation, reflecting best practices for building portfolio projects and emphasising industry relevance【364304039507579†L56-L74】.

## 1. Project scenario

Imagine you have been asked to assess user access across several internal systems.  The objective is to identify users with high‑level privileges, see which departments hold the most high‑level permissions and present the results in an interactive dashboard.  For privacy and compliance reasons, you will also explore Row‑Level Security (RLS) in Tableau so that auditors only see data relevant to their region or department【533720745108507†L34-L63】.

## 2. Design a sample database

Create a small relational database (e.g., in **SQLite** or **PostgreSQL**; both are free and easy to use).  Use the following tables:

| Table | Key columns | Purpose |
|---|---|---|
| **Users** | `user_id` (PK), `name`, `department`, `region` | Basic user information (department and region will later be used for RLS). |
| **Systems** | `system_id` (PK), `system_name`, `description` | Systems or applications users can access. |
| **Roles** | `role_id` (PK), `role_name`, `access_level` | Defines privilege levels, e.g., High, Medium, Low.  Use `access_level` to filter for high‑level access. |
| **UserRoles** | `user_id`, `role_id`, `system_id`, `assigned_date` | Many‑to‑many relationship linking users to roles and systems.  Use this table to see who has which role on each system. |
| **SecurityMapping** *(optional)* | `user_id`, `allowed_region` | Used to implement row‑level security by mapping each auditor to the region(s) they are allowed to see【533720745108507†L69-L99】. |

Populate the tables with fictional data for ~25–50 users across departments like *Finance*, *HR*, *IT*, *Sales* and *Compliance*.  Assign a mix of `High`, `Medium` and `Low` access roles across systems such as *Financial System*, *HR System* and *IT Admin*.  You can write a SQL script or use Python to generate the data.

> **Tip:** Dataquest suggests choosing projects that align with your interests and that demonstrate a breadth of skills such as data cleaning, complex joins and reporting【364304039507579†L56-L74】.  Designing this schema yourself showcases data modelling and ensures the dataset contains the elements you need【480319488411087†L10-L19】.

## 3. Write SQL queries

Develop SQL queries that answer typical audit questions.  Some examples:

1. **Identify users with high‑level access.**  Join `Users`, `UserRoles` and `Roles` where `access_level = 'High'`.  Return user name, department, system and role.

   ```sql
   SELECT u.name, u.department, s.system_name, r.role_name
   FROM Users u
   JOIN UserRoles ur ON u.user_id = ur.user_id
   JOIN Roles r ON ur.role_id = r.role_id
   JOIN Systems s ON ur.system_id = s.system_id
   WHERE r.access_level = 'High'
   ORDER BY u.department, u.name;
   ```

2. **Count high‑level users per system.**  Group by system name and count unique users with high‑level roles.

   ```sql
   SELECT s.system_name,
          COUNT(DISTINCT ur.user_id) AS high_user_count
   FROM Systems s
   JOIN UserRoles ur ON s.system_id = ur.system_id
   JOIN Roles r ON ur.role_id = r.role_id
   WHERE r.access_level = 'High'
   GROUP BY s.system_name;
   ```

3. **Departmental distribution of high‑level access.**  Determine which departments have the most high‑level privileges.

   ```sql
   SELECT u.department,
          COUNT(*) AS high_role_count
   FROM Users u
   JOIN UserRoles ur ON u.user_id = ur.user_id
   JOIN Roles r ON ur.role_id = r.role_id
   WHERE r.access_level = 'High'
   GROUP BY u.department
   ORDER BY high_role_count DESC;
   ```

4. **Implement Row‑Level Security (optional).**  To restrict what each auditor sees, join the `Users` table with `SecurityMapping` and filter on matching regions using dynamic functions (Tableau’s `USERNAME()` function can retrieve the logged‑in user)【533720745108507†L34-L63】.

These queries demonstrate ability to join multiple tables, filter and aggregate data – core SQL skills emphasised in many portfolio guides【364304039507579†L56-L74】.

## 4. Build a Tableau dashboard

Use the SQL results as your data source in Tableau (e.g., by connecting Tableau directly to the database or by exporting results to a CSV).  Create a dashboard with the following components:

* **Summary bar chart** – Show the number of high‑level users per system.  This lets auditors quickly spot which system has the most privileged users.
* **Departmental distribution** – Use a pie chart or stacked bar to visualise how high‑level privileges are spread across departments.
* **Detailed table** – List individual users with high‑level roles, with filters for system, department and access level.
* **Row‑Level Security filter (optional)** – Implement RLS so that when a user logs into Tableau Server/Cloud, they only see data for their region or department【533720745108507†L34-L63】.  This can be done using a dynamic calculated field referencing `USERNAME()` and the `SecurityMapping` table【533720745108507†L69-L99】.

Design your dashboard with interactivity (filters and highlights) so that security and audit teams can drill down to specific systems or departments quickly.  Document your design decisions and explain how the dashboard improves the review process.

## 5. Document and share the project

1. **Repository setup.**  Create a public repository (e.g., on GitHub) containing:
   - The SQL script to create and populate the database.
   - Query scripts used to generate the audit data.
   - The Tableau workbook or exported `.twb/.twbx` file.
   - A README file explaining the project objectives, data model, SQL queries and dashboard features.

2. **Write a blog or portfolio post.**  Summarise the project scenario, your design decisions, key insights and screenshots of the dashboard.  Explain how this project reflects your real‑world experience with access reviews and compliance.

3. **Highlight skills.**  In your portfolio, emphasise that the project demonstrates:
   - **Database design and normalisation** (creating tables and relationships).
   - **Complex SQL querying** (joins, filters, aggregations and conditional logic).
   - **Data visualization and storytelling** with Tableau.
   - **Understanding of compliance and security** (through RLS and careful data handling【533720745108507†L34-L63】).

## 6. Extending the project

To make the project more impressive, you could add:

* **Audit log analysis.**  Introduce an `AccessLogs` table (user, system, timestamp, action) and build a dashboard showing login patterns over time, highlighting anomalous activity.
* **Parameterised reporting.**  Use Tableau parameters to let users change the definition of “high‑level” (e.g., include medium‑level roles) and observe how the results change.
* **Automation.**  Use a Python or shell script to refresh the data, run SQL queries and publish the dashboard to Tableau Server automatically.

By following these steps, you’ll have a comprehensive yet manageable project that clearly reflects your day‑to‑day responsibilities and demonstrates your ability to turn data into actionable insights for security and audit teams.
