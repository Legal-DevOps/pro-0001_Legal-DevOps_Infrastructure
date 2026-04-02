
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

# Register Arial with Cyrillic support
# Checking standard Windows paths
font_path = 'C:/Windows/Fonts/arial.ttf'
font_bold_path = 'C:/Windows/Fonts/arialbd.ttf'

pdfmetrics.registerFont(TTFont('Arial', font_path))
pdfmetrics.registerFont(TTFont('Arial-Bold', font_bold_path))

# Settings
DARK_NAVY    = colors.HexColor('#333333')
ACCENT_BLUE  = colors.HexColor('#4A708B')
LIGHT_BLUE   = colors.HexColor('#F4F6F9')
MID_GRAY     = colors.HexColor('#64748B')
BORDER_GRAY  = colors.HexColor('#CBD5E1')
WHITE        = colors.white

TARGET_DIR   = r'e:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\archive\0004\final_output'
CASE_ID      = 'CASE-0004-SWEEP'
TODAY        = datetime.date.today().strftime('%d.%m.%Y')

def build_pdf(filename, doc_code, doc_title, sections):
    path = os.path.join(TARGET_DIR, filename)
    doc  = SimpleDocTemplate(path, pagesize=A4,
                               topMargin=2.2*cm, bottomMargin=2.5*cm,
                               leftMargin=2.0*cm, rightMargin=2.0*cm)

    styles = getSampleStyleSheet()
    body = ParagraphStyle('Body', fontName='Arial', fontSize=10, leading=15, spaceAfter=6, alignment=TA_JUSTIFY)
    body_bold = ParagraphStyle('BodyBold', parent=body, fontName='Arial-Bold')
    section_head = ParagraphStyle('SecHead', fontName='Arial-Bold', fontSize=10, textColor=ACCENT_BLUE, spaceBefore=10, spaceAfter=4)
    bullet_item = ParagraphStyle('Bullet', fontName='Arial', fontSize=10, leftIndent=14, leading=15, spaceAfter=4, bulletIndent=4, alignment=TA_JUSTIFY)

    def page_decor(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(DARK_NAVY)
        canvas.rect(0, A4[1]-1.4*cm, A4[0], 1.4*cm, fill=1, stroke=0)
        canvas.setFillColor(WHITE)
        canvas.setFont('Arial-Bold', 8.5)
        canvas.drawString(1.8*cm, A4[1]-0.7*cm, 'LEGAL-DEVOPS INFRASTRUCTURE')
        canvas.setFont('Arial', 8)
        canvas.drawRightString(A4[0]-1.8*cm, A4[1]-0.7*cm, f'{doc_code} | {CASE_ID} | {TODAY}')
        canvas.setFillColor(LIGHT_BLUE)
        canvas.rect(0, 0, A4[0], 1.4*cm, fill=1, stroke=0)
        canvas.setStrokeColor(ACCENT_BLUE)
        canvas.setLineWidth(1.5)
        canvas.line(0, 1.4*cm, A4[0], 1.4*cm)
        canvas.setFillColor(DARK_NAVY)
        canvas.setFont('Arial', 7.5)
        canvas.drawString(1.8*cm, 0.7*cm, "Юридичний супровід та моніторинг виконання зобов'язань здійснюється системою Legal-DevOps.")
        canvas.setFillColor(ACCENT_BLUE)
        canvas.setFont('Arial-Bold', 7.5)
        canvas.drawRightString(A4[0]-1.8*cm, 0.7*cm, f'Ідентифікатор системи: {CASE_ID}')
        canvas.setFillColor(ACCENT_BLUE)
        canvas.rect(0, 1.4*cm, 0.35*cm, A4[1]-2.8*cm, fill=1, stroke=0)
        canvas.restoreState()

    story = [Spacer(1, 0.5*cm)]
    # FROM / TO Block
    meta_data = [
        [Paragraph('<b>ОТРИМУВАЧ</b>', body_bold), Paragraph('<b>ВІДПРАВНИК</b>', body_bold)],
        [Paragraph('Керівництво ТОВ «ІНСТИТУТ УКРДОРПРОЕКТ»<br/>Корецькому Сергію Степановичу', body),
         Paragraph('Ініціативна група працівників<br/>Case ID: 0004-SWEEP', body)],
    ]
    meta_table = Table(meta_data, colWidths=[8.5*cm, 8.5*cm])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), LIGHT_BLUE),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_GRAY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_GRAY),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 0.5*cm))

    # Title
    title_data = [[Paragraph(f'<font color="#FFFFFF"><b>{doc_title}</b></font>', ParagraphStyle('TitleWhite', fontName='Arial-Bold', fontSize=13, alignment=TA_CENTER, textColor=WHITE))]]
    title_table = Table(title_data, colWidths=[17*cm])
    title_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_NAVY),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(title_table)
    story.append(Spacer(1, 0.5*cm))

    for sec_title, items in sections:
        if sec_title:
            story.append(Paragraph(f'>> {sec_title}', section_head))
            story.append(HRFlowable(width='100%', thickness=0.5, color=BORDER_GRAY))
            story.append(Spacer(1, 0.15*cm))
        for item in items:
            p_style = bullet_item if item.startswith('•') else body
            story.append(Paragraph(item, p_style))
        story.append(Spacer(1, 0.2*cm))

    story.append(Spacer(1, 0.5*cm))
    sig_data = [[Paragraph(f'Дата: {TODAY}', body_bold), Paragraph('Підпис: _____________________', body_bold)]]
    sig_table = Table(sig_data, colWidths=[8.5*cm, 8.5*cm])
    sig_table.setStyle(TableStyle([('LINEABOVE', (0,0), (-1,0), 0.5, BORDER_GRAY), ('TOPPADDING', (0,0), (-1,-1), 8), ('LEFTPADDING', (0,0), (0,-1), 0)]))
    story.append(sig_table)
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
    return path

sections = [
    ('Щодо операцій з іноземним контрагентом', [
        'Надати копію Протоколу перевірки (Due Diligence) контрагента SWEEP DEVELOPMENT (Туреччина), контракт № TM-KBG-01/Д1-С.РП від 31.10.2022.',
        '• Яким чином було підтверджено платоспроможність компанії, створеної за 30 днів до підписання?',
        '• Хто саме проводив перевірку бенефіціарів згідно з п. 13.8 Контракту?',
    ]),
    ('Щодо розподілу прибутку', [
        'Надати інформацію про нараховані та виплачені дивіденди бенефіціарам (Корецькому С.С., Гуджабідзе Г.Р. та іншим) за 2022-2024 рр.',
        'Виплата дивідендів при наявності боргів з зарплати є ознакою розтрати майна (ст. 191 КК України).',
    ]),
    ('Щодо цільового використання коштів', [
        'Надати звіт про рух коштів від державних тендерів. Чому вони не спрямовані на погашення заборгованості перед персоналом?',
    ]),
    ('Попередження про наслідки', [
        'Ненадання відповіді протягом 48 годин буде розцінено як підтвердження зговору. Матеріали будуть передані до НАБУ та Turkish MASAK.',
    ])
]

build_pdf('LEGAL_DEMAND_INSTITUTE.pdf', 'DOC-0004-DEM', 'ЮРИДИЧНИЙ ЗАПИТ ТА ВИМОГА', sections)
print('PDF Created Success: LEGAL_DEMAND_INSTITUTE.pdf')
