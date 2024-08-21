public class Main_Eje8 {
    public static void main (String[] args){
    // creamos varias paginas para que se pueda ejecutar luego el bucle de lectura
        Pagina[] paginas = {
                new Pagina(1, "Composición es una relación fuerte..."),
                new Pagina(2, "Agregación es una relación débil, porque... "),
                new Pagina(1, "Entonces podemos decir que la Relacion es...")
        };

        // creamos el libro con las paginas
        Libro libro = new Libro("POO","Gaston Plazas", paginas);

        // llamamos nuestro objeto libro para leerlo, y muestre lo que hay escrito en sus paginas
        libro.leerLibro();

        // creamos al bibliotecario
        Bibliotecario bibliotecario = new Bibliotecario("Leandro", 9632);

        // creamos la biblioteca
        Biblioteca biblioteca = new Biblioteca("Biblioteca Formosa", bibliotecario);

        // mostramos el nombre del bibliotecario y su asociacion con la biblioteca
        biblioteca.mostrarBibliotecario();
    }
}
