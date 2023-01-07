public class PainelFront {
    private String[] painelfront = new String[18];

    public void criaPainel(){
        for(int i = 0;i < 18;i++){
            painelfront[i] = String.valueOf(i);
        }
    }

    public void atualizaPainel(int indice, String letra){
        this.painelfront[indice] = letra;
    }

    public String[] getPainel(){
        return this.painelfront;
    }
}
