import java.util.*;
public class Day_24_sol{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter numbers: ");
        String str=sc.nextLine();
        String as[]=str.trim().split("\\s");
        int n=as.length;
        int ai[]=new int[n];
        String w=""; 
        System.out.print("Decoded Message: ");
        for(int i=0;i<n;i++){
            ai[i]=Integer.parseInt(as[i]);
            System.out.print((char)ai[i]);
        }
    }
}