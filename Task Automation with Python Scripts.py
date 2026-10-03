# Task 3 of internship which is assigned from Code Alpha Tech Industry
print("======Task Automation with Python Scripts===========")
import re
input_file = "source.txt"
output_file = "extracted_email.txt"

try:
    with open (input_file, "r", encoding="utf-8") as file:
        content = file.read()

    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"    
    emails = re.findall(email_pattern, content)

    unique_emails = sorted(list(set(emails)))
    with open(output_file, "w", encoding= "utf-8")as file:
        for email in unique_emails:
            file.write(email + "/n") 
    print(f"EXTRACTED E-MAILS are these: \n {unique_emails}")        
    print(f"Success! total {len(unique_emails)} extracted unique emails "
      f"{output_file} , saved") 
except FileNotFoundError:     
    print(f"{input_file} , firstly create any test file and also put some dummy "
          f"values in it.")