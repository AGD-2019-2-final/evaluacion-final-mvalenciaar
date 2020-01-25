import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

    for line in sys.stdin:
        line = line.replace ('\n', '')
        line = line.replace ('\t', '')
        line = line.replace ('\r', '')
        col = line.split(' ')
        col = [x for x in col if x != '']
        #print(col)
        key = col[0] + col[2].rjust(5,'0')
        #key = str(key)

        sys.stdout.write("{}---{}\n".format(key, line))
