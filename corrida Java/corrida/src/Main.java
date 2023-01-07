import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Placar placar = new Placar(0,0,0);
        Painel painel = new Painel();
        PainelFront painelfront = new PainelFront();
        char check = ' ';
        int numero = 0;

        painel.criaPainel();
        painelfront.criaPainel();

        while(true){
            if(placar.getA() == 6 || placar.getB() == 6 || placar.getC() == 6){
                break;
            }
            System.out.println("ULTIMA LETRA TIRADA: "+check);
            for(String i : painelfront.getPainel()) {
                System.out.print(i + " ");
            }
            System.out.println("\nA: "+placar.getA());
            System.out.println("B: "+placar.getB());
            System.out.println("C: "+placar.getC());

            while(true) {
                System.out.print("Digite um numero: ");
                numero = sc.nextInt();
                if (numero < 0 || numero > 17) {
                    System.out.println("Digite um numero que esteja no painel");
                } else if (painel.getLetra(numero) == 'X') {
                    System.out.println("Digite um numero que nao foi escolhida");
                } else {
                    break;
                }
            }
            if(painel.getLetra(numero) == 'A'){
                painelfront.atualizaPainel(numero,"A");
                check = 'A';
                placar.atualizaPlacar('A');
            }else if(painel.getLetra(numero) == 'B'){
                painelfront.atualizaPainel(numero,"B");
                check = 'B';
                placar.atualizaPlacar('B');
            }else if(painel.getLetra(numero) == 'C') {
                painelfront.atualizaPainel(numero,"C");
                check = 'C';
                placar.atualizaPlacar('C');
            }
            painel.usaLetra(numero);
            System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
        }
        if(placar.getA() == 6){
            System.out.println("O vencedor da corrida foi: A");
        }else if(placar.getB() == 6){
            System.out.println("O vencedor da corrida foi: B");
        }else if(placar.getC() == 6){
            System.out.println("O vencedor da corrida foi: C");
        }



    }
}