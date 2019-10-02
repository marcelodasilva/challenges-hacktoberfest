import java.util.Scanner;

public class Challenge4 {
	//Challenge 4
	//Given a temperature in Fahrenheit convert it to Celsius format. Formule C = (5 * (F-32) / 9).
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		double d = sc.nextDouble();
		
		System.out.printf("%.2f%n", fahrenheitToCelsius(d));
		
		sc.close();
		
	}
	
	public static double fahrenheitToCelsius(double d) {
		return (5 * (d -32) / 9);
	}
}
