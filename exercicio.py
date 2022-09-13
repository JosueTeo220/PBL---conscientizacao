t_fumante = float(input("\nTempo como fumante (em anos).....: "))
v_maco =    float(input("Valor do maço....................: "))
q_maco =    float(input("Quantidade de maços por dia......: "))

montante = (t_fumante * 360) * (v_maco * q_maco)

if montante > 20000:
    print(f"\nCom o valor R$ {montante:.2f}, você poderia ter dado entrada em um carro.")
elif montante >= 20000 and montante <= 50000:
    print(f"\nCom o valor R$ {montante:.2f}, você poderia ter comprado um carro popular usado")
else:
    print(f"\nCom o valor R$ {montante:.2f}, você poderia ter comprado um carro zero")