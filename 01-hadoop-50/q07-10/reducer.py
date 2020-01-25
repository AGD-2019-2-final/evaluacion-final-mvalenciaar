import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
import re
if __name__ == '__main__':

    for line in sys.stdin:
        line = line.replace ('\n', '')
        line = line.split('---')[1]


        #valor = re.sub('[\[\]]','',repr(valor))
        #valor = re.sub(r'[,.:@#?!&$]', '  ', valor)
        #valor = valor.strip('"\'')
        #valor = valor.replace("'","")
        #valor = valor.ljust(2, '1')

        sys.stdout.write("{}\n".format(line))
