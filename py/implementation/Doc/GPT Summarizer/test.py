import chardet

def get_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
        print(f"Detected encoding: {encoding} with {confidence*100}% confidence")
        return encoding

file_path = '/Users/yorca/projects/sdk_interaction/py/implementation/Doc/web_archive/privacy_docs3.0/AerServ_privacy.mhtml'
encoding = get_file_encoding(file_path)
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