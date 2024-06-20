from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
   pdf.add_page()
   listing = pdf.page_no()

   # Set the header
   pdf.set_font(family="Times", style="B", size=12)
   pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=2, border=1)
   pdf.line(10, 22, 200, 22)


   # Set the footer
   pdf.ln(262)
   pdf.set_font(family="Times", style="I", size=8)
   pdf.cell(w=0, h=8, txt=f"{row['Topic']} ... {listing}", align="R", ln=1)

   # Set background lines
   x1, y1, x2, y2 = 10, 22, 200, 22

   for i in range(28):
      y1, y2 = y1+10, y2+10
      pdf.line(x1, y1, x2, y2)


   for i in range(row['Pages']-1):
      pdf.add_page()
      listing = pdf.page_no()

      # Set the footer
      pdf.ln(274)
      pdf.set_font(family="Times", style="I", size=8)
      pdf.cell(w=0, h=8, txt=f"{row['Topic']} ... {listing}", align="R", ln=1)

      # Set background lines
      x1, y1, x2, y2 = 10, 22, 200, 22

      for i in range(28):
         y1, y2 = y1 + 10, y2 + 10
         pdf.line(x1, y1, x2, y2)


pdf.output("output.pdf")