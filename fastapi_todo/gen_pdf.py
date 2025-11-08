from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from fastapi.responses import FileResponse

def generate_pdf(content:, filename:="rapport.pdf"):
    c = canvas . Canvas ( filename , pagesize = A4 )
    c . setFont ("Helvetica-Bold", 16)
    c . drawString (50 , 800 , " étude de marché automatise")
    c . setFont ("Helvetica", 12)
    y = 780
    for line in content . split ('\n') :
        c . drawString (50 , y , line )
        y -= 15
    c . save ()
    return filename

@app.get("/ download_pdf ")
def download_pdf () :
    filename = generate_pdf (" Exemple de contenu ")
    return FileResponse ( filename , media_type =’ application /pdf ’, filename=" rapport .pdf")
