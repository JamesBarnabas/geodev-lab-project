import csv
def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))
def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row.get(column)
        if raw is None or str(raw).strip() == "":
            continue
        try:
            values.append(float(raw))
        except ValueError:
            continue
    return values
def summarize (values):
    if not values:
      return {"smallest": None, "largest": None,"average": None, "count": 0}
    if len(values) == 0:
       return {"Cannot compute statistics": "No valid numeric values found in the specified column."}
   
    return {"smallest": min(values), "largest": max(values), "count": len(values), "average": sum(values) / len(values)}

def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns: 
        values = clean_values(rows, column)
        report[column] = summarize(values)
    return report
report = summarise_all ("my_data.csv", ["area_1", "area_km2"])
                       
for column, stats in report.items():
    print (column, "->", stats)
