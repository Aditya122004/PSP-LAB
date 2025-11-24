import json
import csv
import pickle

class AddressBook:

    def __init__(self):
        self.records = []

    def add_record(self, name, phone, dob, email):
        data = {
            "name": name,
            "phone": phone,
            "dob": dob,
            "email": email
        }
        self.records.append(data)

    def save_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self.records, f, indent=4)

    def save_csv(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "DOB", "Email"])
            for r in self.records:
                writer.writerow([r["name"], r["phone"], r["dob"], r["email"]])

    def save_binary(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.records, f)

    def search_in_binary(self, filename, key, value):
        with open(filename, "rb") as f:
            data = pickle.load(f)
        for record in data:
            if record.get(key) == value:
                return record  

        return None
