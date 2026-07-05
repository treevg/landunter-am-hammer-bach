import csv
import os

INPUT_FILE = "viersen_weather_2006_2026.csv"
OUTPUT_FILE = "viersen_precipitation_2006_2026.csv"

def extract_precipitation():
    print(f"Extracting precipitation data from {INPUT_FILE}...")
    
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} does not exist.")
        return
        
    records_written = 0
    
    with open(INPUT_FILE, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        
        # Read the header row to find column indices
        headers = next(reader)
        try:
            year_idx = headers.index("year")
            month_idx = headers.index("month")
            day_idx = headers.index("day")
            prcp_idx = headers.index("prcp")
        except ValueError as e:
            print(f"Error: Could not find required columns in input file. {e}")
            return
            
        with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            # Write new header
            writer.writerow(["date", "precipitation_mm"])
            
            for row in reader:
                if not row or len(row) <= max(year_idx, month_idx, day_idx, prcp_idx):
                    continue
                    
                year = row[year_idx]
                month = row[month_idx]
                day = row[day_idx]
                prcp = row[prcp_idx]
                
                # Format date as YYYY-MM-DD
                try:
                    formatted_date = f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
                except ValueError:
                    # Skip rows that don't have valid numeric date parts
                    continue
                
                writer.writerow([formatted_date, prcp])
                records_written += 1
                
    print("\n" + "="*50)
    print("Extraction complete!")
    print(f"Total rows extracted: {records_written}")
    print(f"File saved to: {os.path.abspath(OUTPUT_FILE)}")
    print("="*50)

if __name__ == "__main__":
    extract_precipitation()
