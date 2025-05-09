import pandas as pd
from fpdf import FPDF

# Read data
df = pd.read_csv('sales_data.csv')
total_sales = df['Sales'].sum()
avg_sales = df['Sales'].mean()

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')
pdf.cell(200, 10, txt=f"Total Sales: ${total_sales:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Average Sales: ${avg_sales:.2f}", ln=True)
pdf.output("sales_report.pdf")
