package examQuestions;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class hashRelated {

	public static void main(String[] args) {
		HashMap<Integer, String> map=new HashMap<Integer, String>();
		map.put(123, "bali");
		map.put(124, "amrit");
		map.put(125, "rajshri");
		map.put(126, "priya");
		map.put(127, "komal");
		
		System.out.println(map.size());
		HashMap<Integer, String> map2=map;
		map2.put(128,"Anusha");
		System.out.println(map.size());
		
//		method1(map);
//		method2(map);
//		method3(map);
//		method4(map);
		System.out.println("Done execution.......");
	}
	
	public static void method1(HashMap<Integer, String> map) {
		System.out.println(map.get(126));
	}	
	public static void method2(HashMap<Integer, String> map) {
		Set<Integer> keys=map.keySet();
		for(int i:keys) {
			System.out.println(map.get(i));
		}
	}
	public static void method3(HashMap<Integer, String> map) {
		Set<Entry<Integer, String>> values=map.entrySet();
		for(Map.Entry<Integer, String> e: values) {
//			e.setValue("babu");
			System.out.println(e.getKey()+":"+e.getValue());
		}
//		method2(map);
	}

	public static void method4(HashMap<Integer, String> map) {
		System.out.println((map.containsKey(123)));
		
	}
}
