-select rows from table-

SELECT * FROM mytable


-update table-

UPDATE mytable
SET category = "Coke" 
WHERE meal_id = 2215;

-delete from table-

DELETE FROM mytable
WHERE meal_id = 1571;

-insert in table-
INSERT into mytable values(1901, "Momos", "Chinese")

-drop table-
DROP table mytable;

-sort table-
SELECT *FROM mytable
ORDER BY cuisine ASC;
