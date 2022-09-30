package menudriven;

import java.util.HashMap;

public class testing2 {

	public static void main(String[] args) {
		HashMap<String, String> cols = new HashMap<String, String>();
		cols.put("a", "1");
		cols.put("b", "2");
		System.out.println(cols.size());
		for (String key: cols.keySet()) {
            System.out.println(key+" "+cols.get(key));
        }
		System.out.println(!true);
	}

}
