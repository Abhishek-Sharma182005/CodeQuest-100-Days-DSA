import java.util.*;

public class Day_35_sol{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        System.out.print("Push ");
        String[] pushInput = sc.nextLine().split(" ");
        for (String value : pushInput) {
            stack.push(Integer.parseInt(value));
        }
        System.out.print("Pop: ");
        int popCount = sc.nextInt();
        for (int i = 0; i < popCount && !stack.isEmpty(); i++) {
            stack.pop();
        }
        System.out.print("Current Stack: ");
        for (int num : stack) {
            System.out.print(num + " ");
        }
    }
}
