public class class_Comidas {
    // atributos de Comidas
    String nombre;
    double precio;

    // contructor de la clase comidas
    public class_Comidas(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }
    // metodos para mostrar los atributos
    public void mostrarAtributos(){
        System.out.println("nombre de la comida: "+nombre);
        System.out.println("precio: $"+precio);
    }
}


