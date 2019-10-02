import java.util.Scanner;

public class Challenge2 {
	//Challenge 2
	//Read 5 integers and calculate the arithmetic mean.
	public static void main(String[] args) {
						
		System.out.println(sumOfFiveIntegers());
		
	}
	
	public static int sumOfFiveIntegers() {
		
		int sum = 0;
		
		Scanner sc = new Scanner(System.in);
		
		for (int i = 0; i < 5; i++) 
			sum += sc.nextInt();		
					
		sc.close();
		return sum;
		
	}
	
	
}
