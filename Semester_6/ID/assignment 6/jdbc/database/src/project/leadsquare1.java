package project;

public class leadsquare1 {

	public static void main(String[] args) {
		String s="AgReEmEnT";
		char[] chars=unique(s);
		String newStr=new String(chars);
		System.out.println(newStr);
		for(char i : chars) {
			System.out.println((int)i);
		}
		
	}
	public static char[] unique(String str) {
		char[] chars=new char[str.length()];
		int pos=0;
		for(int i=0;i<str.length();i++) {
			if(!isPresent(chars, str.charAt(i))) {
				chars[pos++]=str.charAt(i);
			}
		}
		char[] ch=new char[pos-1];
		for(int i=0;i<pos-1;i++) {
			ch[i]=chars[i];
		}
		return ch;
	}
	public static boolean isPresent(char[] chars,char c) {
		for(char i : chars) {
			if(Character.toLowerCase(c)==Character.toLowerCase(i)) {
				return true;
			}
		}
		return false;
	}
	public static int count(String s,char c) {
		int count=0;
		for(int i=0;i<s.length();i++) {
			if(Character.toLowerCase(c)==Character.toLowerCase(s.charAt(i))) {
				count++;
			} 
		}
		return count;
	}
}
