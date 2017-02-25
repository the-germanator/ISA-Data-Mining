@echo off
q -d , "SELECT c1 AS ProductID, c2 AS ProductDescription, c3 AS ProductSales FROM SalesWith100.csv" > output.log 
pause