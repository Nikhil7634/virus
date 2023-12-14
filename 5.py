from random import randint
if __name__ == '__main__':
    P = 23
    G = 9
    print('The Value of P is: %d' % P)
    print('The Value of G is: %d' % G)
    a = 4
    print('Secret Number for Alice is: %d' % a)
    x = pow(G, a, P)
    b = 6
    print('Secret Number for Bob is: %d' % b)
    y = pow(G, b, P)
    ka = pow(y, a, P)
    kb = pow(x, b, P)
    print('Secret Key for Alice is: %d' % ka)
    print('Secret Key for Bob is: %d' % kb)
