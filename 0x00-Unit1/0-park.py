#!/usr/bin/python3
if __name__ == '__main__':
    from calculator import mul, add, div
    from math import floor
    print('Welcome to the MINTICs park\n')
    # Read inputs
    # k = kids ad = adults
    k = int(input('Put kid(s) amount: '))
    ad = int(input('Put adult(s) amount: '))
    print('Your team is {} kid(s) and {} adult(s)\n'.format(k, ad))
    # Prices: kp = kids price ap = adults price
    kp = 9000
    ap = 15000
    a = k
    b = kp
    # Total amount
    tot = mul(a, b)
    print("Kids price is: ${}".format(mul(a, b)))
    a = ad
    b = ap
    tot1 = mul(a, b)
    print("Adults price is: ${}\n".format(mul(a, b)))
    a = tot
    b = tot1
    print('total price is: ${}'.format(add(a, b)))
    # Percentage discounts
    a = [float(30), float(45), float(25)]
    b = float(100)
    dscto = [div(a[0], b), div(a[1], b), div(a[2], b)]
    a = tot + tot1
    b = dscto
    print('Mainteance price is ${}, '.format(floor(mul(a, b[0]))),
          'Employes price is ${}, '.format(floor(mul(a, b[1]))),
          'Profits are ${}'.format(floor(mul(a, b[2]))))
