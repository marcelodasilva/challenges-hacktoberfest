import java.util.Random;

public class Challenge1 {
	// Challenge 1
	// Given an array of 10 integers numbers generated randomly, find the sum of its
	// elements.
	public static void main(String[] args) {

		System.out.println(sumOfTenIntgers(genereteTenIntegers()));

	}

	public static int[] genereteTenIntegers() {

		Random rd = new Random();

		int arrayOfTenIntegers[] = new int[10];

		for (int i = 0; i < arrayOfTenIntegers.length; i++) {
			arrayOfTenIntegers[i] = rd.nextInt(100);
		}

		return arrayOfTenIntegers;

	}

	public static int sumOfTenIntgers(int arrayOfTenIntegers[]) {
		int sum = 0;

		for (int i : arrayOfTenIntegers)
			sum += i;

		showTenIntgers(arrayOfTenIntegers);

		return sum;
	}

	public static void showTenIntgers(int arrayOfTenIntegers[]) {

		for (int i = 0; i < arrayOfTenIntegers.length; i++)
			System.out.print((i < arrayOfTenIntegers.length - 1) ?  arrayOfTenIntegers[i] + " + " : arrayOfTenIntegers[i]);			

		System.out.print(": ");
	}
}
