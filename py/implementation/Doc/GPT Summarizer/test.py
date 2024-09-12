import html2text

# Read HTML file
with open('/Users/yorca/projects/sdk_interaction/py/implementation/Doc/web_archive/privacy_docs3.0/Adobe App Measurement for Android_privacy1.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Convert HTML to Markdown
markdown_content = html2text.html2text(html_content)

# Write Markdown to output file
with open('output2.md', 'w', encoding='utf-8') as md_file:
    md_file.write(markdown_content)
#
# import PyPDF2
#
# # Path to your PDF file
# pdf_path = '/Users/yorca/Downloads/test.pdf'
#
# # Open the PDF file in binary read mode
# with open(pdf_path, 'rb') as file:
#     # Create a PDF reader object
#     reader = PyPDF2.PdfReader(file)
#
#     # Get the number of pages in the PDF
#     num_pages = len(reader.pages)
#
#     # Extract text from each page
#     pdf_text = ''
#     for page_num in range(num_pages):
#         page = reader.pages[page_num]
#         pdf_text += page.extract_text()
#
# # Print the extracted text
# print(pdf_text)


# import pandas as pd
#
# data = pd.read_csv("/Users/yorca/projects/sdk_interaction/google play scraper/app_metadata_topfree.csv")
#
# packge_set = set()
# for index, row in data.iterrows():
#     packge_set.add(row[0])
# print(len(packge_set))




# import chardet
#
# def get_file_encoding(file_path):
#     with open(file_path, 'rb') as f:
#         raw_data = f.read()
#         result = chardet.detect(raw_data)
#         encoding = result['encoding']
#         confidence = result['confidence']
#         print(f"Detected encoding: {encoding} with {confidence*100}% confidence")
#         return encoding
#
# file_path = '/Users/yorca/projects/sdk_interaction/py/implementation/Doc/web_archive/privacy_docs3.0/AerServ_privacy.mhtml'
# encoding = get_file_encoding(file_path)
#
# def convert_mhtml_ascii_to_utf8(input_file, output_file):
#     # Step 1: Open the MHTML file in ASCII encoding (as bytes).
#     with open(input_file, 'rb') as f:
#         # Step 2: Read the entire file in binary mode
#         ascii_content = f.read()
#
#     # Step 3: Decode the content using 'ascii' encoding to get a string
#     # You can also use 'latin-1' or 'iso-8859-1' if the content is not pure ASCII
#     decoded_content = ascii_content.decode('ascii', errors='ignore')
#
#     # Step 4: Encode the content into UTF-8
#     utf8_content = decoded_content.encode('utf-8')
#
#     # Step 5: Write the UTF-8 encoded content to the output file
#     with open(output_file, 'wb') as f:
#         f.write(utf8_content)
#
#     print(f"File has been converted to UTF-8 and saved as {output_file}")
#
#
# input_file = "/Users/yorca/projects/sdk_interaction/py/implementation/Doc/web_archive/privacy_docs3.0/AerServ_privacy.mhtml"
# output_file = "output_utf8.mhtml"
# convert_mhtml_ascii_to_utf8(input_file, output_file)