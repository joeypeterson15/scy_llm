from fpdf import FPDF

def convert_text_to_pdf(input_filepath, output_filepath):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(input_filepath, "r", encoding="utf-8") as f:
        for line in f:
            # cell(width, height, txt, border, ln, align)
            # ln=1 moves the current position to the next line
            pdf.cell(0, 5, txt=line, ln=1)

    pdf.output(output_filepath)
    print(f"Successfully converted '{input_filepath}' to '{output_filepath}'")

# Run the conversion
convert_text_to_pdf("lorenipsum.txt", "converted_document.pdf")