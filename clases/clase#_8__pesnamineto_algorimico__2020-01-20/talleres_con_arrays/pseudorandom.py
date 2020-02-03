""" 
m modulo 
a multiplicador
c incremento
X0 valor inicial
X valor
xn+1 = (axn + c) mod m
"""
class random():
        def __init__(self,valorInicial = 3, mod = 600 ,incrementador = 10,multiplicador = 7 ,veces=1):    
            self.valorInicial = valorInicial #valor  inicial para ir aumentandolo y disminuyendo
            self.mod = mod # tambien se pude usar como valor maximo
            self.incrementador = incrementador
            self.multiplicador = multiplicador
            self.veces = veces #veces para que salgan numeros "aleatorios" o tamaño del la lista 
            self.array = []
        def vector(self):
                self.contador = 0
                self.valor=self.valorInicial 
                while self.valor < self.mod and self.veces > self.contador:
	                self.valor = (self.multiplicador * self.valor + self.incrementador) % self.mod
	                self.contador += 1
	                self.array.append(self.valor)    
                return self.array
        def digito(self):
            self.digito = self.array[(self.multiplicador // self.valor + self.incrementador) % self.mod]
            return self.digito
        def help(self):
                print("PSEUDORANDOM \n formula \n m modulo \n a multiplicador \n c incremento \n X0 valor inicial \n X valor \n xn+1 = (axn + c) mod m")
                print("\n \n m>0 \n m>a>0 \n m>c>0")
#continuara despues
