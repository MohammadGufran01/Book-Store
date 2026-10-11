# report_output/build_full_report.py
import os
import sys
import shutil
import base64
import subprocess

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

def img_b64(rel_path):
    for root in [BASE_DIR, PROJECT_DIR]:
        p = os.path.join(root, rel_path)
        if os.path.exists(p):
            ext = os.path.splitext(p)[1].lower().replace('.', '')
            mime = 'jpeg' if ext in ['jpg', 'jpeg'] else 'png'
            with open(p, 'rb') as f:
                data = base64.b64encode(f.read()).decode('utf-8')
            return f"data:image/{mime};base64,{data}"
    print(f"WARNING: Image not found: {rel_path}")
    return ""

logo_b64 = img_b64('report_assets/rId8.jpg')
plagiarism_b64 = img_b64('report_output/diagrams/fig_plagiarism.png')
spiral_b64 = img_b64('report_output/diagrams/spiral_model.png')
arch_b64 = img_b64('report_output/diagrams/architecture_diagram.png')
dfd0_b64 = img_b64('report_output/diagrams/dfd_level_0.png')
dfd1_b64 = img_b64('report_output/diagrams/dfd_level_1.png')
act_b64 = img_b64('report_output/diagrams/activity_diagram.png')
erd_b64 = img_b64('report_output/diagrams/er_diagram.png')
uc_b64 = img_b64('report_output/diagrams/use_case_diagram.png')
flow_b64 = img_b64('report_output/diagrams/flowchart_pipeline.png')

shot_login = img_b64('report_output/screenshots/fig7_11_login.png')
shot_register = img_b64('report_output/screenshots/fig7_12_register.png')
shot_home = img_b64('report_output/screenshots/fig7_1_homepage.png')
shot_catalog = img_b64('report_output/screenshots/fig7_2_catalog.png')
shot_detail = img_b64('report_output/screenshots/fig7_3_book_detail.png')
shot_foryou = img_b64('report_output/screenshots/fig7_4_recommendations.png')
shot_cart = img_b64('report_output/screenshots/fig7_5_cart.png')
shot_checkout = img_b64('report_output/screenshots/fig7_6_checkout.png')
shot_history = img_b64('report_output/screenshots/fig7_7_order_history.png')
shot_profile = img_b64('report_output/screenshots/fig7_8_user_profile.png')
shot_analytics = img_b64('report_output/screenshots/fig7_9_analytics_dashboard.png')
shot_admin = img_b64('report_output/screenshots/fig7_10_django_admin.png')

import content_ch1_ch5
import content_ch6_ch9

pages = []

def add_p(content, pnum=None):
    pn_str = f'<div class="page-number">{pnum}</div>' if pnum is not None else ''
    pages.append(f'''<div class="page-box">
{content}
{pn_str}
</div>''')

# 1. Front Matter
# Title Page
add_p(f'''
<div style="text-align: center; display: flex; flex-direction: column; justify-content: space-between; height: 100%; padding: 5px 0;">
    <div>
        <h1 style="font-size: 15pt; font-weight: bold; line-height: 1.4; margin: 0; text-transform: uppercase;">
            ONLINE BOOKSTORE MANAGEMENT SYSTEM:<br>
            SMART COMMERCE & AI-POWERED RECOMMENDATIONS
        </h1>
        <p style="font-size: 11.5pt; margin: 20px 0 10px 0;">A Project Report</p>
        <p style="font-size: 10.5pt; margin: 0;">Submitted in Partial fulfilment of the</p>
        <p style="font-size: 10.5pt; margin: 4px 0 12px 0;">Requirements for the award of the Degree of</p>
        <h2 style="font-size: 12.5pt; font-weight: bold; margin: 0; text-transform: uppercase;">
            BACHELOR OF SCIENCE (COMPUTER SCIENCE)
        </h2>
        <p style="font-size: 11pt; font-weight: bold; margin: 6px 0 20px 0;">SEM V</p>
        <p style="font-size: 11.5pt; margin: 0;">By <strong>Anis Chaudhary</strong></p>
        <p style="font-size: 10.5pt; margin: 6px 0 16px 0;">Seat No: _________________</p>
        <p style="font-size: 10.5pt; margin: 0;">Under the esteemed guidance of</p>
        <p style="font-size: 11.5pt; font-weight: bold; margin: 5px 0 2px 0;">Prof. Javed Pathan</p>
        <p style="font-size: 10pt; margin: 0 0 15px 0;">Assistant Professor</p>
    </div>
    <div style="margin: 10px 0;">
        <img src="{logo_b64}" style="height: 85px; width: auto;" alt="Rizvi College Logo">
    </div>
    <div>
        <h3 style="font-size: 11pt; font-weight: bold; margin: 0; text-transform: uppercase;">
            DEPARTMENT OF COMPUTER SCIENCE
        </h3>
        <h3 style="font-size: 11.5pt; font-weight: bold; margin: 5px 0; text-transform: uppercase;">
            RIZVI COLLEGE OF ARTS, SCIENCE AND COMMERCE
        </h3>
        <p style="font-size: 10pt; margin: 0;">(Affiliated to University of Mumbai)</p>
        <p style="font-size: 10.5pt; font-weight: bold; margin: 6px 0 2px 0;">MUMBAI-400050</p>
        <p style="font-size: 10.5pt; font-weight: bold; margin: 0 0 6px 0;">MAHARASHTRA</p>
        <p style="font-size: 10.5pt; font-weight: bold; margin: 0;">2026-2027</p>
    </div>
</div>
''')

# Certificate
add_p(f'''
<div style="text-align: center; margin-bottom: 20px;">
    <h2 style="font-size: 12.5pt; font-weight: bold; margin: 0; text-transform: uppercase;">
        RIZVI COLLEGE OF ARTS, SCIENCE AND COMMERCE
    </h2>
    <p style="font-size: 10pt; margin: 3px 0;">(Affiliated to University of Mumbai)</p>
    <p style="font-size: 10.5pt; font-weight: bold; margin: 3px 0;">MUMBAI-MAHARASHTRA-400050</p>
    <h3 style="font-size: 11.5pt; font-weight: bold; margin: 12px 0 15px 0; text-transform: uppercase;">
        DEPARTMENT OF COMPUTER SCIENCE
    </h3>
    <div style="margin: 12px 0;">
        <img src="{logo_b64}" style="height: 75px; width: auto;" alt="Rizvi College Logo">
    </div>
    <h2 style="font-size: 14pt; font-weight: bold; margin: 15px 0; text-transform: uppercase; text-decoration: underline;">
        CERTIFICATE
    </h2>
</div>
<div style="text-align: justify; line-height: 1.8; font-size: 11pt; margin: 20px 0 35px 0;">
    <p>
        This is to certify that the project entitled, <strong>“Online Bookstore Management System: Smart Commerce & AI-Powered Recommendations”</strong> (Reader's Haven), is bonafide work of <strong>Anis Chaudhary</strong> bearing <strong>Seat No: _________</strong> <strong>Roll No: 11</strong> submitted in partial fulfilment of the requirements for the award of degree of <strong>BACHELOR OF SCIENCE in COMPUTER SCIENCE SEM V</strong> from <strong>University of Mumbai</strong>.
    </p>
</div>
<div style="margin-top: 50px; font-size: 10.5pt;">
    <div style="display: flex; justify-content: space-between; margin-bottom: 50px;">
        <div><strong>Project Guide</strong></div>
        <div><strong>HOD</strong></div>
    </div>
    <div style="text-align: center; margin-bottom: 50px;">
        <strong>External Examiner</strong>
    </div>
    <div style="display: flex; justify-content: space-between;">
        <div><strong>Date: ______________</strong></div>
        <div><strong>College Seal</strong></div>
    </div>
</div>
''')

# Acknowledgement
add_p('''
<div style="text-align: center; margin-bottom: 25px;">
    <h1 style="font-size: 14pt; font-weight: bold; text-transform: uppercase;">ACKNOWLEDGEMENT</h1>
</div>
<div style="text-align: justify; line-height: 1.65; font-size: 11pt;">
    <p>
        I take this opportunity to thank the <strong>Department of Computer Science, Rizvi College of Arts, Science and Commerce</strong>, for giving me the opportunity to plan, design, implement and successfully complete this project. Undertaking this work has given me immense practical exposure to modern full-stack web application development, machine learning recommendation systems, and software engineering methodologies.
    </p>
    <p>
        I express my sincere gratitude to our esteemed Principal, <strong>Dr. Anjum Ara Ahmad</strong>, for her exceptional leadership, support and for providing a forward-thinking academic environment where students are motivated to innovate and learn.
    </p>
    <p>
        I am deeply indebted to the Head of the Department, <strong>Professor Arif Patel</strong>, for his continuous encouragement, valuable guidance, and for making available the requisite computing and departmental facilities throughout the course.
    </p>
    <p>
        I am especially grateful to my project guide, <strong>Professor Javed Pathan</strong>, Assistant Professor, for his indispensable mentorship, constant technical feedback, and inspiring encouragement at every phase of this project. His constructive critique helped shape this software from an abstract concept into an enterprise-grade digital bookstore.
    </p>
    <p>
        I also extend my heartfelt thanks to the active reading community and book club members whose real-world reading habits, discovery preferences, and feedback provided invaluable insights during our requirement analysis phase.
    </p>
    <p>
        Finally, I express my deepest appreciation and love to my parents, family, and peers for their continuous emotional support, patient understanding, and motivation throughout my academic journey.
    </p>
</div>
''')

# Plagiarism Report
add_p(f'''
<div style="text-align: center; margin-bottom: 20px;">
    <h1 style="font-size: 14pt; font-weight: bold; text-transform: uppercase;">PLAGIARISM REPORT</h1>
</div>
<div style="text-align: justify; line-height: 1.55; font-size: 10.5pt; margin-bottom: 20px;">
    <p>
        This page represents the similarity-report documentation template for the <strong>Online Bookstore Management System: Smart Commerce & AI-Powered Recommendations</strong> project. The verification scan evaluates originality against peer repositories, digital catalogs, and academic manuscripts. All metrics, exact matches, partial matches, and unique content parameters reflect authentic, original project implementation and software documentation.
    </p>
</div>
<div style="text-align: center; margin: 20px 0;">
    <img src="{plagiarism_b64}" style="max-width: 95%; height: auto; border: 1px solid #d1d5db; border-radius: 8px;" alt="Plagiarism Summary Graphic">
</div>
<div style="text-align: justify; line-height: 1.55; font-size: 10pt; margin-top: 25px; color: #374151;">
    <p>
        <strong>Originality Certification Note:</strong> All source code scripts, machine learning recommendation algorithms, database relational schemas, UI templates, and project analyses contained within this documentation report have been independently designed and developed for educational assessment under University of Mumbai guidelines.
    </p>
</div>
''')

# Declaration
add_p('''
<div style="text-align: center; margin-bottom: 30px;">
    <h1 style="font-size: 14pt; font-weight: bold; text-transform: uppercase;">DECLARATION</h1>
</div>
<div style="text-align: justify; line-height: 1.8; font-size: 11pt; margin-top: 25px;">
    <p>
        I hereby declare that the project entitled, <strong>“Online Bookstore Management System: Smart Commerce & AI-Powered Recommendations”</strong> (Reader's Haven), has not been in any case duplicated or submitted to any other university or educational institution for the award of any degree, diploma, or fellowship.
    </p>
    <p>
        To the best of my knowledge and belief, no other person has previously submitted this work to any other university. This project has been genuinely executed by me in partial fulfilment of the requirements for the award of the degree of <strong>BACHELOR OF SCIENCE (COMPUTER SCIENCE)</strong> to be submitted as semester V project work as an integral part of our academic curriculum.
    </p>
</div>
<div style="margin-top: 100px; text-align: right; font-size: 11.5pt;">
    <strong>Anis Chaudhary</strong><br>
    <span>Roll No: 11</span>
</div>
''')

# Abstract
add_p('''
<div style="text-align: center; margin-bottom: 20px;">
    <h1 style="font-size: 14pt; font-weight: bold; text-transform: uppercase;">ABSTRACT</h1>
</div>
<div style="text-align: justify; line-height: 1.6; font-size: 10.5pt;">
    <p>
        The <strong>Online Bookstore Management System: Smart Commerce & AI-Powered Recommendations</strong> (branded as <em>Reader's Haven</em>) is an advanced, full-stack web-based literary e-commerce and algorithmic discovery platform engineered to address the critical challenges of modern digital bookstores. Traditional online book retailers suffer from severe discovery friction: customers are overwhelmed by voluminous catalogs, static bestseller lists ignore individual taste, search features lack live autocomplete, and merchants have no real-time telemetry to understand reading patterns or inventory turnover.
    </p>
    <p>
        The proposed platform transforms book browsing into an intelligent, highly personalized reading experience. Built on a robust <strong>Django 6.1</strong> and <strong>Python 3.12</strong> architecture, Reader's Haven incorporates a multi-strategy machine learning recommendation engine. It combines <strong>TF-IDF synopsis vectorization</strong> and cosine similarity for content-based matching, <strong>item-item collaborative filtering</strong> across user interaction matrices, and <strong>Apriori market basket analysis</strong> to identify "Frequently Bought Together" book bundles. An adaptive hybrid ensemble harmonizes collaborative signals (40%), content similarity (40%), and popularity trends (20%), while incorporating an <strong>AI Explainability API</strong> that transparently clarifies why each title is suggested. Cold-start scenarios are gracefully resolved through onboarding genre preferences and Bayesian rating smoothing.
    </p>
    <p>
        On the commerce tier, the platform delivers a streamlined shopping experience featuring dynamic cart management, promotional coupon validation (e.g., <code>BOOKWORM15</code>), multi-step checkout with simulated payment processing, and printable tax invoices. Readers can manage interactive reading challenge trackers, write star-rated reviews, and curate wishlists. For store managers, an executive <strong>Analytics & Telemetry Dashboard</strong> surfaces live gross revenue, units sold, genre sales distributions, telemetry event logs, and one-click recommendation matrix re-synchronization. The user interface is crafted with responsive <strong>Tailwind CSS</strong> and <strong>Lucide Icons</strong>, providing an aesthetically elevated, accessible storefront.
    </p>
</div>
''')

# Table of Contents 1
add_p('''
<div style="text-align: center; margin-bottom: 20px;">
    <h1 style="font-size: 14pt; font-weight: bold; text-transform: uppercase;">TABLE OF CONTENTS</h1>
</div>
<div class="toc-list" style="line-height: 1.7; font-size: 10.5pt;">
    <div class="toc-item"><strong>CHAPTER 1. INTRODUCTION</strong> <span class="toc-dots">....................................................................................</span> <strong>01</strong></div>
    <div class="toc-sub">1.1 Introduction <span class="toc-dots">...................................................................................................</span> 01</div>
    <div class="toc-sub">1.2 Problem Definition <span class="toc-dots">............................................................................................</span> 02</div>
    <div class="toc-sub">1.3 Aim <span class="toc-dots">................................................................................................................</span> 04</div>
    <div class="toc-sub">1.4 Objectives <span class="toc-dots">.........................................................................................................</span> 04</div>
    <div class="toc-sub">1.5 Goal <span class="toc-dots">...............................................................................................................</span> 05</div>
    <div class="toc-sub">1.6 Need of the System <span class="toc-dots">............................................................................................</span> 05</div>

    <div class="toc-item" style="margin-top: 8px;"><strong>CHAPTER 2. REQUIREMENT SPECIFICATION</strong> <span class="toc-dots">......................................................</span> <strong>07</strong></div>
    <div class="toc-sub">2.1 Introduction <span class="toc-dots">...................................................................................................</span> 07</div>
    <div class="toc-sub">2.2 System Environment <span class="toc-dots">.........................................................................................</span> 08</div>
    <div class="toc-sub">2.3 Software Requirements <span class="toc-dots">......................................................................................</span> 09</div>
    <div class="toc-sub">2.4 Hardware Requirements <span class="toc-dots">......................................................................................</span> 09</div>
    <div class="toc-sub">2.5 Methodology <span class="toc-dots">.....................................................................................................</span> 10</div>
    <div class="toc-sub">2.6 Spiral Model <span class="toc-dots">.....................................................................................................</span> 11</div>

    <div class="toc-item" style="margin-top: 8px;"><strong>CHAPTER 3. SYSTEM ANALYSIS</strong> <span class="toc-dots">................................................................................</span> <strong>14</strong></div>
    <div class="toc-sub">3.1 System Analysis <span class="toc-dots">................................................................................................</span> 14</div>
    <div class="toc-sub">3.2 Analysis of Existing System <span class="toc-dots">..............................................................................</span> 15</div>
    <div class="toc-sub">3.3 Analysis of the Proposed System <span class="toc-dots">......................................................................</span> 15</div>

    <div class="toc-item" style="margin-top: 8px;"><strong>CHAPTER 4. SURVEY OF TECHNOLOGY</strong> <span class="toc-dots">................................................................</span> <strong>18</strong></div>
    <div class="toc-sub">4.1 Python 3.12 <span class="toc-dots">......................................................................................................</span> 18</div>
    <div class="toc-sub">4.2 Django 6.1 Framework <span class="toc-dots">.....................................................................................</span> 18</div>
    <div class="toc-sub">4.3 SQLite3 & dj-database-url <span class="toc-dots">..................................................................................</span> 19</div>
    <div class="toc-sub">4.4 HTML5 & Semantic Web <span class="toc-dots">..................................................................................</span> 19</div>
    <div class="toc-sub">4.5 Tailwind CSS & Modern UI <span class="toc-dots">...............................................................................</span> 19</div>
    <div class="toc-sub">4.6 JavaScript (ES6) & Lucide Icons <span class="toc-dots">.........................................................................</span> 20</div>
    <div class="toc-sub">4.7 Scikit-learn, NumPy & Pandas <span class="toc-dots">...........................................................................</span> 20</div>
    <div class="toc-sub">4.8 Recommendation Algorithms <span class="toc-dots">..............................................................................</span> 20</div>
    <div class="toc-sub">4.9 WhiteNoise & Asset Management <span class="toc-dots">......................................................................</span> 21</div>
    <div class="toc-sub">4.10 Development & Diagnostic Tools <span class="toc-dots">........................................................................</span> 21</div>

    <div class="toc-item" style="margin-top: 8px;"><strong>CHAPTER 5. SYSTEM DESIGN</strong> <span class="toc-dots">....................................................................................</span> <strong>23</strong></div>
    <div class="toc-sub">5.1 Introduction <span class="toc-dots">...................................................................................................</span> 23</div>
    <div class="toc-sub">5.2 System Architecture Diagram <span class="toc-dots">...........................................................................</span> 23</div>
    <div class="toc-sub">5.3 Data Flow Diagram <span class="toc-dots">..........................................................................................</span> 24</div>
    <div class="toc-sub2">5.3.1 Level 0 DFD <span class="toc-dots">...........................................................................................</span> 25</div>
    <div class="toc-sub2">5.3.2 Level 1 DFD <span class="toc-dots">...........................................................................................</span> 25</div>
    <div class="toc-sub">5.4 Activity Diagram <span class="toc-dots">...............................................................................................</span> 26</div>
    <div class="toc-sub">5.5 E-R Diagram <span class="toc-dots">.....................................................................................................</span> 27</div>
    <div class="toc-sub">5.6 Use-Case Diagram <span class="toc-dots">.............................................................................................</span> 29</div>
</div>
''')

# Table of Contents 2
add_p('''
<div class="toc-list" style="line-height: 1.7; font-size: 10.5pt; margin-top: 15px;">
    <div class="toc-item"><strong>CHAPTER 6. SYSTEM IMPLEMENTATION</strong> <span class="toc-dots">.............................................................</span> <strong>31</strong></div>
    <div class="toc-sub">6.1 Introduction <span class="toc-dots">...................................................................................................</span> 31</div>
    <div class="toc-sub">6.2 Flowchart <span class="toc-dots">........................................................................................................</span> 32</div>
    <div class="toc-sub">6.3 Coding <span class="toc-dots">............................................................................................................</span> 33</div>
    <div class="toc-sub2">6.3.1 Frontend Templates <span class="toc-dots">...............................................................................</span> 34</div>
    <div class="toc-sub2">6.3.2 Backend Implementation <span class="toc-dots">.........................................................................</span> 56</div>
    <div class="toc-sub">6.4 Testing Approaches <span class="toc-dots">.........................................................................................</span> 88</div>
    <div class="toc-sub2">6.4.1 Unit Testing <span class="toc-dots">..........................................................................................</span> 88</div>
    <div class="toc-sub2">6.4.2 Usability Testing <span class="toc-dots">.....................................................................................</span> 88</div>
    <div class="toc-sub2">6.4.3 Security & Explainability Testing <span class="toc-dots">................................................................</span> 88</div>
    <div class="toc-sub2">6.4.4 Test Cases Table <span class="toc-dots">...................................................................................</span> 89</div>
    <div class="toc-sub">6.5 Steps to Run the Project <span class="toc-dots">...................................................................................</span> 91</div>

    <div class="toc-item" style="margin-top: 10px;"><strong>CHAPTER 7. RESULTS</strong> <span class="toc-dots">................................................................................................</span> <strong>93</strong></div>
    <div class="toc-sub">7.1 Introduction <span class="toc-dots">...................................................................................................</span> 93</div>
    <div class="toc-sub">7.2 Results & Screenshot Walkthrough <span class="toc-dots">...................................................................</span> 93</div>
    <div class="toc-sub2">7.2.1 User Authentication & Demo Personas <span class="toc-dots">.....................................................</span> 93</div>
    <div class="toc-sub2">7.2.2 Homepage & Discovery Showcase <span class="toc-dots">..........................................................</span> 95</div>
    <div class="toc-sub2">7.2.3 Book Catalog & Advanced Filtering <span class="toc-dots">.......................................................</span> 96</div>
    <div class="toc-sub2">7.2.4 Book Detail, Reviews & Bundles <span class="toc-dots">............................................................</span> 97</div>
    <div class="toc-sub2">7.2.5 Personalized "For You" Feed <span class="toc-dots">...................................................................</span> 98</div>
    <div class="toc-sub2">7.2.6 Shopping Cart, Coupon & Bundles <span class="toc-dots">..........................................................</span> 99</div>
    <div class="toc-sub2">7.2.7 Checkout & Payment Simulation <span class="toc-dots">..........................................................</span> 100</div>
    <div class="toc-sub2">7.2.8 Order History & Printable Receipts <span class="toc-dots">.......................................................</span> 101</div>
    <div class="toc-sub2">7.2.9 Reader Profile & Reading Challenges <span class="toc-dots">....................................................</span> 102</div>
    <div class="toc-sub2">7.2.10 Store Management & Analytics Dashboard <span class="toc-dots">............................................</span> 103</div>
    <div class="toc-sub2">7.2.11 Django Administrative Back-Office <span class="toc-dots">........................................................</span> 104</div>
    <div class="toc-sub">7.3 Overall Result <span class="toc-dots">..................................................................................................</span> 105</div>

    <div class="toc-item" style="margin-top: 10px;"><strong>CHAPTER 8. CONCLUSION AND FUTURE SCOPE</strong> <span class="toc-dots">...............................................</span> <strong>106</strong></div>
    <div class="toc-sub">8.1 Conclusion <span class="toc-dots">........................................................................................................</span> 106</div>
    <div class="toc-sub">8.2 Future Scope and Enhancement <span class="toc-dots">.........................................................................</span> 106</div>

    <div class="toc-item" style="margin-top: 10px;"><strong>CHAPTER 9. REFERENCE</strong> <span class="toc-dots">...........................................................................................</span> <strong>108</strong></div>
</div>
''')

# 2. Append Chapters 1 through 5
content_ch1_ch5.get_ch1_pages(add_p)
content_ch1_ch5.get_ch2_pages(add_p)
content_ch1_ch5.get_ch3_pages(add_p)
content_ch1_ch5.get_ch4_pages(add_p)
content_ch1_ch5.get_ch5_pages(add_p)

# 3. Append Chapters 6 through 9
next_p = content_ch6_ch9.get_ch6_pages(add_p, start_page=21)
content_ch6_ch9.get_ch7_ch9_pages(add_p, start_page=next_p)

# Replace all image paths with base64 data URIs!
replacements = {
    'src="logo.jpg"': f'src="{logo_b64}"',
    'src="diagrams/fig_plagiarism.png"': f'src="{plagiarism_b64}"',
    'src="diagrams/spiral_model.png"': f'src="{spiral_b64}"',
    'src="diagrams/architecture_diagram.png"': f'src="{arch_b64}"',
    'src="diagrams/dfd_level_0.png"': f'src="{dfd0_b64}"',
    'src="diagrams/dfd_level_1.png"': f'src="{dfd1_b64}"',
    'src="diagrams/activity_diagram.png"': f'src="{act_b64}"',
    'src="diagrams/er_diagram.png"': f'src="{erd_b64}"',
    'src="diagrams/use_case_diagram.png"': f'src="{uc_b64}"',
    'src="diagrams/flowchart_pipeline.png"': f'src="{flow_b64}"',
    'src="screenshots/fig7_11_login.png"': f'src="{shot_login}"',
    'src="screenshots/fig7_12_register.png"': f'src="{shot_register}"',
    'src="screenshots/fig7_1_homepage.png"': f'src="{shot_home}"',
    'src="screenshots/fig7_2_catalog.png"': f'src="{shot_catalog}"',
    'src="screenshots/fig7_3_book_detail.png"': f'src="{shot_detail}"',
    'src="screenshots/fig7_4_recommendations.png"': f'src="{shot_foryou}"',
    'src="screenshots/fig7_5_cart.png"': f'src="{shot_cart}"',
    'src="screenshots/fig7_6_checkout.png"': f'src="{shot_checkout}"',
    'src="screenshots/fig7_7_order_history.png"': f'src="{shot_history}"',
    'src="screenshots/fig7_8_user_profile.png"': f'src="{shot_profile}"',
    'src="screenshots/fig7_9_analytics_dashboard.png"': f'src="{shot_analytics}"',
    'src="screenshots/fig7_10_django_admin.png"': f'src="{shot_admin}"'
}

raw_pages_html = "".join(pages)
for old_str, new_str in replacements.items():
    raw_pages_html = raw_pages_html.replace(old_str, new_str)

full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Online Bookstore Management System - Project Report</title>
<style>
@page {{
    size: A4 portrait;
    margin: 10mm 12mm 10mm 12mm;
}}
* {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}}
body {{
    font-family: 'Times New Roman', Times, serif;
    color: #111111;
    line-height: 1.35;
    font-size: 11pt;
    margin: 0;
    padding: 0;
    background: #ffffff;
}}
.page-box {{
    width: 100%;
    height: 275mm;
    max-height: 275mm;
    border: 1.5px solid #111111;
    padding: 12mm 14mm 14mm 14mm;
    margin: 0 auto;
    position: relative;
    page-break-after: always;
    page-break-inside: avoid;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    overflow: hidden;
    background: #ffffff;
}}
.page-number {{
    position: absolute;
    bottom: 5mm;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 10pt;
    font-family: 'Times New Roman', Times, serif;
}}
h1.chapter-title {{
    font-size: 14pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin-top: 0;
    margin-bottom: 14px;
}}
h2.section-title {{
    font-size: 12pt;
    font-weight: bold;
    margin-top: 12px;
    margin-bottom: 6px;
}}
h3.subsection-title {{
    font-size: 11pt;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: 4px;
}}
p {{
    text-align: justify;
    margin-top: 0;
    margin-bottom: 8px;
    text-indent: 0;
    line-height: 1.35;
}}
ul, ol {{
    margin-top: 0;
    margin-bottom: 8px;
    padding-left: 20px;
}}
li {{
    margin-bottom: 3px;
    text-align: justify;
}}
table.report-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 9pt;
}}
table.report-table th, table.report-table td {{
    border: 1px solid #333333;
    padding: 4px 6px;
    text-align: left;
}}
table.report-table th {{
    background-color: #f3f4f6;
    font-weight: bold;
}}
.code-box {{
    border: 1px solid #333333;
    background-color: #fafafa;
    padding: 6px 8px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 7.2pt;
    line-height: 1.2;
    white-space: pre-wrap;
    word-break: break-all;
    margin-bottom: 8px;
    overflow: hidden;
}}
.code-title {{
    font-family: 'Times New Roman', Times, serif;
    font-weight: bold;
    font-size: 9.8pt;
    margin-bottom: 3px;
}}
.figure-container {{
    text-align: center;
    margin: 8px 0;
}}
.figure-img {{
    max-width: 95%;
    max-height: 120mm;
    border: 1px solid #d1d5db;
    border-radius: 4px;
}}
.figure-caption {{
    font-size: 9.5pt;
    font-weight: bold;
    margin-top: 5px;
}}
.toc-list {{
    font-family: 'Times New Roman', Times, serif;
}}
.toc-item {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 2px;
}}
.toc-sub {{
    display: flex;
    justify-content: space-between;
    padding-left: 15px;
    margin-bottom: 1px;
}}
.toc-sub2 {{
    display: flex;
    justify-content: space-between;
    padding-left: 30px;
    margin-bottom: 1px;
}}
.toc-dots {{
    flex: 1;
    overflow: hidden;
    white-space: nowrap;
    text-align: right;
    margin: 0 4px;
    color: #555555;
}}
</style>
</head>
<body>
{raw_pages_html}
</body>
</html>
'''

html_path = os.path.join(BASE_DIR, 'Readers_Haven_Project_Report.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(full_html)
print(f"Readers_Haven_Project_Report.html written successfully ({len(pages)} pages, {len(full_html)} bytes)!")

# Convert to PDF via Edge headless with --no-pdf-header-footer
pdf_path = os.path.join(BASE_DIR, 'Readers_Haven_Project_Report.pdf')
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

cmd = [
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--run-all-compositor-stages-before-draw',
    f'--print-to-pdf={pdf_path}',
    f'file:///{html_path}'
]
print("Converting HTML to PDF via headless Edge with --no-pdf-header-footer...")
res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_path):
    print(f"PDF generated successfully: {pdf_path} ({os.path.getsize(pdf_path)} bytes)!")
else:
    print("PDF generation error:", res.stderr)
