#!/usr/bin/java --source 11
import java.util.Random;
import java.util.Scanner;

public class Game{
    public static void main(String[] args)
    {
        Scanner data = new Scanner(System.in);
        String[] strArr = {"T", "L", "P"};
        String[] strArr1 = {"T", "L", "P"};
        String replay = "";
        Random opt = new Random();
    do{
        int choice = opt.nextInt(strArr.length);
        int choice1 = opt.nextInt(strArr1.length);
        
        System.out.println("Jugador elige: " + (strArr[choice]));
        System.out.println("Maquina elige: " + (strArr1[choice1]));
        if (choice == 0 && choice1 == 1){
               System.out.println("Gana Jugador");
           }
           else if(choice == 1 && choice1 == 2){
                   System.out.println("Gana Jugador");   
                  }
                  else if(choice == 2 && choice1 == 0){
                             System.out.println("Gana Jugador");

                         }
                         else if(choice == choice1){
        
                            System.out.println("Empate");
                                }
                                else{
                                  System.out.println("Gana Maquina");
                              }
       System.out.println("Volver  A Jugar y/n ?");
       replay = data.next();
}while(replay.equals ("y"));
           
    }
}
