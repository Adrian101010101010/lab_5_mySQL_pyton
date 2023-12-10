USE iot_db;
DELIMITER //
CREATE TRIGGER check_value_before_insert
BEFORE INSERT ON iot_db.user
FOR EACH ROW 
BEGIN 
  IF NEW.name LIKE '%00' THEN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'A column value cannot end with two zeros';
  END IF;
END;
DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_modification
BEFORE INSERT ON iot_db.city
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'this table cannot be changed';
END;
DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_update
BEFORE UPDATE ON iot_db.city
FOR EACH ROW
BEGIN
   SIGNAL SQLSTATE '45000'
   SET MESSAGE_TEXT = 'this table cannot be changed';
END;
DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_delete
BEFORE DELETE ON iot_db.city
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
 SET MESSAGE_TEXT = 'this table cannot be changed';
END;
DELIMITER ;

DELIMITER //
CREATE TRIGGER restrict_names
BEFORE INSERT ON user
FOR EACH ROW
BEGIN
  IF NEW.name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'Сan be created only from such names: Svitlana, Petro, Olha, Taras.';
  END IF;
END;
DELIMITER ;

DELIMITER //
CREATE TRIGGER restrict_names_update
BEFORE UPDATE ON iot_db.user
FOR EACH ROW
BEGIN
  IF NEW.COlumn_name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'Can only be updated to such names: Svitlana, Petro, Olha, Taras.';
  END IF;
END;

DELIMITER ;