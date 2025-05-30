import java.util.*;
public class Day_25_sol{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String str=sc.nextLine();
        String as[]=str.trim().split("\\s+");
        String l="";
        for(String a:as){
            if(a.length()>=l.length()){
                l=a;
            }
        }
        System.out.println("Longest word: "+l);
    }
}