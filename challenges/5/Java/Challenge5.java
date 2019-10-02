import java.util.Scanner;

public class Challenge5 {
	// Challenge 5
	// Make a Program that reads 2 numbers and shows the biggest one.
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n1 = sc.nextInt();
		int n2 = sc.nextInt();

		System.out.println(biggestBetween(n1, n2));

		sc.close();
	}
	
	public static int biggestBetween(int n1, int n2) {
		return (n1 > n2) ? n1 : n2;
	}
	
}
