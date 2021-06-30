#!/usr/bin/java --source 11
import java.util.Scanner;

public class rec{
 public static long Fibo(long n){
     if ((n == 0) || (n ==1)){
            return n;
        }
        else{
         return Fibo(n - 1)+ Fibo(n - 2);
     }
}
 public static void main(String[] args){
      Scanner data = new Scanner(System.in);
      System.out.println("Digite Numero");
      int n = data.nextInt();
     
      System.out.println(Fibo(n));

 }
}
