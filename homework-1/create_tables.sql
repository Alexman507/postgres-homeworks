-- SQL-команды для создания таблиц
create database north;

create table customers (
customer_id varchar(5) unique,
company_name varchar(100) not null,
contact_name varchar(100) not null
);

-- drop table customers;

create table employees (
employee_id int primary key,
first_name varchar(100) not null,
last_name varchar(100) not null,
title varchar(100) not null,
birth_date date,
notes text
);

create table orders (
order_id int primary key,
customer_id varchar(5) references customers (customer_id),
employee_id int references employees (employee_id),
order_date date not null,
ship_city varchar(100) not null
)

--alternative method for copy data from files.csv
copy customers from 'C:\Users\SRE\PycharmProjects\postgres-homeworks\homework-1\north_data\customers_data.csv' with (format csv)
copy employees from 'C:\Users\SRE\PycharmProjects\postgres-homeworks\homework-1\north_data\employees_data.csv' with (format csv)
copy orders from 'C:\Users\SRE\PycharmProjects\postgres-homeworks\homework-1\north_data\orders_data.csv' with (format csv)