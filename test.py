
ne_prastevila = []
for i in range(1, 300):
    t = i ** (1 / 2)
    j = 1
    while j <= t:
        if i % j == 0:
            ne_prastevila.append(i)
        j += 1

for i in range(2, 300):         
    if not i in ne_prastevila:
        print(i)

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        
