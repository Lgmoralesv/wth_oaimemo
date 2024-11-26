from os import strerror
#Crea un histograma a partir del texto encontrado en el archivo leído
srcname = input("Ingresa el nombre del archivo: ")

try:
    dirabc = {}
    
    for line in open(srcname, 'rt'):
        for ch in line:
            if not ch in (' ','\n','.'):
                if not dirabc.get(ch.lower(),False):
                    d1 = {ch.lower() : 1}
                    dirabc.update(d1)
                else:
                    v2 = dirabc.get(ch.lower())+1
                    d2 = {ch.lower() : v2}
                    dirabc.update(d2)
    for valor in sorted(dirabc):
        print(f"{valor} -> {dirabc[valor]}")
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)
