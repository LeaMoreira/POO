public class Pagina {

    private int numero;
    private String contenido;

    public Pagina(int numero, String contenido){
        this.numero = numero;
        this.contenido = contenido;
    }

    // metodo para mostrar lo que hay en las paginas
    public void mostrarContenido(){
        System.out.println("Pagina "+numero+": "+contenido);
    }
}
