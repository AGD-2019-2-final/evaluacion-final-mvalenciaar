import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
from operator import itemgetter
if __name__ == '__main__':

    curkey = None
    tupla = []


    for line in sys.stdin:
        key = line.split("\t")[1]
        val = line.rstrip().split("\t")[2]
        if key == curkey:
            tupla.append(val)
        else:
            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey, ','.join(tupla)))

                tupla = []
            curkey = key
            tupla.append(val)


    sys.stdout.write("{}\t{}\n".format(curkey, ','.join(tupla)))
