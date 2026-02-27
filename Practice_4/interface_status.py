import json


with open("Practice_4/sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)



print("Interface Status")
print("=" * 80)


print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")


print("-" * 80)



for element in data["imdata"]:

   
    attributes = element["l1PhysIf"]["attributes"]


    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")

    
    print(f"{dn:50} {description:20} {speed:8} {mtu:6}")

