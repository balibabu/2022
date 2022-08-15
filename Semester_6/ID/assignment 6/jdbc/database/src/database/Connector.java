package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class Connector {
	String url;
	String uname;
	String password;
	Statement st;
	Connection con;
	public Connector() {
		url = "jdbc:mysql://localhost:3306/s19410121182";
		uname = "root";
		password = "12345";
	}
	public void setDatabaseDetails(String url,String uname,String password) {
		this.url=url;
		this.uname=uname;
		this.password=password;
	}
	public Statement connect() throws SQLException, ClassNotFoundException {
		Class.forName("com.mysql.jdbc.Driver");
		con = DriverManager.getConnection(url, uname, password);
		st = con.createStatement();
		return st;
	}
}