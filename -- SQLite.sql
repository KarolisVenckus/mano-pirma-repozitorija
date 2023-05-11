-- SQLite
CREATE TABLE students (
  studento_id INTEGER PRIMARY KEY,
  vardas VARCHAR(50),
  pavardė VARCHAR(50),
  studijų_programa VARCHAR(100),
  el_paštas VARCHAR(50),
  gimimo_data DATE
);

ALTER TABLE studentai ADD COLUMN phone VARCHAR(20);
ALTER TABLE studentai ADD COLUMN address TEXT(200);
DROP TABLE studentai;