/*
8. WAP To Check Whether Two Strings Are Anagram Or Not?
return yes or no.

ip:
build
dubli
op:
yes

ip1:
Mother In Law
Hitler Woman
op1:
yes
*/

import java.util.*;
class Demo
{
	static String isAnagram(String s1,String s2)
	{
		// write code here
		String s3 = s1.replaceAll("\\s+","");
		String s4 = s2.replaceAll("\\s+","");
		
		String result = "yes";
		if(s3.length()!=s4.length())
			result = "no";
		else
		{
			char c1[] = s3.toLowerCase().toCharArray();
			char c2[] = s4.toLowerCase().toCharArray();
			Arrays.sort(c1);
			Arrays.sort(c2);
			
			if(!Arrays.equals(c1,c2))
				result = "no";
		}
		return result;
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		String s1 = sc.nextLine();
		String s2 = sc.nextLine();
		String result = isAnagram(s1,s2);
		System.out.println(result);
	}
}




