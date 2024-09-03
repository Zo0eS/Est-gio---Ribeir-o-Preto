# =======================================================================================================================

# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

termo1 = 0
termo2 = 1
termo3= 0

print('-' * 42)
print('' * 3, 'verificar a sequencia de finonacci')  
print('-' * 42)

valor = int(input('digite um numero: '))

if valor == 0 or valor == 1:
    print('o numero faz parte da sequencia de fibonacci.')
else:
    while termo3 < valor :
        termo3 = termo1 + termo2
        termo1 = termo2
        termo2 = termo3

    if valor == termo3:
        print('O número faz parte da sequência de Fibonacci.')
    else:
        print('O número digitado não faz parte da sequência de Fibonacci.')



# =======================================================================================================================


        # 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

   def contando_letra_A(string):
    s_lower = string.lower()
    count = s_lower.count('a')
    return count

def main():
    string = input("Digite uma string para verificar a quantidade de letras 'a': ")
    count = contando_letra_A(string)
    
    if count > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

if __name__ == "__main__":
    main()


# =======================================================================================================================


# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)

# Ao final do processamento, qual será o valor da variável SOMA?
# RESPOSTA: A soma deu 77


# =======================================================================================================================


# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, 9 
# b) 2, 4, 8, 16, 32, 64, 128 
# c) 0, 1, 4, 9, 16, 25, 36, 64 
# d) 4, 16, 36, 64, 100
# e) 1, 1, 2, 3, 5, 8, 13
# f) 2,10, 12, 16, 17, 18, 19, 200

# =======================================================================================================================

# 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

# RESPOSTA:

# usarei três lâmpadas
# L1, L2 e L3

# Primeiro passo:
# Ligarei o interruptor 
# L1
# ​
#   e deixaria ligado por um tempo suficiente (por exemplo, 15 minutos).
# Após esse tempo, desligarei o interruptor L1 e ligarei o interruptor L2.
# Deixando o interruptor L2 ligado e mantendo o interruptor L3 desligado.

# logo depois eu iria até as salas onde as lâmpadas estão localizadas e observando as lâmpadas
# chegaria nas seguintes conclusoes:

# Lâmpada 1 (Quente e Ligada): Esta lâmpada está acesa e quente. Ela é controlada pelo interruptor da
# L2, que está ligado no momento da minha visita.

# Lâmpada 2 (Quente e Desligada): Esta lâmpada está apagada, mas quente ao toque. Ela foi ligada pelo interruptor da L1 antes de eu ter desligado L1 .

# Lâmpada 3 (Fria e Desligada): Esta lâmpada está apagada e fria. Ela é controlada pelo interruptor da
# L3, que nunca foi ligado.

