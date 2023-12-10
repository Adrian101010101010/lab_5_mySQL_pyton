INSERT INTO iot_db.client_type(id, type)
VALUES
(1, 'customer'), (2, 'staff'), (3, 'manager'), (4, 'friend');

INSERT INTO iot_db.client (name, number, client_type_id)
VALUES
('Pavelchak Andrii', 10023,  4),
('Veres Zenovii', 10026, 1),
('Yatsuk Yurii', 10030, 1),
('Samotyi Volodymyr', 20011, 2),
('Shevchenko Petro', 30028, 3);

INSERT INTO iot_db.department(id, location, number, contacts)
VALUES
(1, 'Lviv', '№47', '+380(65)784 54 84'),
(2, 'Lviv', '№23', '+380(56)751 54 46'),
(3, 'Lviv', '№71', '+380(69)654 95 12'),
(4, 'Lviv', '№42', '+380(95)856 48 26'),
(5, 'Lviv', '№12', '+380(65)784 12 56'),
(6, 'Kharkiv', '№55', '+380(66)123 45 67'),
(7, 'Odessa', '№19', '+380(67)987 65 43'),
(8, 'Poltava', '№7', '+380(68)456 78 90'),
(9, 'Vinnytsia', '№31', '+380(69)111 22 33'),
(10, 'Chernihiv', '№6', '+380(67)543 21 89');

INSERT INTO iot_db.city(id, city_name)
VALUES
(1, 'Lviv'),
(2, 'Stryi'),
(3, 'kyiv'),
(4, 'Ternopil'),
(5, 'Zakarpattya'),
(6, 'Kharkiv'),
(7, 'Odessa'),
(8, 'Poltava'),
(9, 'Vinnytsia'),
(10, 'Chernihiv');

INSERT INTO iot_db.regione(name)
VALUES
('Lviv region'),
('Kyiv region'),
('Zakarpattya region'),
('Volyn region'),
('Ternopil region'),
('Kharkiv region'),
('Odessa region'),
('Poltava region'),
('Vinnytsia region'),
('Chernihiv region');

INSERT INTO iot_db.ser(id, name, surname, phone, birthday, place_of_delivery)
VALUES
(1, 'Andriy', 'Kub', '+380(93)7229 63 80', '2001-12-24', 'self pickup'),
(2, 'Igod', 'Smuk', '+380(36)943 92 00', '2002-04-15', 'self pickup'),
(3, 'Maria', 'Petrok', '+380(75)968 62 48', '2000-07-23', 'self pickup'),
(4, 'Ola', 'Holodnic', '+380(94)963 94 32', '2004-04-07', 'delivery'),
(5, 'Zak', 'Kohtr', '+380(65)156 65 95', '2003-08-12', 'delivery'),
(6, 'Vasyl', 'Koval', '+380(66)123 45 67', '2002-09-01', 'self pickup'),
(7, 'Olha', 'Bilan', '+380(99)789 12 34', '2000-04-17', 'delivery'),
(8, 'Ivan', 'Dovzhenko', '+380(67)456 78 90', '2001-11-25', 'self pickup'),
(9, 'Natalia', 'Lis', '+380(63)321 54 76', '2001-01-12', 'self pickup'),
(10, 'Taras', 'Sydor', '+380(96)876 54 32', '2002-03-04', 'delivery');

INSERT INTO iot_db.parcel(id, description, weight, status)
VALUES
(1, 'крихке', '100 KG', 'Відправляється'),
(2, 'крихке', '5 KG', 'Відправляється'),
(3, 'крихке', '2 KG', 'В дорозі '),
(4, 'крихке', '1 KG', 'В точці видіці'),
(5, 'крихке', '500 KG', 'В точці видаці'),
(6, 'фарфорова статуетка', '3 KG', 'Відправляється'),
(7, 'крихке', '10 KG', 'Відправляється'),
(8, 'дитячий одяг', '2 KG', 'В дорозі'),
(9, 'медичне обладнання', '15 KG', 'В точці видачі'),
(10, 'крихке', '5 KG', 'В точці видачі');

INSERT INTO iot_db.operator(id, name, surname, phone)
VALUES
(1, 'Andriy', 'Kub', '+380(75) 856 12 49'),
(2, 'Zak', 'Kohtr', '+380(38)380 38 00'),
(3, 'Petro', 'Petrok', '+380(99)999 99 99'),
(4, 'Ostap', 'Holodnic', '+380(11)111 11 12'),
(5, 'Igor', 'Plich', '+380(32)953 45 55'),
(6, 'Artur', 'Melnyk', '+380(59)137 62 81'),
(7, 'Vitaly', 'Koval', '+380(94)796 91 64'),
(8, 'Tetyana', 'Cap', '+380(95)495 26 35'),
(9, 'Natalia', 'Dor', '+380(55)555 55 55'),
(10, 'Oksana', 'Sydorenko', '+380(75)861 95 13');

INSERT INTO  iot_db.delivery(id, recipient, cargo_volume)
VALUES
(1, 'Andriy', '40*70*30'),
(2, 'Artur', '16*72*19'),
(3, 'Zak', '12*12*12'),
(4, 'Dgon', '50*75*30'),
(5, 'Dgon', '90*56*50'),
(6, 'Mykhailo', '35*60*25'),
(7, 'Oksana', '20*50*15'),
(8, 'Vasyl', '42*68*33'),
(9, 'Natalia', '28*55*20'),
(10,'Vitaly', '60*80*40');

INSERT INTO iot_db.courier(id, name, surname, phone, birthday)
VALUES
(1, 'Artur', 'Cap', '+380(45)786 45 29', '2001-10-24'),
(2, 'Panas', 'Madrid', '+380(78)496 79 45', '1988-06-3'),
(3, 'Zak', 'Luk', '+380(67)364 46 63', '1999-09-09'),
(4, 'Dgon', 'Karter', '+380(55)762 35 76', '2000-12-20'),
(5, 'Andriy', 'Dor', '+380(49)486 72 92', '2002-02-02'),
(6, 'Ivan', 'Petrov', '+380(11)123 45 67', '1995-03-17'),
(7, 'Marina', 'Sydorenko', '+380(68)987 12 34', '1990-08-25'),
(8, 'Olexandr', 'Ivanov', '+380(50)555 99 77', '1985-02-10'),
(9, 'Tetyana', 'Koval', '+380(99)777 11 88', '1992-11-29'),
(10, 'Andriy', 'Melnyk', '+380(44)321 76 54', '1998-06-03');

INSERT INTO iot_db.courier_has_delivery(courier_id, delivery_id)
VALUES
(1, 1), (2, 2), (3, 3), (4, 4),
(5, 5), (6, 6), (7, 7), (8, 8),
(9, 9), (10, 10);

INSERT INTO iot_db.parcel_has_courier(courier_id, parcel_id)
VALUES
(1, 1), (2, 2), (3, 3),
(4, 4), (5, 5), (6, 6),
(7, 7), (8, 8), (9, 9), (10, 10);

INSERT INTO iot_db.post_office(number, users)
VALUES
(1, 1), (2, 2), (3, 3),
(4, 4), (5, 5), (6, 6),
(7, 7), (8, 8), (9, 9), (10, 10);
