#!/usr/bin/java --source 11
import java.util.Scanner;
 
public class HelloClass{
    public static void main(String[] args)
    {
        Scanner data = new Scanner(System.in);
        int a = data.nextInt();
        int b = data.nextInt();
        
        int sum = a + b;
        int dif = a - b;
        int mul = a * b;
        int div = a / b;
        System.out.println( "el resultado de suma es " + sum + "," + dif + ","+ mul + "," + div);
     
    }
        


}
