public class Main_Eje3 {
    public static void main(String[] args){
        // creamos cuenta bancaria con el titular y el saldo
        cuentaBancaria cuenta1 = new cuentaBancaria("Leandro", 30000);

        // consultamos saldo inicial y mostramos el nombre el titular
        System.out.println("Titular de la cuenta: " +cuenta1.getTitular());
        System.out.println("saldo inicial de $" +cuenta1.consultarSaldo());

        // operaciones bancarias
        cuenta1.depositar(10000);
        cuenta1.retirar(7500);
        cuenta1.retirar(5000);
    }
}
