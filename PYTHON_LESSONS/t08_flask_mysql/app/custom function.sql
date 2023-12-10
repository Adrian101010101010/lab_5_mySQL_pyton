USE iot_db;
DROP FUNCTION IF EXISTS getMaxCargo;
DELIMITER //
CREATE FUNCTION getMaxCargo()
RETURNS DECIMAL(15,1)
READS SQL DATA
BEGIN
    DECLARE max_cargo DECIMAL(15,1);
    SELECT COUNT(cargo_volume) INTO max_cargo
    FROM delivery;
    RETURN max_cargo;
END //
DELIMITER ;
SELECT getMaxCargo() AS max_cargo;


DROP PROCEDURE IF EXISTS callGetMaxCargo;

DELIMITER //

CREATE PROCEDURE callGetMaxCargo()
BEGIN
 DECLARE result DECIMAL(15,1);
 SET result = getMaxCargo();
 SELECT CONCAT('Result: ', result) AS Result;

END //

 DELIMITER ;

CALL callGetMaxCargo();

