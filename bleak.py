import asyncio
from bleak import Bleakscanner

async def scan_for_beacons():
    print("starting BLE device scan...")