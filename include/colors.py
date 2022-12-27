#MODULO DE CORES

def ColorSimple(ctx):
    colors = ['\033[0;31m','\033[0;32m','\033[0;33m', '\033[0;34m','\033[0;35m', '\033[0;36m', '\033[0;37m']
    if ctx == 'red':
        return colors[0]
    elif ctx == 'green':
        return colors[1]
    elif ctx == 'yellow':
        return colors[2]
    elif ctx == 'blue':
        return colors[3]
    elif ctx == 'purpple':
        return colors[4]
    elif ctx == 'cian':
        return colors[5]
    elif ctx == 'white':
        return colors[6]
        
        
if __name__ == '__main__':
    c1 = ColorSimple('purpple')
    c2 = ColorSimple('white')
    #print (c1,'m',c2)