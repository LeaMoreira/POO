public class Main_Eje5 {
    public static void main (String[] args){

        // Aplicamos polimorfismo con la variable mi animal
        Animal miAnimal;

        // miAnimal ahora sera un perro
        miAnimal = new Perro2();
        miAnimal.hacerSonido();

        // miAnimal ahora sera un gato
        miAnimal = new Gato();
        miAnimal.hacerSonido();

        // probando la lista en java
        Animal[] animals = {new Perro2(), new Gato()
        };

        // probando el bucle for java
        for (Animal animal: animals){
            animal.hacerSonido();
        }
    }
}
