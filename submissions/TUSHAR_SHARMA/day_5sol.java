import java.util.Scanner;

public class day_5sol{
    public static void main (String [ ]args)
    {
        Scanner scanner = new 
Scanner(System .in);
//now  write code to enter
    System.out.print ("enter a number:");
    int N =scanner.nextInt();
    for (int i =1; i<=N; i++){
        System.out.println(i);
    }
    scanner.close();
    }
}