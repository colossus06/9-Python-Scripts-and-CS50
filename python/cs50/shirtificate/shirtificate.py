
from fpdf import FPDF

pdf = FPDF()

n= input("What's your name?")

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_font("helvetica", size=20, style="B")


pdf.add_page()
pdf.image("shirtificate.png", x=0, y=50)

pdf.cell(200, 10, txt="CS50 Shirtificate", align="C")
pdf.ln(110)

pdf.set_text_color(255, 255, 255)
pdf.cell(200, 10, txt="{}".format(n)+ " took CS50", align="C")
pdf.output("shirtificate.pdf")

