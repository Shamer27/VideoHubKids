--  CREATE TABLE Reviews (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                        user_id INTEGER,
--                        user_name TEXT NOT NULL,
--                        game TEXT NOT NULL,
--                        review_title TEXT NOT NULL,
--                        date TEXT NOT NULL,
--                        review_text TEXT NOT NULL,
--                        score INTEGER);


--  CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                      username TEXT NOT NULL,
--                      password TEXT NOT NULL);

INSERT INTO Reviews(user_id, user_name, game, review_title, date, review_text, score)
                        VALUES(1, 'test', 'Elden Balls', 'Great game', '1/2/24', 'This game is great, graphics amazing, UI amazing', 5) 