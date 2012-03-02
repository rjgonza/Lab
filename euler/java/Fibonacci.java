import java.util.*;
public class Fibonacci{
	public static void main (String[] args){
	int x;
		if(args.length<1){
			Scanner scan = new Scanner(System.in);
			System.out.print("Enter a number: ");
			x=scan.nextInt();
			System.out.println(fib(x));
		}else
                        System.out.println(fib(Integer.parseInt(args[0])));

	}

	public static int fib(int x){
		if (x < 2)
			return x;
		else
			return fib(x-1)+fib(x-2);
	}
}
