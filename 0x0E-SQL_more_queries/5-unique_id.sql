-- This script creates a table named 'unique_id' with 'id' and 'name' fields
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);
