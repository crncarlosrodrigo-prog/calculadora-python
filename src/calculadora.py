def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de a e b."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de a e b."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de a por b. Lança erro se b for zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def potencia(a, b):
    """Retorna a elevado a b."""
    return a ** b
