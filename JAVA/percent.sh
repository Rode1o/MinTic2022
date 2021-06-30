#!/usr/bin/java --source 11
import java.util.Scanner;

public class Percentsal{
    public static void main(String[] args)
    {
        Scanner data = new Scanner(System.in);
        System.out.println("Nombre");
        String na = data.next();
        System.out.println("Salario");
        float sa = data.nextFloat();
        System.out.println("Edad");
        float ed = data.nextFloat();

        if (ed > 60){
               sa *= 1.15 ;
               System.out.println(sa);
           }
           else if (ed >= 51 && ed < 61 ){
                       sa *= 1.1;
                       System.out.println(sa);
                   }
                   else if (ed >= 19 && ed < 60){
                            sa *= 1.05;
                            System.out.println(sa);
                           }
                           else{
                            System.out.println("No puede trabajar");
                            }
          

        
    }
}
