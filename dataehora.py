from datetime import date, datetime, timedelta

#data = date(2023, 7, 10)
#print(data)
#print(date.today())


#data_hora = datetime(2023, 7, 10)
#print(data_hora)
#print(datetime.today())

tipo_carro = "M"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(days=tempo_grande)
    print(f"\nO carro chegou: {data_atual} e ficará pronto às {data_estimada}")

print()
print(date.today() - timedelta(days=1))
print()
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())