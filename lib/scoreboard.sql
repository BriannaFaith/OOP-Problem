CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    chickenwings INTEGER DEFAULT 0,
    hamburgers INTEGER DEFAULT 0,
    hotdogs INTEGER DEFAULT 0
);

INSERT INTO participants (name, chickenwings, hamburgers, hotdogs) VALUES
    ('Habanero Hillary', 5, 17, 11),
    ('Big Bob', 20, 4, 11);
