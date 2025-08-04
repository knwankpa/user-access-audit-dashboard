-- SQL script to create the user access auditing schema

CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    region TEXT
);

CREATE TABLE Systems (
    system_id INTEGER PRIMARY KEY,
    system_name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE Roles (
    role_id INTEGER PRIMARY KEY,
    role_name TEXT NOT NULL,
    access_level TEXT NOT NULL
);

-- Junction table linking users, roles and systems
CREATE TABLE UserRoles (
    user_id INTEGER,
    role_id INTEGER,
    system_id INTEGER,
    assigned_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (role_id) REFERENCES Roles(role_id),
    FOREIGN KEY (system_id) REFERENCES Systems(system_id)
);

-- Optional table for implementing row‑level security in Tableau
CREATE TABLE SecurityMapping (
    user_id INTEGER,
    allowed_region TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);