from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def buat_pdf_chat(judul: str, isi: str, filename: str):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = [
        Paragraph(judul, styles["Title"]),
        Spacer(1, 12),
        Paragraph(isi.replace("\n", "<br/>"), styles["BodyText"]),
    ]

    doc.build(story)
    return filename