CREATE DATABASE IF NOT EXISTS CookingBlog;
USE CookingBlog;

CREATE TABLE IF NOT EXISTS recipes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  ingredients JSON,
  steps JSON,
  cooking_time INT,
  difficulty VARCHAR(50),
  chapter VARCHAR(100),
  image_url TEXT,
  author VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  for_sale BOOLEAN DEFAULT FALSE,
  price DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  bank_name VARCHAR(255),
  card_number VARCHAR(255),
  card_holder_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS deals (
  id INT AUTO_INCREMENT PRIMARY KEY,
  recipes_id INT NOT NULL,
  buyer_id INT NOT NULL,
  author_id INT NOT NULL,
  price DECIMAL(10,2),
  status ENUM('created', 'payment_sent', 'completed', 'canceled', 'disputed') DEFAULT 'created',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (recipes_id) REFERENCES recipes(id),
  FOREIGN KEY (buyer_id) REFERENCES users(id),
  FOREIGN KEY (author_id) REFERENCES users(id)
);

INSERT INTO recipes (title, description, ingredients, steps, cooking_time, difficulty, chapter, image_url, author) VALUES
('Limoncello mojito', 'Refresh a classic mojito with a splash of zesty limoncello. Serve this refreshing drink in tall glasses and garnish with the remaining mint leaves to serve', '["1 lemon","juiced","1 tbsp golden caster sugar","small handful of mint","leaves picked","100ml white rum","100ml limoncello","ice","300ml soda water"]', '["step 1","Put the lemon juice, sugar and half the mint leaves in a cocktail shaker. Bash with a cocktail muddler or the end of a rolling pin until the sugar has dissolved.","step 2","Pour the rum and limoncello into the shaker and add a handful of ice. Cover with the lid and shake until the outside of","the shaker feels cold.","step 3","Fill two tall glasses with ice, then strain in the cocktail and top up with the soda water. Garnish with the remaining mint leaves to serve."]', 10, 'Easy', 'Drinks', 'https://images.immediate.co.uk/production/volatile/sites/30/2023/03/Limoncello-mojito-787046e.jpg?quality=90&webp=true&resize=700,636', 'СA');

INSERT INTO users (username, email, password) VALUES
('PankivRoman', 'pankiv.roma@gmail.com', 'scrypt:32768:8:1$M7R8b35nabH69E9A$534ebfaec73f094b9ac7275872c044bab3365324995ef8cdd224cfda2dfec9db429d4e8e1313b61b7483e6f5472c265ccf7b8a9b0c584b679f968995f4b26303'),
('ivnj', 'pankiv.dfg@gmail.com', 'scrypt:32768:8:1$LouSowhEM5JwYaBx$04396a728b5f1328469b01d16cf2be2d3d2c7fb07bd25c266301706723986403d3a7f20dc66a0e820648ba60b2c4fcaff37e2db56b16a07fa4f713baf1f61a7f'),
('NikitaHor', 'nita@huhi.com', 'scrypt:32768:8:1$LTfD9ABsLsZVfbDQ$8f94b3d4505fb067be776e48022a59f39768cc0fb65f626df317f8afe349d566a82a302513f87b76411cc18993dca09fea7e845bb3aeb07d8dd7978757130024'),
('Jane Doe', 'ddnita@huhi.com', 'scrypt:32768:8:1$LTfD9ABsLsZVfbDQ$8f94b3d4505fb067be776e48022a59f39768cc0fb65f626df317f8afe349d566a82a302513f87b76411cc18993dca09fea7e845bb3aeb07d8dd7978757130024'),
('Criss', 'Criss@gmail.com', 'scrypt:32768:8:1$sRiyFMiuAsgn5yK7$434be94512715e0ebbeba445ae829dcc29794f7c2e6cfd5b47fef02d3cb028ec930c04c16900259efefcd0cb9a2a031513860d1e10085a5724ea7d4e031cdc43'),
('Nelly', 'nelpankiv.roma@gmail.com', 'scrypt:32768:8:1$j1jOzwQfg3ZcrX63$05c149c781073e41bc90428a16d4227670b456a964bde98d136fd220c1d7ae3cb5418a44c0f287c0b44eb19038e3db1bbf3d6ed9c0451ba68e6e465455bc4dc9'),
('CrissAnders', 'CrisAnd@gmail.com', 'scrypt:32768:8:1$hJHgJJTNOnlsICfU$693588057f2ddfa89b146d2f03b0f2d9d1ab59cab27cc366fc148638b616b34046b66c261aeb84c9a23c03cdb88ffe3076d5d774c7932a0c6be1a53f00af456e'),
('СA', 'CA@g.com', 'scrypt:32768:8:1$73BDTR5paM71Tez0$ea1bdd61d8f6d7e35a93391c0a305229feb6ae9ddf4e22582c820cc453e5ea3e3564c5ea6644367bf7369b87dd783c762c01d40d209ac5a219738ac15775916f');