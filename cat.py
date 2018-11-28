import sys

if len(sys.argv) != 2:
  sys.stderr.write('to run with one arguments\n')
  exit()
try:
  fh = open(sys.argv[1],"r")
except FileNotFoundError:
  sys.stderr.write(sys.argv[1] + ' not exists \n')
  exit()
fe = open("upper","w")
line = fh.readline().strip()
while line:
  if line.isupper():
   fe.write(line + '\n')
  if line.isnumeric():
   print("El numero es: " + str(line))
  else:
   print("Caracter no numerico.")#Con esto te dice que los otros campos que hay no contienen 	numeros.
  line = fh.readline().strip()
fh.close()
fe.close()
print("Los que no se admiten como numero se han guardado en la carpeta upper")
