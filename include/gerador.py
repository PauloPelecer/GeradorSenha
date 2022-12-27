import random
import re
import base64


def play(password):
    a = re.sub('[aA]', 'B', password)
    b = re.sub('b', 'm', a)
    c = re.sub('[cC]', '6', b)
    d = re.sub('[dD]', 'j', c)
    e = re.sub('[eE]', 'a', d)
    f = re.sub('[fF]', 'n', e)
    g = re.sub('[gG]', 'l', f)
    h = re.sub('[hH]', '9', g)
    u = re.sub('[uU]', '3', h)
    v = re.sub('[vV]', 'f', u)
    p = re.sub('[pP]', 'g', v)
    q = re.sub('[qQ]', 'h', p)
    w = re.sub('[wW]', '8', q)
    y = re.sub('[yY]', '4', w)
    x = re.sub('[xX]', 'y', y)
    z = re.sub('[zZ]', '0', x)
    senha = '@'+ z + str(random.randint(1000,50000))
    return senha
    
