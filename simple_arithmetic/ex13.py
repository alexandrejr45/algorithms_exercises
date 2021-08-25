# Calcular a velocidade final de um automóvel

v_inicial = float(input("Velocidade inicial\n"))
accl = float(input("Aceleração\n"))
tempo = float(input("Tempo\n"))
v_final = v_inicial + accl * tempo

v_final = v_final / 3.6

print("Velocidade final: ", v_final)
