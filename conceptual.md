### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
* - Postgres is an open source relational database management system. Data is orginized in tables with rows and columns that can have relationships between tables using foreign keys

- What is the difference between SQL and PostgreSQL?
* - structured query language used to mantaine and manipulate relational databases. postgresql uses the sql language to work with data

- In `psql`, how do you connect to a database?
* - \c

- What is the difference between `HAVING` and `WHERE`?
* - where filters by special conditions using boolean expression
* - have filters by group by

- What is the difference between an `INNER` and `OUTER` join?
* - inner join returns matching value rows between both tables
* - outter joins all the matching and unmatching values from both tables

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
* - returns the left table and matching values from the right
* - return the right table and matching values form the left

- What is an ORM? What do they do?
* - object relational mapping tool
* - translates the data from the database to not need sql

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
* - AJAX requests are made client side in a web browser
* - AJAX requests are subject to same origin policy 
* - AJAX typically transfers data using JSON
* 
* - Requests are made server side
* - Requests can make requests to any domain or API without restritions
* - Requests servers can use various data formats

- What is CSRF? What is the purpose of the CSRF token?
* - Cross Site Request Forgery. Web apps use the token to help mitigate attacks

- What is the purpose of `form.hidden_tag()`?
* - allows hidden inputs to be included like CSRF
* - the user can't see the the inputs but are
* - submitted with the form 
