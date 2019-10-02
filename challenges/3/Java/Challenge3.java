import java.util.Scanner;

public class Challenge3 {
	// Challenge 3
	// Generate the N first elements of fibonacci sequence.
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		fibonacciSequenceOf(n);

		sc.close();
	}

	public static void fibonacciSequenceOf(int n) {

		int a = 1, b = 0, aux = 0, count = 0;

		while (count < n) {
			aux = a;
			a = a + b;

			System.out.print((count < n - 1) ? b + " " : b + "\n");

			b = aux;
			count++;
		}
	}
}
