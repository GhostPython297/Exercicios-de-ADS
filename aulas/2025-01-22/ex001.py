## ímpar par ou roubo
## ainda não foi finalizado

entrada = input()

p, j1, j2, r, a = map(int, entrada.split(" "))

escolha_jogador = p
numero_escolhido001 = j1
numero_escolhido002 = j2
roubou = bool(r)
acusado = bool(a)
resultado = 1 if (numero_escolhido001 + numero_escolhido002) % 2 == 0 else 0

vitoria001 = roubou and not acusado
vitoria002 = not roubou and acusado and resultado == escolha_jogador
vitoria003 = not roubou and not acusado and escolha_jogador == resultado
vitoria = vitoria001 or vitoria002 or vitoria003

ganhador = 1 if vitoria else 2

print(f"Jogador {ganhador} ganha!")