import math
a=float(input())
b=float(input())
c=float(input())
d=float(input())
alpha=float(input())
gamma=float(input())
alpha=math.radians(alpha)
gamma=math.radians(gamma)
s=(a+b+c+d)/2
area=math.sqrt((s - a) * (s - b) * (s - c) * (s - d) - a * b * c * d * math.cos((alpha + gamma) / 2)**2)
print(round(area, 2))
