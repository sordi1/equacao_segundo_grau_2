import cmath  # Para lidar com raízes complexas

def resolver_equacao_quadratica(a, b, c):
    # Calculando o discriminante
    delta = b**2 - 4*a*c
    
    # Calculando as raízes
    if delta > 0:
        # Duas raízes reais e diferentes
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        # Uma raiz real (duas iguais)
        x1 = -b / (2 * a)
        return x1,
    else:
        # Raízes complexas
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(-delta) / (2 * a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

# Entrada de dados
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Verifica se 'a' é diferente de zero
if a == 0:
    print("O valor de 'a' não pode ser zero em uma equação quadrática.")
else:
    # Calcula as raízes
    solucoes = resolver_equacao_quadratica(a, b, c)
    
    # Exibe as soluções
    if len(solucoes) == 2:
        print(f"As raízes da equação são: x1 = {solucoes[0]} e x2 = {solucoes[1]}")
    elif len(solucoes) == 1:
        print(f"A raiz da equação é: x1 = {solucoes[0]}")
    else:
        print(f"As raízes complexas da equação são: {solucoes[0]} e {solucoes[1]}")
