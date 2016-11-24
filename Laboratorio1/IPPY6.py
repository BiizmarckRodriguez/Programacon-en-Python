##Carlos Bismarck Rodriguez Rodriguez
#Introduccion a la programacion en Python
#24/11/2016
#6
print( '===Calcular IMC - Masa corporal===')
peso = raw_input ('peso actual: ')
altura = raw_input ('altura actual: ')
imc = (float(peso)/(float(altura)*float(altura)))*10000

print 'Su IMC es : ', imc
if imc <16:
  raw_input ('Delgadez severa')
if imc <16.99 and imc >16:
  raw_input ('Delgadez moderada')
if imc <124.99 and imc >18.5:
  raw_input ('Normal')
if imc >25:
  raw_input ('Sobrepeso')
