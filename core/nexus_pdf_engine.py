import os
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Registered PDF Standard: CORPORATE STEALTH v2.1 (NEXUS)
# This is the master layout reference for all Legal-DevOps documents.

class LayoutConfig:
    GRAPHITE   = colors.HexColor("#2B2B2B")
    STEEL_BLUE = colors.HexColor("#4A708B")
    MID_GRAY   = colors.HexColor("#64748B")
    LIGHT_BLUE = colors.HexColor("#F4F6F9")
    BORDER     = colors.HexColor("#CBD5E1")
    WHITE      = colors.white

    DEFAULT_QR_PATH = r"E:\Downloads\404\qrcode_master.png"

def setup_fonts():
    pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))

def get_standard_styles():
    st = getSampleStyleSheet()
    styles = {}
    styles['body'] = ParagraphStyle("Body", fontName="Arial", fontSize=10, leading=15, alignment=TA_JUSTIFY, spaceAfter=8)
    styles['body_bold'] = ParagraphStyle("BodyBold", parent=styles['body'], fontName="Arial-Bold")
    styles['h2'] = ParagraphStyle("H2", fontName="Arial-Bold", fontSize=11, textColor=LayoutConfig.STEEL_BLUE, spaceBefore=12, spaceAfter=4)
    styles['bullet'] = ParagraphStyle("Bullet", fontName="Arial", fontSize=10, leftIndent=15, leading=15, spaceAfter=6, alignment=TA_JUSTIFY)
    styles['title_center'] = ParagraphStyle("TitleCenter", fontName="Arial-Bold", fontSize=13, alignment=TA_CENTER)
    return styles

def create_nexus_document(output_path, doc_code, case_id, doc_title, sender_text, recipient_text, content_builder, qr_path=LayoutConfig.DEFAULT_QR_PATH):
    setup_fonts()
    today = datetime.date.today().strftime("%d.%m.%Y")
    
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        topMargin=2.8*cm, bottomMargin=2.5*cm, leftMargin=2*cm, rightMargin=2*cm
    )

    def nexus_decorator(canvas, doc):
        canvas.saveState()
        # 1. Header (Graphite block)
        canvas.setFillColor(LayoutConfig.GRAPHITE)
        canvas.rect(0, A4[1]-2.2*cm, A4[0], 2.2*cm, fill=1, stroke=0)
        
        # 2. QR Code
        if os.path.exists(qr_path):
            canvas.drawImage(qr_path, A4[0]-2.0*cm - 1.6*cm, A4[1]-1.9*cm, width=1.6*cm, height=1.6*cm)
            
        # 3. Header Text
        canvas.setFillColor(LayoutConfig.WHITE)
        canvas.setFont("Arial-Bold", 11)
        canvas.drawString(2*cm, A4[1]-1.0*cm, "LEGAL-DEVOPS INFRASTRUCTURE")
        canvas.setFont("Arial", 8)
        canvas.drawString(2*cm, A4[1]-1.5*cm, f"ІДЕНТИФІКАТОР СПРАВИ: {case_id} | DOC: {doc_code}")
        
        # 4. Footer Lines
        canvas.setStrokeColor(LayoutConfig.STEEL_BLUE)
        canvas.setLineWidth(1)
        canvas.line(2*cm, 1.8*cm, A4[0]-2*cm, 1.8*cm)
        
        # Footer Text - Line 1
        canvas.setFillColor(LayoutConfig.GRAPHITE)
        canvas.setFont("Arial", 8)
        canvas.drawString(2*cm, 1.35*cm, "Юридичний супровід та моніторинг здійснюється системою Legal-DevOps Infrastructure.")
        canvas.setFont("Arial-Bold", 8)
        canvas.drawRightString(A4[0]-2*cm, 1.35*cm, "NEXUS-Orchestrator")
        
        # Footer Text - Line 2
        canvas.setFont("Arial", 7.5)
        canvas.setFillColor(LayoutConfig.MID_GRAY)
        canvas.drawString(2*cm, 0.95*cm, f"Електронний ідентифікатор справи: {case_id}")
        canvas.drawRightString(A4[0]-2*cm, 0.95*cm, f"Timestamp: {today}")
        
        canvas.restoreState()

    story = []
    s = get_standard_styles()

    # Meta Section (Sender / Recipient)
    meta_table = Table([
        [Paragraph(f"<b>ОТРИМУВАЧ:</b> {recipient_text}", s['body_bold'])],
        [Paragraph(f"<b>ВІДПРАВНИК:</b> {sender_text}", s['body_bold'])]
    ], colWidths=[17*cm])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LayoutConfig.LIGHT_BLUE),
        ('BOX', (0,0), (-1,-1), 0.5, LayoutConfig.BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6)
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 1*cm))

    # Main Title
    story.append(Paragraph(doc_title, s['title_center']))
    story.append(Spacer(1, 0.8*cm))

    # Build Content Blocks dynamically
    story = content_builder(story, s)

    # Warning Block
    story.append(Spacer(1, 1*cm))
    warning_style = ParagraphStyle(
        "WarningBlock", 
        fontName="Arial-Bold", 
        fontSize=9, 
        textColor=LayoutConfig.GRAPHITE, 
        backColor=colors.HexColor("#FEE2E2"), # Light red background
        borderPadding=8,
        borderColor=colors.HexColor("#EF4444"),
        borderWidth=1,
        borderRadius=2,
        alignment=TA_JUSTIFY,
        leading=13
    )
    warning_text = (
        "АВТОМАТИЗОВАНИЙ КОНТРОЛЬ: Цей документ сформовано та взято на моніторинг системою Legal-DevOps. "
        "Ігнорування вимог або порушення встановлених законом строків надання відповіді є підставою "
        "для автоматичної ініціації скарг до КМДА, Держпродспоживслужби та прокуратури щодо бездіяльності посадових осіб."
    )
    story.append(Paragraph(warning_text, warning_style))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(f"Дата автоматичної генерації: {today} | Підпис не потрібен (цифровий слід сформовано)", 
                           ParagraphStyle("Sig", fontName="Arial-Bold", fontSize=9, textColor=LayoutConfig.MID_GRAY)))

    doc.build(story, onFirstPage=nexus_decorator, onLaterPages=nexus_decorator)
    return output_path

def test_builder(story, styles):
    story.append(Paragraph("▸ Тестовий блок", styles['h2']))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LayoutConfig.BORDER))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Стандартизація дизайну успішно завершена. Об'єкт готовий до імпорту іншими модулями системи.", styles['body']))
    return story

if __name__ == "__main__":
    out_dir = r"E:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\core"
    if not os.path.exists(out_dir): os.makedirs(out_dir)
    p = os.path.join(out_dir, "test_template.pdf")
    create_nexus_document(p, "SYS-TEST-00", "CORE-INIT", "СТАНДАРТ ГЕНЕРАЦІЇ NEXUS-DEVOPS", "System Init", "Administrator", test_builder)
    print(f"Template system initialized at {p}")
