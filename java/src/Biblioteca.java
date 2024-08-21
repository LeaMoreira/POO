public class Biblioteca {
    private String nombre;
    private Bibliotecario bibliotecario;

    public Biblioteca( String nombre, Bibliotecario bibliotecario){
        this.nombre = nombre;
        this.bibliotecario = bibliotecario;
    }

    // metodo
    public void mostrarBibliotecario(){
        System.out.println("Bibliotecario: "+bibliotecario.getNombre());
    }
}
