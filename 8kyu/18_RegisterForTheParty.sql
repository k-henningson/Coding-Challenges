-- You received an invitation to an amazing party. 
-- Now you need to write an insert statement to add yourself to the table of participants.

-- participants table schema

-- name (string)
-- age (integer)
-- attending (boolean)

INSERT into participants (name, age, attending)
VALUES ('Kyra', 36, true);
SELECT * FROM participants;
