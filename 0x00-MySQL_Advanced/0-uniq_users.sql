-- We are all unique!
CREATE TABLE users IF NOT EXISTS (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY(id)
);
