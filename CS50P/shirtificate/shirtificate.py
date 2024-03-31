from fpdf import FPDF

user_input = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4" )
pdf.add_page()
pdf.rect(15, 15, 210-30, 297-30)
#pdf.add_font("Datalegreya-Thin", "", "Datalegreya-Thin.otf")
#pdf.set_font("Datalegreya-Thin", "", 40)
pdf.set_font("helvetica", "B", 40)
pdf.set_xy(50, 30)
pdf.write(40, "CS50 Shirtificate")

#image
pdf.image("shirtificate.png", 25, 70, 160, 160)

#second text
#pdf.add_font("Datalegreya-Thin", "", "Datalegreya-Thin.otf")
pdf.set_text_color(255, 255, 255)
#pdf.set_font("Datalegreya-Thin", "", 25)
pdf.set_font("helvetica", "B", 20)
pdf.set_xy(58, 105)
pdf.write(30, user_input + " took CS50")

#save
pdf.output("shirtificate.pdf")
