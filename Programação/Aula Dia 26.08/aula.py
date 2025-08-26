class Cubo:
    def __init__(self,valor):
        self.x = valor
        print('Metodo Criado')
    
    def calcularCubo (self):
        cubo = self.x * self.x * self.x
        return f'Cubo calculado {cubo}'
    
cubo = Cubo(int(input('Digite um valor para calcular ao cubo: ')))
calculo = cubo.calcularCubo()
cubo2 = Cubo(30)
print(calculo)
