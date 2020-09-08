"""
Sätt ihop ett program (skript) som skriver en hälsningsfras och sedan räknar ut arean på en cirkulär
bottenplatta, och volymen av en cylinder och en kon med den bottenplattan hjälp av inmatad data
och era funktioner. Programmet ska göra följande:
1. Skriva ut Hello i terminalen
2. Fråga efter användarens namn
3. Fråga efter cirkelradien
4. Skriva ut hur stor namngiven användares cirkel är.
5. Fråga efter höjden på cylinder/kon.
6. Skriva ut hur stor namngiven användares cylinder och kon blir.
"""


def area(radie):
    return (radie ** 2) * 3.141592


def volume_cylinder(area, height):
    return area * height


def volume_cone(area, height):
    return volume_cylinder(area, height) / 3


def print_volume(name, volume_name, volume):
    print(
        name
        + "s "
        + volume_name
        + " rymmer "
        + str(volume)
        + " kubikcm, eller "
        + str(volume / 1000)
        + " kubikdm(liter)."
    )


print("Hello")

name = input("Vem är du? ")

radius = float(input("Hur stor är radien på din cirkulära bottenplatta (cm)? "))

area = area(radius)

print("Arean av " + name + " bottenplattan är " + str(area) + " kvadratcm")

height = float(input("Hur hög ska konen och cylindern vara (cm)? "))
print_volume(name, "kon", volume_cone(area, height))
print_volume(name, "cylinder", volume_cylinder(area, height))
