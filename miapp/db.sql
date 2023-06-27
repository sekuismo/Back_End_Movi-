CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  password VARCHAR(60),
  email VARCHAR(50) UNIQUE,
  avatar VARCHAR(100),
  country CHAR(2),
  date_added TIMESTAMP
);

CREATE TABLE lista_de_peliculas (
  id SERIAL PRIMARY KEY,
  is_viewed BOOLEAN,
  is_erased BOOLEAN,
  date_added TIMESTAMP,
  user_id INT REFERENCES usuarios(id),
  movie_id INT REFERENCES peliculas(id)
);

CREATE TABLE peliculas (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100),
  description VARCHAR(800),
  year INT,
  language CHAR(2),
  genre_name VARCHAR(20),
  genre_id INT,
  img_url VARCHAR(100),
  url VARCHAR(100)
);
