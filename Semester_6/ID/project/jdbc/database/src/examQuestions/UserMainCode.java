package examQuestions;

import java.nio.channels.UnsupportedAddressTypeException;

public class UserMainCode {

	public static void main(String[] args) {
		String str="Bali bAbu";
		System.out.println(reverseWordsAndCase("Wipro Technologies, Banglore,1",1));
		
	}
	public static String reverseWordsAndCase(String input1,int input2) {
		if(input2==0) {
			return case1(input1);
		}
		return case2(input1);
	}
	public static String case2(String str) {
		String[] arrOfStr = str.split(" ");
		String newStr=reverse2(arrOfStr[0]);
		for(int i=1;i<arrOfStr.length;i++) {
			newStr+=" "+reverse2(arrOfStr[i]);
		}
		return newStr;
	}
	
	public static String case1(String str) {
		String[] arrOfStr = str.split(" ");
		String newStr=reverse(arrOfStr[0]);
		
		for(int i=1;i<arrOfStr.length;i++) {
			newStr+=" "+reverse(arrOfStr[i]);
		}
		return newStr;
	}
	
	public static String reverse(String str) {
		String newStr="";
		for(int i=str.length()-1;i>=0;i--) {
			newStr+=str.charAt(i);
		}
		return newStr;
	}
	public static String reverse2(String str) {
		int[] arr=new int[str.length()];
		for(int i=0;i<str.length();i++) {
			if(str.charAt(i)>=65 && str.charAt(i)<=90) {
				arr[i]=1;
			}
		}
		str=str.toLowerCase();
		char[] charArr=reverse(str).toCharArray();
		for(int i=0;i<charArr.length;i++) {
			if(arr[i]==1) {
				if(charArr[i]>=97 && charArr[i]<=122) {
					charArr[i]-=32;
				}else {
					charArr[charArr.length-i-1]-=32;
				}
			}
		}
		String newStr=new String(charArr);
		return newStr;
	}

}
