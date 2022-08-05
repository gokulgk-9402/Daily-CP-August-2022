# Write your MySQL query statement below
SELECT name, sum(Transactions.amount) as balance
FROM Users, Transactions
WHERE Users.account = Transactions.account
GROUP BY Transactions.account
HAVING balance > 10000;