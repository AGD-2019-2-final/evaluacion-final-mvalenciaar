import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    contador = 0
    for line in sys.stdin:
        if contador < 6:
            val, key, fecha, val = line.split("\t")
            val = int(val)

            sys.stdout.write("{}\t{}\t{}\n".format(key, fecha, val))
            contador += 1
