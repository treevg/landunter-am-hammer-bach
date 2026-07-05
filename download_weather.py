import os
import urllib.request
import gzip
import csv
from io import TextIOWrapper

# Configuration
STATION_ID = "D5064"  # Viersen station ID from your URL
START_YEAR = 2006
END_YEAR = 2026
OUTPUT_FILE = "viersen_weather_2006_2026.csv"

def download_and_merge():
    print(f"Starting download for station {STATION_ID} ({START_YEAR} - {END_YEAR})...")
    
    records_written = 0
    years_processed = []
    header_written = False
    
    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        
        for year in range(START_YEAR, END_YEAR + 1):
            url = f"https://data.meteostat.net/daily/{year}/{STATION_ID}.csv.gz"
            print(f"Fetching data for year {year}... ", end="", flush=True)
            
            try:
                # Setup request with user-agent to avoid potential bot blocks
                req = urllib.request.Request(
                    url, 
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                )
                
                with urllib.request.urlopen(req) as response:
                    # Decompress gzip data
                    with gzip.GzipFile(fileobj=response) as gfile:
                        # Wrap in TextIOWrapper to read as text lines
                        text_file = TextIOWrapper(gfile, encoding='utf-8')
                        reader = csv.reader(text_file)
                        
                        year_records = 0
                        for row in reader:
                            if not row:
                                continue
                            
                            # Detect header row
                            if row[0] == "year" or row[0] == "date":
                                if not header_written:
                                    writer.writerow(row)
                                    header_written = True
                                continue
                            
                            writer.writerow(row)
                            year_records += 1
                        
                        print(f"Done! ({year_records} records added)")
                        records_written += year_records
                        years_processed.append(year)
                        
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print(f"Not found (HTTP 404). Data might not be available yet.")
                else:
                    print(f"Error: {e.reason} (HTTP {e.code})")
            except Exception as e:
                print(f"Error: {e}")
                
    print("\n" + "="*50)
    print("Process complete!")
    print(f"Successfully processed years: {years_processed}")
    print(f"Total weather records written: {records_written}")
    print(f"File saved to: {os.path.abspath(OUTPUT_FILE)}")
    print("="*50)

if __name__ == "__main__":
    download_and_merge()
