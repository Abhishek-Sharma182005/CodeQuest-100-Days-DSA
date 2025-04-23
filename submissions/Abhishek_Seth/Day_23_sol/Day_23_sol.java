import java.util.*;
public class Day_23_sol {
    public static void main(String[] args) {
        // Basic Word Frequency Counter - Time: O(n²), Space: O(n)
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text: ");
        String sen = sc.nextLine();
        String[] w = sen.split(" ");
        boolean[] c = new boolean[w.length];
        for (int i = 0; i < w.length; i++) {
            if (!c[i]) {
                int wc = 1;
                for (int j = i + 1; j < w.length; j++) {
                    if (w[i].equals(w[j])) {
                        wc++;
                        c[j] = true;
                    }
                }
                System.out.println(w[i] + ": " + wc);
            }
        }
    }
}
