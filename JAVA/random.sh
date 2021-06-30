#!/usr/bin/java --source 11

import java.util.Random;
import java.util.Scanner;

 public class Rand{
     public static void main(String[] args)
     {
         Random number = new Random();
         int x = number.nextInt(101);
         Scanner data = new Scanner(System.in);
         //System.out.println("Digite Numero");
         int a = 0 ; //data.nextInt();
         System.out.println(x);

         while( x != a ){
             System.out.println("Digite Numero");
             a = data.nextInt();
             if (a < x ){
                    System.out.println("El numero es mayor");
                }else if( a > x ){
                    System.out.println("El numero es menor ");
                }else {
                    break;
}
            
         }
     }
}
