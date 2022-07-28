/*
1) WAP to left rotate the elements of an array.
ip:
5 // array size
1 2 3 4 5 // array elements
2 // no.of rotations
op:
3 4 5 1 2
------------------------

test cases:

ip1:
5
1 2 3 4 5
2
op1:
3 4 5 1 2

ip2:
6
10 20 30 80 99 2
2
op2:
30 80 99 2 10 20

ip3:
4
5 5 5 5
1
op3:
5 5 5 5


ip4:
5
1 8 45 23 99
0
op4:
1 8 45 23 99
*/

import java.util.Scanner;
class Demo
{
	static int[] leftRotate(int n,int a[], int r)
	{
		// write code here
		int temp,i,j;
		for(i=1; i<=r ;i++)
		{
			temp = a[0];
			for(j=1; j<n; j++)
			{
				a[j-1] = a[j];
			}
			a[n-1] = temp;
		}
		return a;
		
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a[] = new int[n];
		int i;
		for(i=0;i<n;i++)
			a[i] = sc.nextInt();
		int r = sc.nextInt();
		
		a = leftRotate(n,a,r);
		
		for(i=0;i<n;i++)
			System.out.print(a[i]+" ");
	}
}