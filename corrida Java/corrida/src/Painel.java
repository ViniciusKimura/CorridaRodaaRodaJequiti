import java.util.Random;

public class Painel {
    private char[] painel = new char[18];

    public void criaPainel(){
        Random rand = new Random();
        int contA = 0, contB = 0, contC = 0, aleatorio = 0, cont = 0;
        while (contA != 6 || contB != 6 || contC != 6) {
            while(true)
            {
                aleatorio = rand.nextInt(3);
                if (aleatorio == 0 && contA < 6) {
                    this.painel[cont] = 'A';
                    contA += 1;
                    cont += 1;
                    break;
                } else if (aleatorio == 1 && contB < 6) {
                    this.painel[cont] = 'B';
                    contB += 1;
                    cont += 1;
                    break;
                } else if (aleatorio == 2 && contC < 6) {
                    this.painel[cont] = 'C';
                    contC += 1;
                    cont += 1;
                    break;
                }
            }
        }
    }

    public char getLetra(int indice){
        return this.painel[indice];
    }

    public void usaLetra(int indice){
        this.painel[indice] = 'X';
    }
}
