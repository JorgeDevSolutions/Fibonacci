def pertence_a_fibonacci(n):
    # Inicializamos os primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Continuamos gerando números da sequência até que 'b' seja maior ou igual a 'n'
    while b < n:
        a, b = b, a + b
    
    # Verificamos se o número informado está na sequência
    if b == n or n == 0:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Loop principal para tentar novos números
while True:

    # Entrada do usuário
    numero = int(input("Informe um número: "))
    print(pertence_a_fibonacci(numero))

    # Pergunta se o usuário deseja tentar novamente
    resposta = input("Deseja tentar outro número? (s/n): ").strip().lower()
    if resposta != 's':
        print("Programa encerrado.")
        break