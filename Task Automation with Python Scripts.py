import re

# Input and output file paths
input_file = "sample.txt"
output_file = "extracted_emails.txt"

# Read contents from the input file
with open(input_file, "r") as file:
    content = file.read()

# Regular expression to extract email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, content)

# Write emails to the output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print(f"✅ {len(emails)} email(s) extracted and saved to '{output_file}'")
