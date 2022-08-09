class Solution:
    def nineDivisors(self, N):
        c = 0
        lim = int( N ** 0.5)

        prime = [i for i in range(lim+1)]

        i = 2
        while i * i <= lim:
            if prime[i] == i:
                for j in range(i*i, lim + 1, i):
                    if prime[j] == j:
                        prime[j] = i

            i += 1

        for i in range(2, lim+1):
            p = prime[i]
            q = prime[i//prime[i]]

            if p*q == i and q!=1 and p!= q:
                c += 1

            elif prime[i] == i:
                if i**8 <= N:
                    c += 1

        return c