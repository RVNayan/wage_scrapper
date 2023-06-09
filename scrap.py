import requests
from bs4 import BeautifulSoup
import json

def get_table_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    table = soup.find('table')
    heading1 = table.find('tr').text.strip()    
    
    contents = []
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text.strip())
        if row_data:
            contents.append(row_data)

    
    return contents,heading1

company_name = input("Enter the company name: ")
url = f"http://www.levels.fyi/companies/{company_name}/salaries/software-engineer/"


table_headings = get_table_contents(url)[1]
table_contents = get_table_contents(url)[0]

print(f"The average median fresher salary at {company_name} is",table_contents[0][1])

#json_data = json.dumps(table_contents, indent=4)
#print(json_data)


