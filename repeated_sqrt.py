

file: <repeated_sqrt>

copyright (c) 2016 <Branden Sweetser>

license: MIT


from math import sqrt

for n in range(1, 60):

    r = 2.0

    if n > 51:

        n = 45

    for i in range(n):

        r = sqrt(r)

        for i in range(n):

            r = r**2

        print '%d times sqrt and **2: %16f' %(n, r)
