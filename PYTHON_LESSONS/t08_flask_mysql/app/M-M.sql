USE iot_db
DELIMITER //

CREATE PROCEDURE insert_into_docking_table_courier_has_delivery(
  corier_name VARCHAR(45),
  corier_phone VARCHAR(45),
  delivery_recipient VARCHAR(45)
)
  
BEGIN
 DECLARE courier_id INT;
 DECLARE delivery_id INT;
 
 SELECT id INTO courier_id
  FROM courier
   WHERE name = corier_name AND phone = corier_phone;
   
SELECT id INTO delivery_id
 FROM delivery
   WHERE recipient = delivery_recipient;
   
INSERT INTO courier_has_delivery(courier_id, delivery_id)
VALUES (courier_id, delivery_id);
END //
DELIMITER ;

CALL insert_into_docking_table_courier_has_delivery('Antin','+380 (46) 751 75 84', 'Antin');