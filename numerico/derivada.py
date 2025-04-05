class Derivada:
    def __init__(self, func, h=1e-7):
        """
        Inicializa a classe com a função e o valor de h (incremento pequeno).
        
        Parâmetros:
        - func: a função que se deseja derivar.
        - h: incremento para aproximar o limite.
        """
        self.func = func
        self.h = h

    def direita(self, x):
        """
        Calcula a derivada usando a diferença pela direita:
            f'(x) ≈ (f(x + h) - f(x)) / h
        """
        return (self.func(x + self.h) - self.func(x)) / self.h

    def esquerda(self, x):
        """
        Calcula a derivada usando a diferença pela esquerda:
            f'(x) ≈ (f(x) - f(x - h)) / h
        """
        return (self.func(x) - self.func(x - self.h)) / self.h

    def central(self, x):
        """
        Calcula a derivada usando a diferença central:
            f'(x) ≈ (f(x + h) - f(x - h)) / (2h)
        """
        return (self.func(x + self.h) - self.func(x - self.h)) / (2 * self.h)

