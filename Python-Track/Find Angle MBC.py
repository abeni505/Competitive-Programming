# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=float(input())
BC=float(input())


AC=math.sqrt(((AB**2)+(BC**2)))
theta_rad=math.atan(AB/BC)
theta_deg=math.degrees(theta_rad)

print(f'{round(theta_deg)}\N{Degree sign}')
