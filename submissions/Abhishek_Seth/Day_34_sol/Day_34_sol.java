import java.util.*;

public class    Day_34_sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> queue = new LinkedList<>();
        System.out.print("Enqueue ");
        String[] enqueue = sc.nextLine().split(" ");
        for (String value : enqueue) {
            queue.add(Integer.parseInt(value));
        }
        System.out.print("Dequeue: ");
        int c = sc.nextInt();
        for (int i = 0; i < c && !queue.isEmpty(); i++) {
            queue.poll();
        }
        System.out.print("Remaining Queue: ");
        for (int num : queue) {
            System.out.print(num + " ");
        }
    }
}
