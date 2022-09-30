package examQuestions;

import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Set;

public class MyFunction {

	public static void main(String[] args) {
		int[] array = { 1, 2, 3, 4, 1, 4, 2, 5, 1, 2, 5 };
		HashMap<Integer, Integer> map = Counter(array);
		System.out.println(map);
	}

	public static void printHashMap(HashMap<Integer, Integer> map) {
		Set<Entry<Integer, Integer>> values = map.entrySet();
		for (Entry<Integer, Integer> e : values) {
			System.out.println(e.getKey() + ":" + e.getValue());
		}
	}
	public static HashMap<Integer, Integer> Counter(int[] array) {
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		for (int i = 0; i < array.length; i++) {
			if (map.containsKey(array[i])) {
				map.put(array[i], 1 + map.get(array[i]));
			} else {
				map.put(array[i], 1);
			}
		}
		return map;
	}
}
