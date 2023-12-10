USE iot_db;
DELIMITER //

CREATE PROCEDURE insert_10_tapes(
 table_name VARCHAR(45)
)

BEGIN
  DECLARE n INT DEFAULT 1;
  WHILE n <= 10 DO
  
    SET @name = CONCAT('Noname', n);
    SEt @query = CONCAt('INSERT INTO ', table_name, ' (name) VALUES (?)');
    
      PREPARE binding FROM @query;
      EXECUTE binding USING @name;
      DEALLOCATE PREPARE binding;
    SET n = n + 1;
  END WHILE;
END //

DELIMITER ;

CALL insert_10_tapes('user');