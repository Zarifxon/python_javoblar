# tartibla

alifbe = []
print("Harflarni kiriting: ")
for n in range(26):
    alifbe.append(input(f"{n+1} - harfni kiriting:"))
    print("Alifbe harflari quyidagicha: ",  sorted(alifbe), end=' ')
  