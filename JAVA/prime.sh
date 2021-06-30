#!/usr/bin/java --source 11
import java.util.Scanner;

 public class Prime{
 public static void main(String[] args){
     int p = 0;
     Scanner data = new Scanner(System.in);
     String options = "";
     
 do{
     System.out.println("Digite número");
     int n = data.nextInt();
     for (int i = 1; i <= n; i++){
            if (n % i == 0){
              p++;      
                }
         }
     if (p == 2 || p != 2){
            System.out.println("Otro Numero?");
            options = data.next();   
        }
}while(options.equals ("y"));
     
  
}
}
