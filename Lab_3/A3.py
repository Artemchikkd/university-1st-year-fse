previous = int(input())
current = int(input())

if current >= previous:
    used = current - previous
else:
    used = 10000 - previous + current

if used <= 300:
    price = 21
elif used <= 600:
    price = 21 + (used - 300) * 0.06
elif used <= 800:
    price = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    price = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

average = price / used

print("Предыдущее  Текущее  Использовано  К оплате  Ср. цена m^3")
print(f"{previous:10} {current:8} {used:13} {price:9.2f} {average:12.2f}")