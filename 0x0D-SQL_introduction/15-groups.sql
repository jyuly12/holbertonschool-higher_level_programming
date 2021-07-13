-- Lists the number of records with the same score in the table second_table
-- of the database hbtn_0c_0 in your MySQL server.
SELECT score, COUNT(*) as number FROM second_table GROUP by score
ORDER BY number DESC;
