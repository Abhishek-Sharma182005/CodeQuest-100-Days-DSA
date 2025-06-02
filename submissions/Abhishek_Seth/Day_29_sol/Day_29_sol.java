import java.util.*;
public class Day_29_sol{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String n1,n2;
        System.out.print("Enter first list: ");
        n1=sc.nextLine();
        String arr1[]=n1.trim().split("\\s+");
        System.out.print("Enter second list: ");
        n2=sc.nextLine();
        String arr2[]=n2.trim().split("\\s+");
        int l1,l2,l,c=0;
        l1=arr1.length;
        l2=arr2.length;
        l=l1>=l2?l1:l2;
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                if(arr1[i].equals(arr2[j])){
                    c++;
                }
            }
        }
        if(c==0){
            System.out.println("No common elements found!");
        }
        else{
            System.out.print("Common elements: ");
            for (int i = 0; i < l; i++) {
                for (int j = 0; j < l; j++) {
                    if(arr1[i].equals(arr2[j])){
                        System.out.print(arr1[i]+" ");
                    }
                }
            }
        }
    } 
}