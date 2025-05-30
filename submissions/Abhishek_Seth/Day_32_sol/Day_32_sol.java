import java.util.*;
public class Day_32_sol{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String a1,a2;
        System.out.print("Enter first sorted array: ");
        a1=sc.nextLine();
        System.out.print("Enter second sorted array: ");
        a2=sc.nextLine();
        String a3=a1+" "+a2;
        String ar[]=a3.trim().split("\\s");
        int n=ar.length;
        int arr[]=new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(ar[i]);
        }
        Arrays.sort(arr);
        System.out.print("Merged Sorted Array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
    }
}