-- Followed https://stackoverflow.com/questions/8645889/there-can-be-only-one-auto-column
-- Images from https://unsplash.com/s/photos/open-source

USE images;

CREATE TABLE IF NOT EXISTS image (
  id INT NOT NULL AUTO_INCREMENT,
  url VARCHAR(255) NOT NULL,
  thumbs_up INT DEFAULT 0,
  thumbs_down INT DEFAULT 0,
  PRIMARY KEY (id)
);

INSERT INTO image (url, thumbs_up, thumbs_down)
VALUES
("https://images.unsplash.com/photo-1523251343397-9225e4cb6319?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 1, 0),
("https://images.unsplash.com/photo-1489389944381-3471b5b30f04?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 0, 1),
("https://plus.unsplash.com/premium_photo-1678566111481-8e275550b700?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8b3BlbiUyMHNvdXJjZXxlbnwwfHwwfHx8MA%3D%3D", 0, 0),
("https://images.unsplash.com/photo-1518717202715-9fa9d099f58a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fG9wZW4lMjBzb3VyY2V8ZW58MHx8MHx8fDA%3D", 0, 1),
("https://images.unsplash.com/photo-1526657782461-9fe13402a841?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fG9wZW4lMjBzb3VyY2V8ZW58MHx8MHx8fDA%3D", 1, 0),
("https://images.unsplash.com/photo-1444454508600-22e585108a04?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fG9wZW4lMjBzb3VyY2V8ZW58MHx8MHx8fDA%3D", 0, 1),
("https://images.unsplash.com/photo-1541569863345-f97c6484a917?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fG9wZW4lMjBzb3VyY2V8ZW58MHx8MHx8fDA%3D", 1, 0),
("https://images.unsplash.com/photo-1486395130845-ec128138002e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjN8fG9wZW4lMjBzb3VyY2V8ZW58MHx8MHx8fDA%3D", 0, 1);

