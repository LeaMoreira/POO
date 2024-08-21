public class Matematica {
    // metodo para multiplicar
    public int multiplicar(int a, int b){
        return a*b;
    }

    // metodo para multiplicar sobrecargado
    public int multiplicar(int a, int b, int c){
        return a*b*c;
    }

    public static void main(String[] args){
        Matematica math = new Matematica();

        // llamamos al metodo con dos parametros a y b
        int resultado_1 = math.multiplicar(15, 30);
        System.out.println("Resultado de 1er multiplicacion: "+resultado_1);
        // llamamos al metodo con tre parametros a, b y c
        int resultado_2 = math.multiplicar(20, 5, 10);
        System.out.println("Resultado 2da multiplicacion: "+resultado_2);

    }
}
