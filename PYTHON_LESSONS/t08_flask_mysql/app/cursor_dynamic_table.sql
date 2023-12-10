DROP PROCEDURE IF EXISTS cursor_dynamic_table;

DELIMITER //

CREATE PROCEDURE cursor_dynamic_table()
BEGIN
    DECLARE date_write INT DEFAULT FALSE;
    DECLARE table_name CHAR(30);
    DECLARE columnss INT;
    DECLARE sql_query VARCHAR(1000);
    DECLARE cur CURSOR FOR SELECT name FROM operator;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET date_write = TRUE;

 OPEN cur;
  read_loop: LOOP
   FETCH cur INTO table_name;
   IF date_write THEN
   LEAVE read_loop;
   END IF;
   SET columnss = FLOOR(1 + RAND() * 9);
   SET @sql_query = CONCAT('CREATE TABLE ', table_name, '_', DATE_FORMAT(NOW(), '%Y%m%d%H%i%s'), ' (');
   SET @n = 1;
   WHILE @n<= columnss DO
   SET @sql_query = CONCAT(@sql_query, 'column', @n, ' VARCHAR(45)');
   IF @n < columnss THEN SET @sql_query = CONCAT(@sql_query, ', ');
   END IF;
   SET @n = @n + 1;
   END WHILE;

   SET @sql_query = CONCAT(@sql_query, ')');
   PREPARE stmt FROM @sql_query;
   EXECUTE stmt;
   DEALLOCATE PREPARE stmt;
  END LOOP;
CLOSE cur;

END //

DELIMITER ;

CALL cursor_dynamic_table();