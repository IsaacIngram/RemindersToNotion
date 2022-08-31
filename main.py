from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv('vars.env')



NOTION_TOKEN = os.getenv('TOKEN')
DATABASE_ID = os.getenv('DATABASE')

notion = Client(auth=NOTION_TOKEN)

this_folder = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(this_folder, 'output.txt')

with open(file) as imp:
    lines = imp.readlines()

print("Transferring reminders...")

for line in lines:
    new_page = {
        "Name": {"title": [{"text": {"content": line.replace("\n", "")}}]},
    }
    notion.pages.create(parent={"database_id": DATABASE_ID}, properties=new_page)

with open("output.txt", 'w') as imp:
    imp.writelines('')
    
print("Complete")