import java.util.*;

public class Day_36_sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().toLowerCase().replaceAll("[^a-z\\s]", ""); // remove punctuation
        String[] w = s.split("\\s+");
        Map<String, Integer> frequencyMap = new LinkedHashMap<>();
        for (String word : w) {
            frequencyMap.put(word, frequencyMap.getOrDefault(word, 0) + 1);
        }
        int c = 0;
        for (Map.Entry<String, Integer> entry : frequencyMap.entrySet()) {
            if (c == 0) {
                System.out.print(entry.getKey() + ": " + entry.getValue());
            } else {
                System.out.print(", " + entry.getKey() + ": " + entry.getValue());
            }
            c++;
        }
    }
}
