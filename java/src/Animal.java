public class Animal {

    // metodos
    public void hacerSonido(){
        System.out.println("Animal: Hacer Sonido ANIMAL");
    }
}

// subclase perro, que hereda el metodo de la super clase animal
class Perro extends Animal{

    // sobreEscribimos el metodo de la superClase Animal
    public void hacerSonido(){
        System.out.println("Perro: guau, guau");
    }
}