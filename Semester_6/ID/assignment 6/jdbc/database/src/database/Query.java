package database;

import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;

public class Query {
	static Statement st;

	public static void show(String query) throws SQLException {
		ResultSet rs = st.executeQuery(query);
		ResultSetMetaData rsMetaData = rs.getMetaData();
		int count = rsMetaData.getColumnCount();

		ArrayList<String> cols = new ArrayList<String>();
		for (int i = 1; i <= count; i++) {
			cols.add(rsMetaData.getColumnName(i));
		}
		String separator=count==1?"":", ";
		for (String s : cols) {
			System.out.print(s + separator);
		}
		System.out.println();

		int sn = 1;
		while (rs.next()) {
			System.out.print(sn++ + ". ");
			for (String s : cols) {
				System.out.print(rs.getString(s) + separator);
			}
			System.out.println();
		}
	}

	public static ArrayList<String> columns(String query) throws SQLException {
		ResultSet rs = st.executeQuery(query);
		ResultSetMetaData rsMetaData = rs.getMetaData();
		int count = rsMetaData.getColumnCount();

		ArrayList<String> cols = new ArrayList<String>();
		for (int i = 1; i <= count; i++) {
			cols.add(rsMetaData.getColumnName(i));
		}
		return cols;
	}

	public static void execute(String query) throws SQLException {
		int count=st.executeUpdate(query);
		System.out.println("%d rows affected".formatted(count));
	}
	
	public static HashMap<String,String> columnsType(String query) throws SQLException {
		ResultSet rs = st.executeQuery(query);
		ResultSetMetaData rsMetaData = rs.getMetaData();
		int count = rsMetaData.getColumnCount();
		HashMap<String,String> columnTypeName=new HashMap<String, String>();
		for (int i = 1; i <= count; i++) {
			columnTypeName.put(rsMetaData.getColumnName(i), rsMetaData.getColumnTypeName(i));
		}
//		System.out.println(columnTypeName);
		return columnTypeName;
	}
	
	public static void test(String query) throws SQLException {
		ResultSet rs = st.executeQuery(query);
		String name;
//		name =rs.get();
//		System.out.println(name);
		while (rs.next()) { // to move pointer from column name to data row
			name =rs.getString(1);
			System.out.println(name);
		}
	}
}
