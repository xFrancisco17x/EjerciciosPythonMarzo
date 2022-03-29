jornada = 48
hTrabajadas = int(input("¿Cuantas horas ha trabajado?"))
pagoHora = 2
pagoHoraExtra = 3.5

if hTrabajadas <= jornada:
    salario = hTrabajadas * pagoHora
else:
    salario = (jornada*pagoHora) + ((hTrabajadas-jornada)*pagoHoraExtra)

print("Su pago es de: ",salario)