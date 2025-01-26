--   CREATE TABLE Games (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                          user_id INTEGER NOT NULL,
--                          date TEXT NOT NULL,
--                          score INTEGER,
--                          game TEXT NOT NULL,
--                          review TEXT NOT NULL,
--                          review_title TEXT NOT NULL,
--                          reviewer_name TEXT NOT NULL);


--   CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                       username TEXT NOT NULL,
--                       password TEXT NOT NULL);
--  INSERT INTO Users (username, password) VALUES
--                         ('adminUser', 'adminPassword'),
--                         ('test1User', 'test1Pass');
-- INSERT INTO Games (user_id, date, score, game, review, review_title, reviewer_name) VALUES
--                         (1, '2021-01-01', 10, 'Game1', 'This is a review of Game1', 'Game1 Review', 'adminUser'),
--                         (1, '2021-01-02', 9, 'Game2', 'This is a review of Game2', 'Game2 Review', 'adminUser'),
--                         (1, '2021-01-03', 8, 'Game3', 'This is a review of Game3', 'Game3 Review', 'adminUser'),
--                         (1, '2021-01-04', 7, 'Game4', 'This is a review of Game4', 'Game4 Review', 'adminUser'),
--                         (1, '2021-01-05', 6, 'Game5', 'This is a review of Game5', 'Game5 Review', 'adminUser'),
--                         (1, '2021-01-06', 5, 'Game6', 'This is a review of Game6', 'Game6 Review', 'adminUser'),
--                         (1, '2021-01-07', 4, 'Game7', 'This is a review of Game7', 'Game7 Review', 'adminUser'),
--                         (1, '2021-01-08', 3, 'Game8', 'This is a review of Game8', 'Game8 Review', 'adminUser'),
--                         (1, '2021-01-09', 2, 'Game9', 'This is a review of Game9', 'Game9 Review', 'adminUser'),
--                         (1, '2021-01-10', 1, 'Game10', 'This is a review of Game10', 'Game10 Review', 'adminUser'),
--                         (2, '2021-01-01', 10, 'Game1', 'This is a review of Game1', 'Game1 Review', 'test1User'),
--                         (2, '2021-01-02', 9, 'Game2', 'This is a review of Game2', 'Game2 Review', 'test1User'),
--                         (2, '2021-01-03', 8, 'Game3', 'This is a review of Game3', 'Game3 Review', 'test1User'),
--                         (2, '2021-01-04', 7, 'Game4', 'This is a review of Game4', 'Game4 Review', 'test1User'),
--                         (2, '2021-01-05', 6, 'Game5', 'This is a review of Game5', 'Game5 Review', 'test1User'),
--                         (2, '2021-01-06', 5, 'Game6', 'This is a review of Game6', 'Game6 Review', 'test1User'),
--                         (2, '2021-01-07', 4, 'Game7', 'This is a review of Game7', 'Game7 Review', 'test1User'),
--                         (2, '2021-01-08', 3, 'Game8', 'This is a review of Game8', 'Game8 Review', 'test1User'),
--                         (2, '2021-01-09', 2, 'Game9', 'This is a review of Game9', 'Game9 Review', 'test1User'),
--                         (2, '2021-01-10', 1, 'Game10', 'This is a review of Game10', 'Game10 Review', 'test1User'); 

INSERT INTO Games (user_id, date, score, game, review, review_title, reviewer_name) VALUES
                  (1, '2021-01-01', 5, 'Game1', 'This is a review of Game1', 'Game1 Review', 'test1user');
