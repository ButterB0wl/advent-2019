f = open('day1.txt', 'r')
masses = f.read().split()
print(masses)
fuels = [int(int(x)/3)-2 for x in masses]
print(fuels)
fuel_sum = sum(fuels)
print(fuel_sum)

for i, fuel in enumerate(fuels):
    remainder = fuels[i]
    total_fuel = fuels[i]
    while(remainder > 0):
        remainder = int(remainder/3)-2
        if remainder > 0:
            total_fuel += remainder
    fuels[i] = total_fuel

print(fuels)
print(sum(fuels))
