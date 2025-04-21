import java.util.*;
public class Day_21_sol {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter numbers: ");
        String n = sc.nextLine();
        String[] parts = n.trim().split("\\s+");
        int s = 0;
        for (int i = 0; i < parts.length; i++) {
            int num = Integer.parseInt(parts[i]);
            if ((i + 1) % 2 == 0) {
                s += num;
            }
        }
        System.out.println("Hidden Key: " + s);
    }
}
