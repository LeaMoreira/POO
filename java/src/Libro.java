public class Libro {
    private String titulo;
    private String autor;
    private Pagina[] paginas;

    public Libro(String titulo, String autor, Pagina[] paginas){
        this.titulo = titulo;
        this.autor = autor;
        this.paginas = paginas;
    }

    // metodo para leer el libro
    public void leerLibro(){
        // bucle for para recorrer las paginas y leer su contenido
        for (Pagina pagina: paginas){
            pagina.mostrarContenido();
        }
    }
}
