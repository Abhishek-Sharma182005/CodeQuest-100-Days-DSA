import java.util.*;
public class Day_26_sol{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String str=sc.nextLine().toLowerCase();
        int c1=0;
        int c2=0;
        for(int i = 0; i <str.length();i++){
            if(str.charAt(i)=='a'||str.charAt(i)=='e'||str.charAt(i)=='i'||str.charAt(i)=='o'||str.charAt(i)=='u'){
                c1++;
            }
            else if(str.charAt(i)>='a'&& str.charAt(i)<='z'){
                c2++;
            }
        }
        System.out.println("Vowels: " +c1+"\nConsonants: "+c2);
    }
}