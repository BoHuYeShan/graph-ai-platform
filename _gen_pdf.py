#!/usr/bin/env python3
"""Generate B.A.I.T. v3 PDF using fpdf2 with CJK support."""
import re
import os
from fpdf import FPDF

FONT_PATH = r"C:\Windows\Fonts\simhei.ttf"
INPUT_MD = r"D:\-Users-\Documents\GitHub\PJG1\BAIT_Platform_Design_Doc_v3_clean.md"
OUTPUT_PDF = r"D:\-Users-\Documents\GitHub\PJG1\BAIT_Platform_Design_Doc_v3.pdf"

class BaitPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("CJK", "", FONT_PATH)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("CJK", size=8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 8, "B.A.I.T. Platform Design Doc v3", align="C")
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("CJK", size=8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"— {self.page_no()} —", align="C")


def clean_line(line):
    """Remove markdown formatting for plain text rendering."""
    # Bold
    line = re.sub(r'\*\*([^*]+)\*\*', r'\1', line)
    # Italic
    line = re.sub(r'\*([^*]+)\*', r'\1', line)
    # Inline code
    line = re.sub(r'`([^`]+)`', r'\1', line)
    # Links
    line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
    # Images
    line = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'[\1]', line)
    # Strikethrough
    line = re.sub(r'~~([^~]+)~~', r'\1', line)
    return line


def render_markdown(pdf, md_text):
    lines = md_text.split("\n")
    in_code_block = False
    in_table = False
    table_rows = []

    for line in lines:
        # Code block toggle
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            if in_code_block:
                pdf.set_font("Courier", size=8)
                pdf.set_fill_color(240, 240, 240)
            else:
                pdf.set_font("CJK", size=10)
                pdf.ln(2)
            continue

        if in_code_block:
            # Use CJK font (not Courier) to handle Chinese chars in code/JSON
            pdf.set_font("CJK", size=8)
            # Truncate very long lines
            display = line[:110] if len(line) > 110 else line
            if display.strip():
                pdf.cell(0, 4, display, new_x="LMARGIN", new_y="NEXT", fill=True)
            else:
                pdf.ln(2)
            continue

        # Horizontal rule
        if re.match(r'^---+$', line.strip()):
            pdf.ln(3)
            pdf.set_draw_color(200, 200, 200)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(5)
            continue

        # Table handling (simplified)
        if '|' in line and line.strip().startswith('|'):
            # Check if separator row
            if re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                continue  # skip separator
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if cells:
                pdf.set_font("CJK", size=8)
                col_w = (pdf.w - pdf.l_margin - pdf.r_margin) / max(len(cells), 1)
                for cell in cells:
                    cell = clean_line(cell)
                    pdf.cell(col_w, 6, cell[:40], border=1)
                pdf.ln()
            continue

        # Empty line
        if not line.strip():
            pdf.ln(3)
            continue

        # Headings
        for level in range(1, 7):
            pattern = r'^' + '#' * level + r'\s+(.+)'
            match = re.match(pattern, line)
            if match:
                text = clean_line(match.group(1))
                sizes = {1: 18, 2: 16, 3: 14, 4: 12, 5: 11, 6: 10}
                pdf.set_font("CJK", size=sizes.get(level, 10))
                if level <= 2:
                    pdf.ln(5)
                pdf.multi_cell(0, sizes.get(level, 10) + 4, text)
                pdf.ln(2)
                break
        else:
            # Regular paragraph
            pdf.set_font("CJK", size=10)
            cleaned = clean_line(line)

            # Reset x position to safe margin
            indent = 0
            list_match = re.match(r'^(\s*)([-*+]|\d+\.)\s+', cleaned)
            if list_match:
                indent = 10

            pdf.set_x(pdf.l_margin + indent)

            # Handle blockquotes
            if cleaned.startswith('>'):
                pdf.set_x(pdf.l_margin + 10)
                pdf.set_text_color(100, 100, 100)
                text = cleaned.lstrip('> ').strip()
                if text:
                    pdf.multi_cell(pdf.w - pdf.l_margin - pdf.r_margin - 10, 5, text)
                pdf.set_text_color(0, 0, 0)
            else:
                # Ensure enough space
                available_w = pdf.w - pdf.l_margin - pdf.r_margin - indent - 2
                if available_w > 20 and cleaned.strip():
                    pdf.multi_cell(available_w, 5, cleaned)


def main():
    with open(INPUT_MD, encoding="utf-8") as f:
        md_text = f.read()

    pdf = BaitPDF()
    pdf.add_page()
    pdf.set_font("CJK", size=10)

    render_markdown(pdf, md_text)
    pdf.output(OUTPUT_PDF)
    size = os.path.getsize(OUTPUT_PDF)
    print(f"PDF generated: {OUTPUT_PDF} ({size:,} bytes)")


if __name__ == "__main__":
    main()
