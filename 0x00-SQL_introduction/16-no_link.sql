-- lists all records that don't have name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
