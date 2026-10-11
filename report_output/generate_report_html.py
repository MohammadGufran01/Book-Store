# report_output/generate_report_html.py
import os
import sys
import shutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

def get_code(rel_path, max_lines=90):
    path = os.path.join(PROJECT_DIR, rel_path)
    if not os.path.exists(path):
        return f"# File {rel_path} not found"
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = [line.rstrip() for line in f if line.strip()]
        if max_lines and len(lines) > max_lines:
            lines = lines[:max_lines] + [f"# ... [Listing truncated for documentation brevity - full code in {rel_path}]"]
        return "\n".join(lines)

def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# Copy logo if needed
logo_src = os.path.join(PROJECT_DIR, 'report_assets', 'rId8.jpg')
logo_dst = os.path.join(BASE_DIR, 'logo.jpg')
if os.path.exists(logo_src) and not os.path.exists(logo_dst):
    shutil.copy(logo_src, logo_dst)

html_pages = []

def add_page(content, page_num=None, is_cover=False):
    pn_html = ""
    if page_num is not None:
        pn_html = f'<div class="page-number">{page_num}</div>'
    extra_cls = " cover-page" if is_cover else ""
    html = f'''<div class="page-container{extra_cls}">
{content}
{pn_html}
</div>'''
    html_pages.append(html)

print("Starting to generate page content...")
