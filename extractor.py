import PyPDF2

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

for line in matching_lines:
    print(line)
                      
