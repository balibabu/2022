package jdbcTest;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class bank {

	public static void main(String[] args) {
		try {
			Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
			String conurl = "jdbc:sqlserver://172.17.144.108;databaseName=s19410121182";
			Connection con = DriverManager.getConnection(conurl, "s19410121182", "Iter1234#");
			System.out.println("connection is established");

			Statement stmt = con.createStatement();
			String sqlstr = "select * from CUSTOMER";
			ResultSet rs = stmt.executeQuery(sqlstr);
			while (rs.next()) {
				System.out.println(
						rs.getString(1) + "\t" + rs.getString(2) + "\t\t" + rs.getLong(3) + "\t\t" + rs.getString(4));
			}
			stmt.close();
			con.close();
		} catch (Exception e) {
			System.out.println(e);
		}
	}
}
