-- SQL-команды для создания таблиц
CREATE table customers
(
	customer_id varchar(10) Primary key,
	company_name varchar(255) NOT NULL,
	contact_name varchar(255) NOT NULL
);

CREATE table employees
(
	employee_id int Primary key,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title text,
	birth_date date,
	notes text,
	author int REFERENCES user_account(user_id) NOT NULL
);

CREATE table orders
(
	order_id int Primary key,
	customer_id varchar(10) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(100) NOT NULL

);