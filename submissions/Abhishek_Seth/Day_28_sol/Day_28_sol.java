import java.util.*;
public class Day_28_sol{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter cipher text: ");
        String s2="";
        String s1= sc.nextLine();
        System.out.print("Enter shift value: ");
        int n=sc.nextInt();
        System.out.print("Decoded Message: ");
        for (int i = 0; i < s1.length(); i++) {
            char w = s1.charAt(i);
            if(Character.isLetter(w)){
                if(Character.isUpperCase(w)){
                    w = (char) ('A' + ((w - 'A' - n + 26) % 26));
                }
                else if(Character.isLowerCase(w)){
                    w = (char) ('a' + ((w - 'a' - n + 26) % 26));
                }
            }
            System.out.print(w);
        }
        
    }
}