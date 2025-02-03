-- CREATE TABLE Reviews (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                       user_id INTEGER,
--                       reviewTitle TEXT NOT NULL,
--                       score INTEGER,
--                       gameName TEXT NOT NULL,
--                       reviewDate TEXT NOT NULL,
--                       reviewText TEXT NOT NULL,
--                       username TEXT NOT NULL);

-- CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                     username TEXT NOT NULL,
--                     password TEXT NOT NULL);                

-- INSERT INTO Reviews (user_id, reviewDate, score, gameName, reviewText, reviewTitle, username) VALUES
-- (1, '2021-01-01', 5, 'The Witcher 3', 'This game is amazing!', 'Best game ever', 'user1'),
-- (2, '2021-01-02', 4, 'The Witcher 3', 'This game is amazing!', 'Great game', 'user2'),
-- (3, '2021-01-03', 3, 'The Witcher 3', 'This game is amazing!', 'Good game', 'user3'),
-- (4, '2021-01-04', 2, 'The Witcher 3', 'This game is amazing!', 'Bad game', 'user4'),
-- (5, '2021-01-05', 1, 'The Witcher 3', 'This game is amazing!', 'Worst game ever', 'user5');