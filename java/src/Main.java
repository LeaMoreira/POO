// Programa principal
public class Main{
    public static void main(String[] args){
        // creamos el objeto de la clase comida
        class_Comidas pizza = new class_Comidas("pizza", 14800);

        // llamamos al metodo mostrarDetalles del objeto pizza
        pizza.mostrarAtributos();

        class_Comidas guiso = new class_Comidas( "guiso", 6500);

        guiso.mostrarAtributos();
    }
}