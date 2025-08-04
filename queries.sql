-- Query to list users with high-level access across systems
SELECT u.name, u.department, s.system_name, r.role_name
FROM Users u
JOIN UserRoles ur ON u.user_id = ur.user_id
JOIN Roles r ON ur.role_id = r.role_id
JOIN Systems s ON ur.system_id = s.system_id
WHERE r.access_level = 'High'
ORDER BY u.department, u.name;

-- Query to count high-level users per system
SELECT s.system_name,
       COUNT(DISTINCT ur.user_id) AS high_user_count
FROM Systems s
JOIN UserRoles ur ON s.system_id = ur.system_id
JOIN Roles r ON ur.role_id = r.role_id
WHERE r.access_level = 'High'
GROUP BY s.system_name;

-- Query to count high-level roles per department
SELECT u.department,
       COUNT(*) AS high_role_count
FROM Users u
JOIN UserRoles ur ON u.user_id = ur.user_id
JOIN Roles r ON ur.role_id = r.role_id
WHERE r.access_level = 'High'
GROUP BY u.department
ORDER BY high_role_count DESC;

-- Query to implement row-level security (example using region)
-- Replace 'East' with the region of the logged-in user or use Tableau's USERNAME() function
SELECT u.name, u.department, u.region, s.system_name, r.role_name
FROM Users u
JOIN UserRoles ur ON u.user_id = ur.user_id
JOIN Roles r ON ur.role_id = r.role_id
JOIN Systems s ON ur.system_id = s.system_id
JOIN SecurityMapping sm ON u.user_id = sm.user_id
WHERE r.access_level = 'High' AND sm.allowed_region = 'East';