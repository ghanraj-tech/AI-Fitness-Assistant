from fpdf import FPDF

def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="AI Fitness Report", ln=True, align="C")

    pdf.ln(10)

    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    file_path = "fitness_report.pdf"
    pdf.output(file_path)

    return file_path