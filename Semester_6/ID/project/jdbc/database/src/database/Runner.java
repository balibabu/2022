package database;

public class Runner {

	public static void main(String[] args) throws Exception {
		Connector db=new Connector();
		db.connect();
		DBOperator op=new DBOperator(db.st);
		op.show("account");
//		op.insert("account");
		op.delete("account", "Type", "B00A");
		
	}
}
