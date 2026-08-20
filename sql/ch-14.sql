-- FUNCTIONS
DELIMITER //
create function square_it(x int)
returns  int 
deterministic
BEGIN
 Return x* x;
 end //
 
 delimiter ;
 
 select 
  unit_price ,
  square_it(unit_price)
  from dim_Product;
  
