import pandas as pd
import re

# Load the Excel file
file_path = "2025.xlsx"  # Update this path if needed
sheet_name = "GrossRevenueByEvent"

# Read the sheet
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

# Initialize result list
event_data = []
current_event = None
event_dates = []

# Function to check if a string is a valid date
def is_date(value):
    return bool(re.match(r"\d{2}/\d{2}/\d{4}", str(value).strip()))

# Iterate through rows
for _, row in df.iterrows():
    cell_value = str(row[0]).strip()
    
    # If we hit "Event Date", assume the previous row was an event title
    if cell_value == "Event Date" and current_event is None:
        current_event = str(df.iloc[_ - 1, 0]).strip()
        event_dates = []
    
    # If we hit a date, store it
    elif is_date(cell_value):
        event_dates.append(cell_value)
    
    # If we hit a total row (often contains "Total"), save and reset
    elif "Total" in cell_value and current_event:
        if event_dates:
            event_data.append([current_event, min(event_dates), max(event_dates)])
        current_event = None
        event_dates = []

# Save the last event's dates
if current_event and event_dates:
    event_data.append([current_event, min(event_dates), max(event_dates)])

# Create a DataFrame with results
result_df = pd.DataFrame(event_data, columns=["Event Title", "First Date", "Last Date"])

# Save to a new Excel file
output_file = "processed_events2025.xlsx"
result_df.to_excel(output_file, index=False)

print(f"Processed file saved as {output_file}")
