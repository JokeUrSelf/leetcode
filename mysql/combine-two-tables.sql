# https://leetcode.com/problems/combine-two-tables/


SELECT p.firstName, p.lastName, a.city, a.state
FROM
Person AS p
LEFT OUTER JOIN
Address AS a
ON
p.personId = a.personId