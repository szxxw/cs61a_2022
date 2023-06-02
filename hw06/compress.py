import os
import PyPDF2

# Define input and output file names
input_file = 'C:\\Users\\szx\加签\\Zixin_Shen_Undergraduate and Graduate Transcript.pdf'
output_file = 'C:\\Users\\szx\加签\\2张加签照片 姓名出生日期写在照片后\\Zixin_Shen_Undergraduate and Graduate Transcript.pdf'

# Define the maximum file size in bytes
max_file_size = 2000000  # 2 MB

# Define the maximum quality reduction percentage
max_quality_reduction = 10

# Define the initial compression level
compression_level = 1

while True:
    # Open the input PDF file
    with open(input_file, 'rb') as f_in:
        pdf_reader = PyPDF2.PdfReader(f_in)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add all pages of the PDF to the writer object
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[6])

        # Apply the current compression level to the content streams
        pdf_writer.compressContentStreams(compression_level)

        # Write the compressed PDF to the output file
        with open(output_file, 'wb') as f_out:
            pdf_writer.write(f_out)

    # Check the size of the compressed PDF
    compressed_size = os.path.getsize(output_file)

    # Check if the compressed file size is within the limit
    if compressed_size <= max_file_size:
        break

    # Check if the maximum quality reduction has been reached
    if compression_level >= max_quality_reduction:
        break

    # Increase the compression level
    compression_level += 1

# Print the final compression level and file size
print(f"Final compression level: {compression_level}")
print(f"Final file size: {compressed_size} bytes")
