#!/usr/bin/java --source 11
import java.util.Scanner;

 public class Multi{
     public static void main(String[] args)
     {
         Scanner data = new Scanner(System.in);
         System.out.println("Escriba Sexo");
         String gender = data.next();
         System.out.println("Escriba altura");
         int c = data.nextInt();
         //System.out.println(gender);
// sale del programa
         if(gender.equalsIgnoreCase ('m')){
                System.out.println("Peso ideal es " + (c - 110));
}
           else if(gender.equals ("f") || gender.equals ("F")){
                   System.out.println("Peso ideal es " + (c - 120));
}
   
     }
}
