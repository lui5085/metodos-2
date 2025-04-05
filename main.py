from numerico.derivada import Derivada
# Exemplo de uso:
if __name__ == "__main__":
    def f(x):
        return x**2

    deriv = Derivada(f, h=1e-7)
    
    x = 3.0
    
    deriv_direita = deriv.direita(x)
    deriv_esquerda = deriv.esquerda(x)
    deriv_central = deriv.central(x)
    
    valor_exato = 2 * x

    print("Derivada de f(x)=x² em x =", x)
    print("Usando a diferença pela direita:", deriv_direita)
    print("Usando a diferença pela esquerda:", deriv_esquerda)
    print("Usando a diferença central:", deriv_central)
    print("Valor exato da derivada:", valor_exato)