public class cuentaBancaria {

    // atributos
    private double saldo;
    private String titular; // aca declaramos que el titular solo puede ser asignado una vez en le constructor
                            // y luego ya no podra ser cambiado

    // constructor
    public cuentaBancaria(String titular, double saldoInicial){
        this.titular = titular;
        if (saldoInicial >= 0){
            this.saldo = saldoInicial;
        } else {
            this.saldo = 0;
        }
    }

    // metodos
        // depositar
    public void depositar(double monto){
        if (monto > 0) {
            saldo += monto;
            System.out.println("Se deposito un total de $" +monto+ " saldo actual de $" +saldo);
        }
        else{
            System.out.println("el monto a depositar debe ser mayor a $0");
        }
    }
        // retirar efectivo
    public void retirar(double monto){
        if (monto > 0 && monto <= saldo){
            saldo -= monto;
            System.out.println("monto a retirar de $" +monto+ " saldo actual de $" +saldo);
        }
        else{
            System.out.println("el monto a retirar excede el saldo disponible de $" +saldo);
        }
    }

        // consultar saldo
    public double consultarSaldo(){
        return saldo;
    }

        // obtener titular
    public String getTitular(){
        return titular;
    }
}
