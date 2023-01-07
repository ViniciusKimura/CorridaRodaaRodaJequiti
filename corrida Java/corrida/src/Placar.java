public class Placar {
    private int a;
    private int b;
    private int c;

    public Placar(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public void atualizaPlacar(char letra){
        if(letra == 'A'){
            this.a = this.a + 1;
        } else if (letra == 'B') {
            this.b = this.b + 1;
        } else if (letra == 'C') {
            this.c = this.c + 1;
        }
    }

    public int getA()
    {
        return a;
    }
    public int getB()
    {
        return b;
    }
    public int getC()
    {
        return c;
    }
}
