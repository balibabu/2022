package examQuestions							;
import java.util.Scanner						;
public class test1 								{
	public static void main(String[] args) 		{
		for(int i=0;i<5;i++) 					{
			System.out.println("Hello World")	;
												}
		Scanner sc=new Scanner(System.in)		;
		int n=sc.nextInt();
		sc.nextLine();
		String name=sc.nextLine()				;
		String phone_no=sc.nextLine()			;
		System.out.println(name)				;
		System.out.println(phone_no)			;
		String q="%s     %s".formatted(name,phone_no);
		System.out.println(q);
												}
												}
