//package utp.misiontic2022.c2.mundo;

import java.util.Scanner;

public class Sistema_De_inversion {
    int pTiempo = 0;
    double pCapital = 0;
    double pIntereses  = 0 ;
    // VARIABLES

    // Constructor
    public Sistema_De_inversion(int tiempo, double capital, double interes) {
    pTiempo = tiempo;
    pCapital = capital;
    pIntereses = interes;
    }
    //METODOS
    public double intereSimple() {
        return (Math.round(pCapital * (pIntereses/100)* pTiempo));
    }
    public double interesCompuesto() {
        return (Math.round(pCapital * (1 + Math.pow(pIntereses/100, pTiempo)) - 1));
    }
    public double diferenciaInteres() {
        return (interesCompuesto() - intereSimple());
        }
    public String compararInversion() {
        if (intereSimple() ==  0 || interesCompuesto() == 0 ){
            return ("Faltan datos para calcular la diferencia en el total de intereses generados para el proyecto.");
        }
        else {
    return ("El interés simple es: " + intereSimple() + ", el interés compuesto es: " + interesCompuesto() + ", La diferencia en el total de intereses generados para el proyecto, si escogemos entre evaluarlo a una tasa de interés Compuesto y evaluarlo a una tasa de interés Simple, asciende a la cifra de: $" + diferenciaInteres());
        }
    }

    public static void main(String[] args){
        // WRAP VARIABLES
        Scanner sc = new Scanner(System.in);
        Integer tiempo = sc.nextInt();
        Double capital = sc.nextDouble();
        Double interes = sc.nextDouble();

        Sistema_De_inversion app = new Sistema_De_inversion(tiempo , capital, interes);
        System.out.println(app.compararInversion());
        System.out.println(app.intereSimple());
        System.out.println(app.interesCompuesto());
        }
}













        /*Scanner sc = new Scanner(System.in);.useDelimiter("\n");
        try {int tiempo = Integer.parseInt(sc.next());
            double capital = Double.parseDouble sc.nextDouble();
        double interes = Double.parseDouble(sc.next());

        Sistema_De_inversion test= new Sistema_De_inversion(tiempo, capital, interes);

        double int_s = Math.round(test.pCapital * (test.pIntereses/100)* test.pTiempo);
        double int_c = Math.round(test.pCapital * (1 + Math.pow(test.pIntereses/100, test.pTiempo)) - 1);
        double dif_int = Math.round(int_c - int_s);
        String compararInversion = "El interés simple es: " + int_s + ", el interés compuesto es: " + int_c + ", La diferencia en el total de intereses generados para el proyecto, si escogemos entre evaluarlo a una tasa de interés Compuesto y evaluarlo a una tasa de interés Simple, asciende a la cifra de: $" + dif_int;
        System.out.println(compararInversion);
    }
        catch(Exception e){
            System.out.println("Faltan datos para calcular la diferencia en el total de intereses generados para el proyecto.");
            }
        }
        }*/
