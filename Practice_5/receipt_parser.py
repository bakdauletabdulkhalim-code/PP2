import re
import os

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "raw.txt")

with open(file_path, "r", encoding="utf-8") as f:
    t = f.read()


p = [int(x.replace(" ", "").replace(",", "")) 
     for x in re.findall(r"Стоимость\s*\n\s*([\d\s]+,\d{2})", t)]


n = [m.splitlines()[0].strip() 
     for m in re.findall(r"\d+\.\s*(.+?)(?:\n\d+|$)", t, flags=re.DOTALL)]

total = sum(p)

dt = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})", t)
dt = dt.group(1) if dt else ""

pay = re.search(r"Банковская карта", t)
pay = pay.group(0) if pay else ""

for i in range(len(p)):
    print(f"{i+1}. {n[i]} — {p[i]}")

print(f"Total: {total} Tenge")
print(f"Date & Time: {dt}")
print(f"Payment Method: {pay}")