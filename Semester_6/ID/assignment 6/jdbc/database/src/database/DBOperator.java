package database;

import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Scanner;

public class DBOperator {
	
	public DBOperator(Statement st) {
		Query.st = st;
	}

	public void show(String table) throws Exception {
		String query = "select * from "+table;
		Query.show(query);
	}
	
	public void insert(String table) throws SQLException {
		Scanner sc=new Scanner(System.in);
		HashMap<String, String> cols =Query.columnsType("select * from "+table);
		String query="insert into "+table+" values(";
		int c=cols.size();
		for (String key: cols.keySet()) {
            System.out.println("enter value for "+key);
            if(cols.get(key).equalsIgnoreCase("int")) {
            	query+=sc.nextLine();
            }else {
            	query+="'%s'".formatted(sc.nextLine());
            }
            query+=c-->1?", ":"";
        }
		query+=")";
		System.out.println(query);
	}

	public void delete(String table, String colName,String colValue) throws SQLException {
		HashMap<String, String> cols =Query.columnsType("select * from "+table);
		colValue=(!cols.get(colName).equalsIgnoreCase("int"))?"'"+colValue+"'":colValue;
		String query="delet from %s where %s=%s".formatted(table,colName,colValue);
		System.out.println(query);
	}

	public void update(String table,String keyName,String keyValue) throws SQLException {
		Scanner sc=new Scanner(System.in);
		HashMap<String, String> cols =Query.columnsType("select * from "+table);
		
		System.out.println("\nenter the column Name you wanna change and new Value for that");
		for (String key: cols.keySet()) {
			System.out.println(key);
		}
		String colname=sc.nextLine();
		String newValue=sc.nextLine();
		
		newValue=!cols.get(colname).equalsIgnoreCase("int")?"'"+newValue+"'":newValue;
		keyValue=(!cols.get(keyName).equalsIgnoreCase("int"))?"'"+keyValue+"'":keyValue;
		String query="update %s set %s=%s where %s=%s".formatted(table,colname,newValue,keyName,keyValue);
		System.out.println(query);
	}

}



















//select * from customer
//show tables
/*
private void print(HashMap<String, String> cols) {
	for (String key: cols.keySet()) {
		System.out.println(key+" "+cols.get(key));
	}
}
 * ArrayList<String> cols =Query.columns(query); for(String s: cols)
 * System.out.println(s);
 * 
 */