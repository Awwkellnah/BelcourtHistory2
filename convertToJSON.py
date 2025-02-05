import pandas as pd

csv_file = "movies2.csv"  # Replace with your actual file path

# Read CSV with ISO-8859-1 encoding
df = pd.read_csv(csv_file, encoding="ISO-8859-1")

# Save as JSON
df.to_json("movies6.json", orient="records", indent=4)

print("Conversion complete!")
