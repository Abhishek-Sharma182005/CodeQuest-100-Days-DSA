import java.util.*;
public class Day_22_sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  // Take input from user
        System.out.print("Enter binary number: ");
        int n = sc.nextInt();  // Read binary number as integer
        int c = 0;
        int d, i = n, s = 0;
        // Convert binary to decimal
        // Time Complexity: O(k), where k is the number of digits in the binary number
        while (n != 0) {
            d = n % 10;
            s = s + d * (int)Math.pow(2, c);
            n = n / 10;
            c++;
        }
        // Output the decimal result
        System.out.print("Decimal: " + s);
        // Space Complexity: O(1)
    }
}
