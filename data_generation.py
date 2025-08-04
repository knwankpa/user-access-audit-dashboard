"""
Script to generate sample user access data and create summary charts.

This script creates a small dataset of users, systems and roles, assigns high-
level, medium and low privileges randomly, stores the data in an SQLite
database, runs the queries defined in `queries.sql`, and generates bar charts
showing the number of high-level users per system and per department.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from pathlib import Path


def create_data():
    np.random.seed(42)
    users = pd.DataFrame({
        'user_id': range(1, 31),
        'name': [f'User_{i}' for i in range(1, 31)],
        'department': np.random.choice(['Finance', 'HR', 'IT', 'Sales', 'Compliance'], size=30),
        'region': np.random.choice(['North', 'South', 'East', 'West'], size=30)
    })
    systems = pd.DataFrame({
        'system_id': [1, 2, 3],
        'system_name': ['Financial System', 'HR System', 'IT Admin'],
        'description': ['Handles financial transactions', 'HR management system', 'IT administration tools']
    })
    roles = pd.DataFrame({
        'role_id': [1, 2, 3, 4, 5],
        'role_name': ['Administrator', 'Manager', 'Analyst', 'Viewer', 'Auditor'],
        'access_level': ['High', 'High', 'Medium', 'Low', 'High']
    })
    user_roles = pd.DataFrame({
        'user_id': np.random.choice(users['user_id'], size=100),
        'role_id': np.random.choice(roles['role_id'], size=100),
        'system_id': np.random.choice(systems['system_id'], size=100),
        'assigned_date': pd.to_datetime(np.random.choice(pd.date_range('2024-01-01', '2024-12-31'), size=100))
    })
    return users, systems, roles, user_roles


def create_database(users: pd.DataFrame, systems: pd.DataFrame, roles: pd.DataFrame, user_roles: pd.DataFrame):
    conn = sqlite3.connect(':memory:')
    users.to_sql('Users', conn, index=False, if_exists='replace')
    systems.to_sql('Systems', conn, index=False, if_exists='replace')
    roles.to_sql('Roles', conn, index=False, if_exists='replace')
    user_roles.to_sql('UserRoles', conn, index=False, if_exists='replace')
    return conn


def run_queries(conn: sqlite3.Connection):
    q1 = """
    SELECT s.system_name, COUNT(DISTINCT ur.user_id) AS high_user_count
    FROM Systems s
    JOIN UserRoles ur ON s.system_id = ur.system_id
    JOIN Roles r ON ur.role_id = r.role_id
    WHERE r.access_level = 'High'
    GROUP BY s.system_name;
    """
    q2 = """
    SELECT u.department, COUNT(*) AS high_role_count
    FROM Users u
    JOIN UserRoles ur ON u.user_id = ur.user_id
    JOIN Roles r ON ur.role_id = r.role_id
    WHERE r.access_level = 'High'
    GROUP BY u.department
    ORDER BY high_role_count DESC;
    """
    high_users_per_system = pd.read_sql(q1, conn)
    dept_high_counts = pd.read_sql(q2, conn)
    return high_users_per_system, dept_high_counts


def generate_charts(high_users_per_system: pd.DataFrame, dept_high_counts: pd.DataFrame, output_dir: str):
    sns.set(style="whitegrid")
    # Chart 1: High-level users per system
    plt.figure(figsize=(8, 5))
    sns.barplot(x='system_name', y='high_user_count', data=high_users_per_system, palette='viridis')
    plt.title('High-Level Users per System')
    plt.xlabel('System')
    plt.ylabel('Number of High-Level Users')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(Path(output_dir) / 'high_users_per_system.png')
    plt.close()
    # Chart 2: High-level users per department
    plt.figure(figsize=(8, 5))
    sns.barplot(x='department', y='high_role_count', data=dept_high_counts, palette='magma')
    plt.title('High-Level Users per Department')
    plt.xlabel('Department')
    plt.ylabel('Count of High-Level Roles')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(Path(output_dir) / 'dept_high_counts.png')
    plt.close()


if __name__ == '__main__':
    users, systems, roles, user_roles = create_data()
    conn = create_database(users, systems, roles, user_roles)
    h_users, d_counts = run_queries(conn)
    output_dir = Path('.')
    generate_charts(h_users, d_counts, output_dir)
    print(h_users)
    print(d_counts)