create database bankingsystem4;
use bankingsystem4;

CREATE TABLE bankingsystem4 (
	login_account varchar(30),
	account_number varchar(20),
	balance_amount varchar(200), 
	password int,
	deposite_amount int,
	withdraw_amount int
);
SELECT * FROM bankingsystem4;
insert into bankingsystem4(login_account,account_number,balance_amount,password,deposite_amount,withdraw_amount) value("123s","1234a","2000","143","60","70");
insert into bankingsystem4(login_account,account_number,balance_amount,password,deposite_amount,withdraw_amount) value("123e","1234k","1000","123","100","50");
insert into bankingsystem4(login_account,account_number,balance_amount,password,deposite_amount,withdraw_amount) value("123b","1234u","1500","133","500","1000");