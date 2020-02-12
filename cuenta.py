class Cuenta:
    def __init__(self):
        self.saldo = 0

    def consultar(self):
        return self.saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            raise Exception ("No tenes fondos suficientes")

    def transferir(self, other, monto):
        self.retirar(monto)
        other.depositar(monto)

        #if self.saldo >= monto:
        #    other.saldo += monto
        #    self.saldo -= monto
        #else:
        #    raise Exception ("No tenes fondos suficientes")












## tests

nik = Cuenta()
assert nik.consultar() == 0, "Cuando creas la cuenta, debe arrancar en 0"

nik.depositar(800)
assert nik.consultar() == 800, "Nik necesita su primer sueldo"


nik.retirar(20)
assert nik.consultar() == 780, "Saco plata para birras"

try:
    nik.retirar(100000)
    assert False, "No deberia poder retirar plata que no tiene"
except Exception as e:
    pass


mel = Cuenta()

nik.transferir(mel, 200)

assert nik.consultar() == 580, "Deberia haberle retirado la plata"
assert mel.consultar() == 200, "Deberia haberle llegado a mel"
