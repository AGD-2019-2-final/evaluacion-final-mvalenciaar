import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
      for line in sys.stdin:
          cantidad_registros = line.split(',')[2]
          sys.stdout.write("{}\t1\n".format(cantidad_registros))
