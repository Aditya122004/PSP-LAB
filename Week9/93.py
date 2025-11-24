old = {
    5: {"item1": 100, "item2": 200, "item3": 300},
    12: {"item4": 500, "item5": 600},
    18: {"item6": 1000}
}

new = {
    5: {"item1": 110, "item2": 210, "item3": 310},
    12: {"item4": 550, "item5": 540},
    18: {"item6": 1200}
}

impact = {}

for gst in old:
    impact[gst] = {}
    for item in old[gst]:
        old_price = old[gst][item]
        new_price = new[gst][item]
        old_total = old_price + (old_price * gst / 100)
        new_total = new_price + (new_price * gst / 100)
        diff = round(new_total - old_total, 2)
        impact[gst][item] = diff

print("=== Buyer Impact After GST ===")
for gst in impact:
    print(f"\nGST {gst}%:")
    for item in impact[gst]:
        value = impact[gst][item]
        status = "Loss" if value > 0 else "Profit" if value < 0 else "No Change"
        print(f"  {item}: {abs(value)} ({status})")
