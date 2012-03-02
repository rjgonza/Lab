//The prime factors of 13195 are 5, 7, 13 and 29.
//
//What is the largest prime factor of the number 600851475143 ?

//Author: Ramon J. Gonzalez
//2011.06.13

import java.util.Scanner;

public class problem3 {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the (whole)number you want to find the largest factor of: ");
		long num=scan.nextLong();
		System.out.println("Calculating the largest prime factor of: " + num);
		long factor=1;
		long currentprime=0;
		for (long x=num; x>1; x--)
			if (num%x==0 && isPrime(x))
			{
				currentprime=x;
				if (currentprime>factor)
					factor=currentprime;
			}
		System.out.println("The larget prime factor of " + num + " is " + factor);
	}
	
	public static boolean isPrime(long x){
		boolean prime=true;
		for (long i=2; i<x; i++)
			if(x%i==0)
				prime=false;
		return prime;
	}
}

//600_851_475_143 
//123_456_789_123
