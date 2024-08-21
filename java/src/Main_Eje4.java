public class Main_Eje4 {
    public static void main (String[] args){

        // con eso hacemos que la superClase animal haga su sonido
        Animal animal = new Animal();
        animal.hacerSonido();

        // con esto hacemos que la subClase perro haga su sonido
        Perro perro = new Perro();
        perro.hacerSonido();
    }
}
