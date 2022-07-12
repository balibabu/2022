package project;

import java.sql.*;

public class JDBCProject {

	public static void main(String[] args) throws Exception {
		String url = "jdbc:mysql://localhost:3306/aliens"; // database name
		String uname = "root";
		String password = "12345";

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection(url, uname, password);
		Statement st = con.createStatement();
		
		//getting data from table
		fetching(st);
		
		//inserting data in table
//		insertion1(st);
//		insertion2(con);
		
	}
	
	public static void fetching(Statement st)throws Exception {
		String query = "select * from student";
		ResultSet rs = st.executeQuery(query);
		while (rs.next()) { // to move pointer from column name to data row
			String name =rs.getInt("Sroll_no")+" "+ rs.getString("Sname");
			System.out.println(name);
		}
	}
	
	public static void insertion1(Statement st) throws Exception {
		String query = "insert into student values (4,'Ladu')";
		int count = st.executeUpdate(query);
		System.out.println(count+" rows affected");
	}
	
	public static void insertion2(Connection con) throws Exception { //using prepared statement
		String name="Bhola";
		int roll=5;
		String query = "insert into student values (?,?)";
		
		PreparedStatement st=con.prepareStatement(query);
		st.setInt(1, roll);
		st.setString(2, name);
		int count = st.executeUpdate();
		System.out.println(count+" rows affected");
	}
	

}
