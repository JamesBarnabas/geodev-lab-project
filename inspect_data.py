import csv
with open ("my_data.csv", encoding = "utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
print ("Number of rows:", len(rows))
print ("Columns:", list(rows[0].keys()))


import csv
with open("my_data.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
values =[]
for row in rows:
    value = float(row["area_1"])
    values.append(value)

print ("Smallest:", min(values))
print ("Largest:", max(values))
print ("Count:", len(values))



import csv
with open("my_data.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
values =[]
for row in rows:
    raw = row["area_1"].strip()
    if raw == "":
        continue
    values.append(float(raw))

print ("Smallest:", min(values))
print ("Largest:", max(values))
print ("Count:", len(values))


import csv

def inspect_column(filename, column):
  with open(filename, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

  values = []
  for row in rows:
    raw = row.get(column)

    if raw is None or str(raw).strip() == "":
      continue

    try:
      values.append(float(raw))
    except ValueError:
      continue

  if not values:
    return {"smallest": None, "largest": None, "count": 0}

  return {"smallest": min(values), "largest": max(values), "count": len(values), "average": sum(values) / len(values)}


result = inspect_column("my_data.csv", "area_1")
area_2_result = inspect_column("my_data.csv", "area_km2")

print(f"Result for area_1: {result}")
print(f"Result for area_km2: {area_2_result}")