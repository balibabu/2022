/*
16) WAP to find the frequency of each element in the array
ip1:
9 // size of an array
1 2 8 3 2 2 2 5 1 // array elements
op1:
1 repeated 2 times
2 repeated 4 times
8 repeated 1 times
3 repeated 1 times
5 repeated 1 times
*/

import java.util.Scanner;
class Demo
{
	static void frequency(int a[])
	{
		// write code here
		int i,j,count;
		for(i=0;i<a.length;i++)
		{
			count = 1;
			for(j=i+1;j<a.length;j++)
			{
				if(a[i]==a[j])
				{
					count++;
					a[j] = -1;
				}
			}
			if(a[i]!=-1)
				System.out.println(a[i]+"-"+count);
		}
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a[] = new int[n];
		int i;
		for(i=0;i<n;i++)
			a[i] = sc.nextInt();
		
		frequency(a);
		
	}
}
