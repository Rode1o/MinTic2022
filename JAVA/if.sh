#!/usr/bin/java --source 11
import java.util.Scanner;

public class AvgClass{
    public static void main(String[] args)
    {
        Scanner data = new Scanner(System.in);
        System.out.println("Ingrese Nombre");
        String name = data.nextLine();
        float a = data.nextFloat();
        float b = data.nextFloat();
        float c = data.nextFloat();
        float p = ((a+b+c)/3);
        
        if (p > 3){
               System.out.println("Aprobado");
           }
           else{
            System.out.println("Reprobado");
            
        }
        
    }
}
