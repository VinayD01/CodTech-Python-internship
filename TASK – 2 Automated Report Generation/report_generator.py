from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import matplotlib.pyplot as plt

# ---------- READ DATA ----------
data_dict = {}

with open("data.txt", "r") as file:
    for line in file:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            data_dict[key.strip()] = value.strip()

name = data_dict["Name"]
course = data_dict["Course"]
semester = data_dict["Semester"]
cgpa = float(data_dict["CGPA"])
attendance = float(data_dict["Attendance"])

# ---------- CREATE CHART ----------
plt.bar(["CGPA (%)", "Attendance (%)"], [cgpa * 10, attendance])
plt.title("Performance Overview")
plt.ylabel("Value")
plt.savefig("chart.png")
plt.close()

# ---------- CREATE PDF ----------
pdf_file = "report.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 20)
c.drawCentredString(width / 2, height - 50, "Automated Student Report")

# ---------- TABLE ----------
table_data = [
    ["Field", "Value"],
    ["Name", name],
    ["Course", course],
    ["Semester", semester],
    ["CGPA", str(cgpa)],
    ["Attendance (%)", str(attendance)]
]

table = Table(table_data, colWidths=[200, 200])
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
    ("FONT", (0,0), (-1,0), "Helvetica-Bold")
]))

table.wrapOn(c, width, height)
table.drawOn(c, 80, height - 350)

# ---------- ADD CHART ----------
c.drawImage("chart.png", 150, 100, width=300, height=200)

# Footer
c.setFont("Helvetica-Oblique", 10)
c.drawCentredString(width / 2, 40, "Generated using Python, ReportLab & Matplotlib")

c.save()

print("Advanced PDF report generated successfully!")
