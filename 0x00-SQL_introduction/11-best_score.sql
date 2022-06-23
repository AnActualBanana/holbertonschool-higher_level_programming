-- lists all records with score higher than 10, descending.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
