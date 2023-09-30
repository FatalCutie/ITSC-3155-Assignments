
CREATE TABLE sandwiches (
sandwich_size varchar(50),
price decimal(5,2)
);

CREATE TABLE Resources (
item varchar(50),
amount int(5)
);

CREATE TABLE recipes (
sandwich_size varchar(50),
item varchar(50),
amount int(5)
);

INSERT INTO sandwiches (sandwich_size, price) VALUES
('small', 1.75),
('medium', 3.25),
('large', 5.5);

INSERT INTO Resources (item, amount) VALUES
('bread', 12),
('ham', 18),
('cheese', 24);

INSERT INTO recipes (sandwich_size, item, amount) VALUES
('Small', 'bread', 2),
('Small', 'ham', 4),
('Small', 'cheese', 4),
('medium', 'bread', 4),
('medium', 'ham', 6),
('medium', 'cheese', 8),
('large', 'bread', 6),
('large', 'ham', 8),
('large', 'cheese', 12);

SELECT * FROM recipes;
SELECT * FROM Resources;
SELECT * FROM sandwiches;