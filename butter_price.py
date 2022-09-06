import subprocess

# subprocess.run(["clear"])

def for_one_butter(price, mass):
    price_for_one_g = int(price)/int(mass)
    return price_for_one_g

prices=[]
masses=[]
i=0
print("\nWelcome to the butter price calculator!\nPlease press Enter when you are done.")
while True:
    print(f"\nButter n.{i+1}")
    price=input(f"Price :\t")
    if price == "":
        break
    prices.append(int(price))
    mass=input("Mass  :\t")
    if mass == "":
        break
    masses.append(int(mass))
    i+=1

i=0
print("\nThe cost of 100 g. of")
for i in range(len(prices)):
    print(f"Butter n.{i+1} is {int(for_one_butter(prices[i], masses[i])*100)}")

print()
