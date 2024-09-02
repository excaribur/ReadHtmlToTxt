from bs4 import BeautifulSoup
from datetime import datetime

# Read the HTML file
with open('room.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <p> tags
p_tags = soup.find_all('p')

# Extract text from each <p> tag
text_lines = [p.get_text(strip=True) for p in p_tags]

# Generate a filename with current date and time
now = datetime.now()
filename = f'extracted_text_{now.strftime("%Y%m%d_%H%M%S")}.txt'

# Write the extracted text to the file
with open(filename, 'w', encoding='utf-8') as file:
    for line in text_lines:
        file.write(line + '\n')

print(f"Text has been saved to {filename}")
