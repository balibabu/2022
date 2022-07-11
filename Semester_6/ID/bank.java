package rajashree;
import java.sql.*;

public class bank {
public static void main(String[] args) {
try
{
//Loads the jdbc driver for sql server
Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver"); 
//Create connection using getconnection()
String conurl="jdbc:sqlserver://172.17.144.108;databaseName=Rajashree";
Connection con=DriverManager.getConnection(conurl,"username","password");
System.out.println("connection is established");

Statement stmt=con.createStatement();
String sqlstr="select * from CUSTOMER";
ResultSet rs=stmt.executeQuery(sqlstr);
while(rs.next()) 
{ 
System.out.println(rs.getString(1)+ "\t" + rs.getString(2) + 
"\t\t" + rs.getLong(3) + "\t\t" +rs.getString(4)); 
}
stmt.close(); 
con.close();
}
catch(Exception e)
{
System.out.println(e);
}
}

}
