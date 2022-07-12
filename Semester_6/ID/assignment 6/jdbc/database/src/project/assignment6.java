package project;

public class assignment6 {

	public static void main(String[] args) throws Exception {
		
	}

}
/*
import java.sql.*; 
import java.io.*;
 public class myjdbcproj{ 
 public static void main(String args[]) throws IOException
{ 
 Connection con=null;
 Statement stmt=null;
 // Declare common variables if any
try{ 
 // Load the driver class 
 Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver"); 
 
 // Create the connection object 
String conurl="jdbc:sqlserver://172.17.144.108;databaseName=sregd.no";
 con=DriverManager.getConnection(conurl,"user ID","user password"); 
stmt=con.createStatement();
do
{
System.out.println("\n\n***** Banking Management System*****");
// Display the menu
System.out.println("Enter your choice(1-9):");
// Accept user's choice
switch(choice_variable)
{
case 1:
// Display customer records
break;
case 2:
// Add customer record
// Accept input for each column from user
break;
case 3:
// Delete customer record
// Accept customer number from user
break;
case 4:
// Update customer record
// Accept customer number from user
System.out.println("Enter 1: For Name 2: For Phone no 3: For City to update:");
// Accept user's choice
switch(choice_variable_1)
{
case 1:
// Update customer's name
break;
case 2:
// Update customer's phone number
break;
case 3:
// Update customer's city
break;
}
break;
case 5:
// Display account details
// Accept customer number from user
 break;
case 6:
// Display loan details 
// Accept customer number from user
// Display the number of loans the customer has or 
// Congratulation if he customer has no loan
break;
case 7:
//Deposit money
// Accept the account number to be deposited in 
// Message for transaction completion
break;
case 8:
//Withdraw money
// Accept the account number to be withdrawn from 
// Handle appropriate withdral ckeck conditions
// Message for transaction completion
break; 
case 9:
// Exit the menu
break;
default:
// Handle wrong choice of option
}
}while(condition);
} //try closing
catch(Exception e)
{ 
// Handling exception
System.out.println(e);
}
 
}// main closing
}// End class
*/