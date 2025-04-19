import java.util.*;
public class Day_19_sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter numbers: ");
        String[] tokens = sc.nextLine().split("\\s+");
        List<Integer> numbers = new ArrayList<>();
        for (String token : tokens) {
            numbers.add(Integer.parseInt(token));
        }
        Collections.sort(numbers);
        System.out.print("Sorted Data: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
    }
}
