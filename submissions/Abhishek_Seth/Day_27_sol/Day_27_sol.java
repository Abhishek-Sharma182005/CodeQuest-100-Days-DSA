import java.util.*;
public class Day_27_sol {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter module scores (space-separated): ");
        String n = sc.nextLine(); // O(N) time & space
        String[] ele = n.trim().split("\\s+"); // O(N) time & space
        int c = 0; // O(1) space
        for (int i = 0; i < ele.length; i++) { // O(N) time
            int e = Integer.parseInt(ele[i]); // O(1) time
            if (e < 50) {
                if (c == 0) {
                    System.out.print("Modules to debug:"); // O(1)
                    c++;
                }
                System.out.print(e + " "); // O(1)
            } else if (c == 0 && i == ele.length - 1 && e >= 50) {
                System.out.println("All modules are working fine!"); // O(1)
            }
        }
        // Total Time: O(N), Total Space: O(N)
    }
}
