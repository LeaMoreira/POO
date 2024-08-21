public class class_Persona {
    // atributos
    String nombre;
    int edad;

    // constructor
    public class_Persona(String nombre, int edad){
        // iniciamos atributos
        this.nombre = nombre;
        this.edad = edad;
    }
    // metodos
    public void mostrarAtributos(){
        System.out.println("nombre: "+nombre);
        System.out.println("edad: "+edad);
    }
}
