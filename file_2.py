import os
import csv

# Folder jahan 80 companies ki txt files hain
folder_path = "tech_data"

# Output file
output_file = "tech_companies_dataset.csv"

# CSV create
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Header
    writer.writerow(["Company", "Summary"])

    count = 0

    # Files read
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()

                # company name clean
                company_name = file_name.replace(".txt", "").replace("_", " ")

                # skip empty files
                if content:
                    writer.writerow([company_name, content])
                    count += 1

            except Exception as e:
                print(f"❌ Error in {file_name}: {e}")

print(f"✅ DONE! Merged files: {count}")