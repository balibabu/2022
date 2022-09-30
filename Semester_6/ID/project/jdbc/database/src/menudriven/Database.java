package menudriven;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Scanner;

public class Database {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) throws Exception {
		driveMenu();
	}

	public static void driveMenu() throws Exception {
		Statement st = getStatement();
		showMenu();
		int choice = 0;
		do {
			System.out.println("\nEnter your choice (0 to show menu again)");
			choice = sc.nextInt();
			switch (choice) {
			case 0:
				showMenu();
				break;
			case 1:
				showRecords(st);
				break;
			case 2:
				addCustomer(st);
				break;
			case 3:
				deleteCustomer(st);
				break;
			case 4:
				updateCustomer(st);
				break;
			case 5:
				showAccountDetails(st);
				break;
			case 6:
				showLoanDetails(st);
				break;
			case 7:
				depositeMoney(st);
				break;
			case 8:
				withdrawMoney(st);
				break;
			}

		} while (choice != 9);
	}

	private static void withdrawMoney(Statement st) throws SQLException {
		System.out.println("enter account number and amount to withdraw");
		String acc_no=sc.next();
		int amt=sc.nextInt();
		String query="update account set balance=balance-%d where account_no='%s'".formatted(amt,acc_no);
		int count=st.executeUpdate(query);
		System.out.println("%d rows affected".formatted(count));
	}

	private static void depositeMoney(Statement st) throws SQLException {
		System.out.println("enter account number and amount to deposit");
		String acc_no=sc.next();
		int amt=sc.nextInt();
		String query="update account set balance=balance+%d where account_no='%s'".formatted(amt,acc_no);
		int count=st.executeUpdate(query);
		System.out.println("%d rows affected".formatted(count));
	}

	private static void showLoanDetails(Statement st) throws SQLException {
		System.out.println("enter customer number");
		String cust_no=sc.next();
		
		String query="select * from customer "
				+ "inner join loan using(cust_no) "
				+ "where customer.cust_no='%s'".formatted(cust_no);
		showQueryTable(st, query);
		
	}
	
	private static void showQueryTable(Statement st,String query) throws SQLException {
		ResultSet rs=st.executeQuery(query);
		System.out.println(rs.getFetchSize());
		System.out.println("showing records");
		
		ResultSetMetaData rsMetaData = rs.getMetaData();
		int count = rsMetaData.getColumnCount();
		
		ArrayList<String> cols=new ArrayList<String>();
		for(int i = 1; i<=count; i++) {
			cols.add(rsMetaData.getColumnName(i));
		}
		
		for(String s:cols) {
			System.out.print(s+"\t\t");
		}
		System.out.println();
		
		while(rs.next()) {
			for(String s:cols) {
				System.out.print(rs.getString(s)+"\t\t");
			}
			System.out.println();
		}
	}

	private static void showAccountDetails(Statement st) throws SQLException {
		System.out.println("enter customer number");
		String cust_no=sc.next();
		
		String query="select customer.*,account.* from customer "
				+ "inner join depositor on customer.cust_no=depositor.cust_no "
				+ "inner join account on depositor.account_no=account.account_no "
				+ "where customer.cust_no='%s'".formatted(cust_no);
		showQueryTable(st, query);
	}

	private static void updateCustomer(Statement st) throws SQLException {
		sc.nextLine();
		System.out.println("enter customer number");
		String cust_no=sc.nextLine();
		System.out.println("\nUpdate ?\n1.Name\n2.Phone Number\n3.City\n4.Exit\nMake your choice");
		int choice=sc.nextInt();
		sc.nextLine();
		switch (choice) {
		case 1:
			System.out.println("enter new name");
			String name=sc.nextLine();
			update(st,cust_no,"name",name);
			break;
		case 2:
			System.out.println("enter new phone number");
			String phone_no=sc.next();
			update(st,cust_no,"phone_no",phone_no);
			break;
		case 3:
			System.out.println("enter new city");
			String city=sc.next();
			update(st,cust_no,"city",city);
			break;
		case 4:
			return;
		}
	}
	
	private static void update(Statement st, String cust_no, String colName, String newValue) throws SQLException {
		String query="update customer set %s='%s' where cust_no='%s'".formatted(colName,newValue,cust_no);
		int count=st.executeUpdate(query);
		System.out.println("%d rows affected".formatted(count));
	}

	private static void deleteCustomer(Statement st) throws SQLException {
		sc.nextLine();
		System.out.println("enter customer number");
		String cust_no=sc.nextLine();
		
		String query="delete from customer where cust_no='%s'".formatted(cust_no);
		int count=st.executeUpdate(query);
		System.out.println("%d rows affected".formatted(count));
	}

	private static void addCustomer(Statement st) throws SQLException {
		sc.nextLine();  //previous input is int so to avoid assigning of \n to cust_no
		System.out.println("enter cust_no,name,phone_no,city");
		String cust_no=sc.nextLine();
		String name=sc.nextLine();
		String phone_no=sc.nextLine();
		String city=sc.nextLine();
		
		String query="insert into customer values('%s','%s','%s','%s');".formatted(cust_no,name,phone_no,city);
		System.out.println(query);
		int count=st.executeUpdate(query);
		System.out.println("%d rows affected".formatted(count));
	}

	private static void showRecords(Statement st) throws SQLException {
		System.out.println("Showing all Records");
		String query = "select * from Customer";
		showQueryTable(st, query);
	}

	public static void showMenu() {
		System.out.println("1.Show All Customers Details");
		System.out.println("2.Add customer");
		System.out.println("3.Delete customer");
		System.out.println("4.Update customer");
		System.out.println("5.Show account details of a customer");
		System.out.println("6.Show loan details of a customer");
		System.out.println("7.Deposite money");
		System.out.println("8.Withdraw money");
		System.out.println("9.Exit");

	}

	public static Statement getStatement() throws ClassNotFoundException, SQLException {
		String url = "jdbc:mysql://localhost:3306/s19410121182";
		String uname = "root";
		String password = "12345";
		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection(url, uname, password);
		Statement st = con.createStatement();
		return st;
	}
}
