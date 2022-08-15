package database;

import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class Customer extends DBOperator {
	MetaData md;
	String cust_no;
	Scanner sc = new Scanner(System.in);

	public Customer(Statement st) throws SQLException {
		super(st);
		md=new MetaData("customer");
		cust_no=sc.nextLine();
	}

	public void show() throws Exception {
		show("customer");
	}

	public void insert() throws SQLException {
		insert("customer");
	}

	public void delete() {
		
		System.out.println();
	}
}
