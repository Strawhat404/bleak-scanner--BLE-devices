import asyncio
from bleak import BleakScanner

async def scan_for_beacons():
    print("starting BLE device scan...")
    devices = await BleakScanner.discover()
    print (f"Found {len(devices)} devices:\n")
    
    for device in devices:
        print(f"Name: {device.name}, Address: {device.address}, RSSI:{device.rrsi}")
        
        if "Beacon X Pro" in (device.name or ""):
            print(">> Detected Beacon X Pro W-6 device!")
            
def main():
    print("Initializing BLE Scanner")
    asyncio.run(scan_for_beacons())
    print("scanning completed.")
if __name__ == "__main__":
    
    main()