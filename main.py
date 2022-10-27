rfid = {
    "10053": "Devon Barker",
    "10054": "Henry Hunt",
    "10055": "Ravioli",
    "10056": "Billium",
}


scanning = True

people_in_building = []
while scanning:
    scanned_id = input()
    if scanned_id in people_in_building:
        people_in_building.remove(scanned_id)
        print(f"Good Bye, {rfid[scanned_id]}")
    else:
        people_in_building.append(scanned_id)
        print(f"Welcome, {rfid[scanned_id]}")
    for people in people_in_building:
        print(rfid[people])