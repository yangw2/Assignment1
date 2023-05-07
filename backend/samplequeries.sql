/* List of 10 most popular male hispanic names in 2014 in descending order. */

SELECT * FROM childNames WHERE sex = 'MALE' AND ethnicity = 'HISPANIC' and yearOfBirth = 2014 ORDER BY amountNames DESC LIMIT 10;

/* Shows the total amount of children named Aidan or Wesley regardless of year or sex  */

SELECT childName, SUM(amountNames) AS total_amount FROM childNames WHERE childName = 'Aidan' OR childName = 'Wesley' GROUP BY childName ORDER BY total_amount DESC;

/* Shows overall top 20 most popular female names throughout all years in descending order*/ 

SELECT childName, SUM(amountNames) AS total_amount FROM childNames WHERE sex = 'FEMALE' GROUP BY childName ORDER BY total_amount DESC LIMIT 20;
