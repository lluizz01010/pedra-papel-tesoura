import random


opcoes = ("pedra", "papel", "tesoura")

print("=== Pedra, Papel e Tesoura ===")

while True:
	try:
		total_rodadas = int(input("Quantas rodadas você quer jogar? "))
		if total_rodadas > 0:
			break
		print("Digite um número de rodadas maior que zero.")
	except ValueError:
		print("Digite um número inteiro válido.")

vitorias_jogador = 0
vitorias_computador = 0
empates = 0
rodada = 1

while rodada <= total_rodadas:
	print(f"\n--- Rodada {rodada}/{total_rodadas} ---")
	jogador = input("Escolha pedra, papel ou tesoura (ou 'sair'): ").strip().lower()

	if jogador == "sair":
		print("Até mais!")
		break

	if jogador not in opcoes:
		print("Opção inválida. Tente novamente.")
		continue

	computador = random.choice(opcoes)
	print(f"Computador escolheu: {computador}")

	if jogador == computador:
		print("Empate!")
		empates += 1
	elif (
		(jogador == "pedra" and computador == "tesoura")
		or (jogador == "papel" and computador == "pedra")
		or (jogador == "tesoura" and computador == "papel")
	):
		print("Você venceu!")
		vitorias_jogador += 1
	else:
		print("Você perdeu!")
		vitorias_computador += 1

	rodada += 1

else:
	print("\n=== Placar final ===")
	print(f"Você: {vitorias_jogador} vitória(s)")
	print(f"Computador: {vitorias_computador} vitória(s)")
	print(f"Empates: {empates}")
	if vitorias_jogador > vitorias_computador:
		print("Você venceu a partida!")
	elif vitorias_jogador < vitorias_computador:
		print("O computador venceu a partida!")
	else:
		print("A partida terminou empatada!")
