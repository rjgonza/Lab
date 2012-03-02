// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
//
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

// Author: Ramon J. Gonzalez
// 2011.06.13

public class problem2ray{
	public static void main (String[] args){
		int sum=0;
		int fibsum=0;
		int seq=1;
		int ans=0;
		while(sum<=4000000){
			fibsum=fib(seq);
			if ((fibsum%2)==0)
				ans+=fibsum;
			seq++;
			sum+=fibsum;
			System.out.println("Sequence: " + seq + " | Value: " + fibsum + " | Sum: " + ans);
		}
		System.out.println(ans);
	}

	public static int fib(int x){
		if (x < 2)
			return x;
		else
			return fib(x-1)+fib(x-2);
	}
}