planilha = open("MIA.csv", "r")

print(planilha)
for linha in planilha:
    print(linha.split(","))



planilha.close()
