import PyPDF2
import json

pdf_file = open('Timetable_Karnataka.pdf', 'rb')
pdf_file_reader  = PyPDF2.PdfReader(pdf_file)

matching_lines = []

number_of_pages = len(pdf_file_reader.pages)

for page_num in range(number_of_pages):
    page = pdf_file_reader.pages[page_num]
    page_text = page.extract_text()
    
    lines = page_text.split('\n')
    for line in lines:
        if "kalaburagi" in line.lower():
            matching_lines.append(line)


pdf_file.close()

   

schedule = []

for line in matching_lines:
    data = line.split(' ')
    timings = data[3:] 
    temp_data = {"from": data[0],
                 "to": data[1],
                 "frequency": data[2],
                 "timing": timings
                 }
    schedule.append(temp_data)

output_filename = 'schedule.json'

with open(output_filename, 'w') as json_file: 
    json.dump(schedule, json_file, indent=4)