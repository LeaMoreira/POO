// creamos la clase abstracta con el comando abstract
abstract class figuraGeometrica {

    // aplicamos el metodo abstracto que se va implementar en la subclase
    public abstract double calcularArea();
}

// clase rectangulo que hereda de figura gemometrica

class Rectangulo extends figuraGeometrica{
    // ponemos los atributos en privado
    private double base;
    private double altura;

    // constructor de la clase
    public Rectangulo(double base, double altura){
        this.base = base;
        this.altura = altura;
    }
    // metodo abstracto de calcularArea
    public double calcularArea(){
        return base*altura;
    }
}
/*
Si bien hay 7 lineas bien realizadas y 2 con advertencia
es porque considera que al estar privado base y altura que las menciona
es porque seran sus valores finales a la hora de calcular el metodo
 */