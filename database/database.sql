CREATE DATABASE smart_navigation;
USE smart_navigation;

CREATE TABLE nodes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    type VARCHAR(20),
    x FLOAT,
    y FLOAT,
    floor INT
);

CREATE TABLE edges (
    id INT PRIMARY KEY AUTO_INCREMENT,
    from_node INT,
    to_node INT,
    weight FLOAT,
    FOREIGN KEY (from_node) REFERENCES nodes(id),
    FOREIGN KEY (to_node) REFERENCES nodes(id)
);

CREATE TABLE faculty (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(50),
    status VARCHAR(20)
);

CREATE TABLE rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    node_id INT,
    room_number VARCHAR(20),
    faculty_id INT,
    FOREIGN KEY (node_id) REFERENCES nodes(id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(id)
);

CREATE TABLE route_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    from_node INT,
    to_node INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_node) REFERENCES nodes(id),
    FOREIGN KEY (to_node) REFERENCES nodes(id)
);

USE smart_navigation;

INSERT INTO nodes (name, type, x, y, floor) VALUES
('Main Block', 'entrance', 0, 0, 0),
('Mechanical Block', 'block', 8, 0, 0),
('Canteen', 'room', 4, 4, 0),
('CSE Department', 'department', 2, 8, 1),
('CSE AIML Department', 'department', 6, 8, 1),
('IS Department', 'department', 10, 8, 1),
('AI ML Lab 1', 'lab', 5, 12, 2),
('AI ML Lab 2', 'lab', 7, 12, 2),
('AI ML Lab 3', 'lab', 9, 12, 2),
('2nd Year Classroom', 'classroom', 2, 15, 2),
('3rd Year Classroom', 'classroom', 6, 15, 2),
('4th Year Classroom', 'classroom', 10, 15, 2);

INSERT INTO edges (from_node, to_node, weight) VALUES
(1,2,8),
(1,3,5),
(1,4,8),
(2,6,8),
(3,4,5),
(3,5,5),
(4,5,4),
(5,6,4),
(4,7,4),
(5,8,4),
(6,9,4),
(7,10,3),
(8,11,3),
(9,12,3),
(10,11,4),
(11,12,4);

INSERT INTO faculty (name, department, status) VALUES
('Dr. Pushpalatha', 'AI & ML', 'Available'),
('Mr. Ganaraj', 'AI & ML', 'Busy'),
('Dr. Sadhana Rai', 'Information Science', 'Available');

INSERT INTO rooms (node_id, room_number, faculty_id) VALUES
(1, 'Main Block', NULL),
(2, 'Mechanical Block', NULL),
(3, 'Canteen', NULL),
(4, 'CSE Department', 1),
(5, 'CSE AIML Department', 2),
(6, 'IS Department', 3),
(7, 'AI ML Lab 1', 2),
(8, 'AI ML Lab 2', 2),
(9, 'AI ML Lab 3', 2),
(10, '2nd Year Classroom', NULL),
(11, '3rd Year Classroom', NULL),
(12, '4th Year Classroom', NULL);

SELECT * FROM nodes;
SELECT * FROM edges;
SELECT * FROM faculty;
SELECT * FROM rooms;
SELECT * FROM route_logs;

SELECT * FROM rooms
WHERE room_number = 'AI ML Lab 2';

SELECT node_id
FROM rooms
WHERE room_number = 'AI ML Lab 2';

SELECT * FROM edges;