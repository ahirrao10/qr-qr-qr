import requests
import json
import schedule
import time

def get_data_from_server():
    laptop_a_ip = "192.168.229.79"  # Replace with the actual IPv4 address of Laptop A
    url = f"http://{laptop_a_ip}:5000/input"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()

        with open("user_data_local.json", "w") as file:
            json.dump(data, file)

    except requests.RequestException as e:
        print(f"Error during request: {e}")

def job():
    print("Running job...")
    get_data_from_server()

# Run the job every 5 minutes
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)