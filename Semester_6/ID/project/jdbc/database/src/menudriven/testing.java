package menudriven;

import java.util.ArrayList;

public class testing {

	public static void main(String[] args) {
		ArrayList<ArrayList<String>> table=new ArrayList<ArrayList<String>>();
		for(int i=0;i<5;i++) {
			ArrayList<String> row=new ArrayList<String>();
			for(int j=0;j<5;j++) {
				row.add(""+i+j);
			}
			table.add(row);
		}
		
		printer(table);
	}
	public static void printer(ArrayList<ArrayList<String>> table) {
		for(ArrayList<String> row:table) {
			for(String s:row) {
				System.out.print(s+" ");
			}
			System.out.println();
		}
	}

}
