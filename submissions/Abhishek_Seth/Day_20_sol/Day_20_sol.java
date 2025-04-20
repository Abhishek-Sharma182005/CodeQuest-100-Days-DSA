import java.util.*;
public class Day_20_sol{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int c=0;
        for (int i =2; i < n; i++) {
            if (n%i==0){
                c++;
            }
        }
        if(c==0){
            System.out.println("Prime");
        }
        else{
            System.out.println("Not Prime");
        }
    }
}