USE iot_db
DELIMITER //
CREATE PROCEDURE data_insertion(
   courier VARCHAR(45),
   name VARCHAR(45), 
   surname VARCHAR(45),
   phone VARCHAR(45),
   birthday DATE
  )

BEGIN
  SET @insertQuery := CONCAT('INSERT INTO ', courier, ' (name, surname, phone, birthday) VALUES (?,?,?,?)');
  
  PREPARE binding FROM @insertQuery;
    SET @name := name;
    SET @surname := surname;
    SET @phone := phone;
    SET @birthday := birthday;
  EXECUTE binding USING @name, @surname, @phone, @birthday;
  DEALLOCATE PREPARE binding;
END //

DELIMITER ;
call data_insertion ('courier','Andrii','Pavelchak','+380 (75) 654 28 64','1976-05-09')