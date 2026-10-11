# report_output/content_ch6_ch9.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

def get_code(rel_path, max_lines=75):
    path = os.path.join(PROJECT_DIR, rel_path)
    if not os.path.exists(path):
        return f"# File {rel_path} not found"
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = [line.rstrip() for line in f if line.strip()]
        if max_lines and len(lines) > max_lines:
            lines = lines[:max_lines] + [f"\n# ... [Listing truncated for documentation brevity - full implementation in {rel_path}]"]
        return "\n".join(lines)

def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def get_ch6_pages(add_p, start_page=21):
    p = start_page

    # Page 21: Intro & Structure
    add_p(f'''
<h1 class="chapter-title">CHAPTER 6. SYSTEM IMPLEMENTATION</h1>
<h2 class="section-title">6.1 Introduction</h2>
<p>
System implementation is the critical phase where theoretical software designs, data flow architectures, and machine learning mathematical models are translated into executable code. In this stage, relational database tables are migrated, view controllers are programmed, template hierarchies are constructed, and recommendation algorithms are trained and integrated into the web server.
</p>
<p>
<strong>Reader's Haven</strong> is implemented using <strong>Python 3.12</strong> and the <strong>Django 6.1</strong> web framework. The codebase is organized cleanly into modular, decoupled applications adhering to Django's standard design principles:
</p>
<ul>
    <li><code>accounts</code>: User authentication, registration, profile management, and demo persona switching.</li>
    <li><code>books</code>: Author, Genre, Book, Review, and BookInteraction models, catalog views, and live search autocomplete APIs.</li>
    <li><code>cart</code>: Shopping cart session persistence, CartItem management, coupon calculations, and wishlist handlers.</li>
    <li><code>orders</code>: Multi-step checkout, Order/OrderItem models, simulated payment processing, and printable tax receipts.</li>
    <li><code>recommendations</code>: Content-based TF-IDF vectorizer, item-item collaborative filtering, Apriori market basket analysis, hybrid ensemble blending, and AI explainability services.</li>
    <li><code>analytics</code>: Executive store manager dashboard, gross sales KPIs, category sales breakdown, and manual matrix sync triggers.</li>
</ul>

<h3 class="subsection-title">Project Structure</h3>
<div class="code-box" style="font-size: 7.5pt; max-height: 80mm;">
Reader-Haven-Bookstore/
├── manage.py                          # Django management script
├── requirements.txt                   # Dependency manifest (Django, scikit-learn, etc.)
├── db.sqlite3                         # Relational SQLite database
├── bookstore_config/                  # Global project configuration
│   ├── settings.py · urls.py · wsgi.py · asgi.py
├── accounts/                          # User accounts & demo personas
│   ├── models.py · views.py · urls.py · forms.py
├── books/                             # Book catalog, reviews & search
│   ├── models.py · views.py · urls.py · forms.py · context_processors.py
├── cart/                              # Cart, coupons & wishlist
│   ├── models.py · views.py · urls.py · context_processors.py
├── orders/                            # Checkout, orders & receipts
│   ├── models.py · views.py · urls.py · forms.py
├── recommendations/                   # AI Machine Learning Engine
│   ├── models.py · views.py · urls.py
│   └── services/
│       ├── content_based.py · collaborative.py · association.py
│       ├── hybrid.py · engine.py
├── analytics/                         # Store manager telemetry dashboard
│   ├── models.py · views.py · urls.py
└── templates/                         # Semantic HTML5 & Tailwind UI
    ├── base.html
    ├── books/ (home.html, book_list.html, book_detail.html)
    ├── cart/ (cart_detail.html, wishlist.html)
    ├── orders/ (checkout.html, order_detail.html, order_history.html)
    ├── recommendations/ (for_you.html)
    └── analytics/ (dashboard.html)
</div>
''', pnum=p)
    p += 1

    # Page 22: Flowchart
    add_p(f'''
<h2 class="section-title">6.2 Flowchart</h2>
<p>
The flowchart illustrates the sequential logic of the core platform pipeline: from user request and authentication through hybrid recommendation scoring, basket assembly, promotional discount application, and transactional order fulfillment.
</p>
<div class="figure-container">
    <img src="diagrams/flowchart_pipeline.png" class="figure-img" style="max-height: 145mm;" alt="System Flowchart">
    <div class="figure-caption">Figure 6.1: Flowchart of Hybrid AI Recommendation and Order Processing Pipeline</div>
</div>
''', pnum=p)
    p += 1

    # Page 23: Coding Intro & base.html
    code_base = esc(get_code('templates/base.html', max_lines=75))
    add_p(f'''
<h2 class="section-title">6.3 Coding</h2>
<p>
The codebase was developed following clean code principles, strict PEP 8 formatting standards, and modular Django patterns. Representative extracts of key frontend templates and backend modules are documented below.
</p>
<h3 class="subsection-title">6.3.1 Frontend Templates</h3>
<div class="code-title">templates/base.html (Master Layout & Global Navigation)</div>
<div class="code-box">
{code_base}
</div>
''', pnum=p)
    p += 1

    # Page 24: home.html
    code_home = esc(get_code('templates/books/home.html', max_lines=75))
    add_p(f'''
<div class="code-title">templates/books/home.html (Hero Banner, Bestsellers & AI Discovery Carousels)</div>
<div class="code-box">
{code_home}
</div>
''', pnum=p)
    p += 1

    # Page 25: book_list.html
    code_list = esc(get_code('templates/books/book_list.html', max_lines=75))
    add_p(f'''
<div class="code-title">templates/books/book_list.html (Catalog Exploration, Filters & Sorting)</div>
<div class="code-box">
{code_list}
</div>
''', pnum=p)
    p += 1

    # Page 26: book_detail.html
    code_detail = esc(get_code('templates/books/book_detail.html', max_lines=75))
    add_p(f'''
<div class="code-title">templates/books/book_detail.html (Metadata, Reviews & Frequently Bought Together)</div>
<div class="code-box">
{code_detail}
</div>
''', pnum=p)
    p += 1

    # Page 27: cart_detail.html
    code_cart = esc(get_code('templates/cart/cart_detail.html', max_lines=75))
    add_p(f'''
<div class="code-title">templates/cart/cart_detail.html (Shopping Cart, Bundles & Coupon Engine)</div>
<div class="code-box">
{code_cart}
</div>
''', pnum=p)
    p += 1

    # Page 28: checkout.html
    code_check = esc(get_code('templates/orders/checkout.html', max_lines=75))
    add_p(f'''
<div class="code-title">templates/orders/checkout.html (Two-Column Checkout & Payment Simulation)</div>
<div class="code-box">
{code_check}
</div>
''', pnum=p)
    p += 1

    # Page 29: for_you.html
    code_foryou = esc(get_code('templates/recommendations/for_you.html', max_lines=75))
    add_p(f'''
<div class="code-title">templates/recommendations/for_you.html (Dedicated Personalized AI Hub)</div>
<div class="code-box">
{code_foryou}
</div>
''', pnum=p)
    p += 1

    # Page 30: dashboard.html (Analytics)
    code_dash = esc(get_code('templates/analytics/dashboard.html', max_lines=75))
    add_p(f'''
<div class="code-title">templates/analytics/dashboard.html (Store Manager Telemetry & KPI Portal)</div>
<div class="code-box">
{code_dash}
</div>
''', pnum=p)
    p += 1

    # Page 31: Backend settings.py
    code_settings = esc(get_code('bookstore_config/settings.py', max_lines=75))
    add_p(f'''
<h3 class="subsection-title">6.3.2 Backend Implementation</h3>
<div class="code-title">bookstore_config/settings.py (Core Settings & App Configurations)</div>
<div class="code-box">
{code_settings}
</div>
''', pnum=p)
    p += 1

    # Page 32: books/models.py
    code_bmodels = esc(get_code('books/models.py', max_lines=75))
    add_p(f'''
<div class="code-title">books/models.py (Author, Genre, Book, Review & Interaction Schemas)</div>
<div class="code-box">
{code_bmodels}
</div>
''', pnum=p)
    p += 1

    # Page 33: cart/models.py
    code_cmodels = esc(get_code('cart/models.py', max_lines=75))
    add_p(f'''
<div class="code-title">cart/models.py (Cart, CartItem, Coupon & Wishlist Schemas)</div>
<div class="code-box">
{code_cmodels}
</div>
''', pnum=p)
    p += 1

    # Page 34: orders/models.py
    code_omodels = esc(get_code('orders/models.py', max_lines=75))
    add_p(f'''
<div class="code-title">orders/models.py (Order & OrderItem Relational Schemas)</div>
<div class="code-box">
{code_omodels}
</div>
''', pnum=p)
    p += 1

    # Page 35: accounts/models.py
    code_amodels = esc(get_code('accounts/models.py', max_lines=75))
    add_p(f'''
<div class="code-title">accounts/models.py (UserProfile, Reading Goals & Preferences)</div>
<div class="code-box">
{code_amodels}
</div>
''', pnum=p)
    p += 1

    # Page 36: content_based.py
    code_content = esc(get_code('recommendations/services/content_based.py', max_lines=75))
    add_p(f'''
<div class="code-title">recommendations/services/content_based.py (TF-IDF Vectorizer & Cosine Similarity)</div>
<div class="code-box">
{code_content}
</div>
''', pnum=p)
    p += 1

    # Page 37: collaborative.py
    code_collab = esc(get_code('recommendations/services/collaborative.py', max_lines=75))
    add_p(f'''
<div class="code-title">recommendations/services/collaborative.py (Item-Item Collaborative Filtering)</div>
<div class="code-box">
{code_collab}
</div>
''', pnum=p)
    p += 1

    # Page 38: association.py
    code_assoc = esc(get_code('recommendations/services/association.py', max_lines=75))
    add_p(f'''
<div class="code-title">recommendations/services/association.py (Apriori Market Basket Bundle Analysis)</div>
<div class="code-box">
{code_assoc}
</div>
''', pnum=p)
    p += 1

    # Page 39: hybrid.py
    code_hybrid = esc(get_code('recommendations/services/hybrid.py', max_lines=75))
    add_p(f'''
<div class="code-title">recommendations/services/hybrid.py (Hybrid Weighted Blending & Explainability)</div>
<div class="code-box">
{code_hybrid}
</div>
''', pnum=p)
    p += 1

    # Page 40: engine.py
    code_engine = esc(get_code('recommendations/services/engine.py', max_lines=75))
    add_p(f'''
<div class="code-title">recommendations/services/engine.py (Central Orchestrator & Cold-Start Handlers)</div>
<div class="code-box">
{code_engine}
</div>
''', pnum=p)
    p += 1

    # Page 41: books/views.py
    code_bviews = esc(get_code('books/views.py', max_lines=75))
    add_p(f'''
<div class="code-title">books/views.py (Catalog Exploration, Live Autocomplete API & Reviews)</div>
<div class="code-box">
{code_bviews}
</div>
''', pnum=p)
    p += 1

    # Page 42: cart/views.py
    code_cviews = esc(get_code('cart/views.py', max_lines=75))
    add_p(f'''
<div class="code-title">cart/views.py (Cart Line-Item Operations, Coupon Redemptions & Bundles)</div>
<div class="code-box">
{code_cviews}
</div>
''', pnum=p)
    p += 1

    # Page 43: orders/views.py
    code_oviews = esc(get_code('orders/views.py', max_lines=75))
    add_p(f'''
<div class="code-title">orders/views.py (Checkout Flow, Payment Confirmation & Invoice Generation)</div>
<div class="code-box">
{code_oviews}
</div>
''', pnum=p)
    p += 1

    # Page 44: analytics/views.py
    code_anviews = esc(get_code('analytics/views.py', max_lines=75))
    add_p(f'''
<div class="code-title">analytics/views.py (Executive Dashboard Metrics, Stock Updates & Re-Sync)</div>
<div class="code-box">
{code_anviews}
</div>
''', pnum=p)
    p += 1

    # Page 45: accounts/views.py
    code_acviews = esc(get_code('accounts/views.py', max_lines=75))
    add_p(f'''
<div class="code-title">accounts/views.py (Registration, Profile Onboarding & Demo Persona Login)</div>
<div class="code-box">
{code_acviews}
</div>
''', pnum=p)
    p += 1

    # Page 46: Testing Approaches
    add_p(f'''
<h2 class="section-title">6.4 Testing Approaches</h2>
<p>
Quality assurance was conducted systematically to verify that Reader's Haven satisfies all functional requirements, security benchmarks, and algorithmic reliability standards. Testing was performed at the unit, usability, and integration levels.
</p>

<h3 class="subsection-title">6.4.1 Unit Testing</h3>
<p>
Unit testing isolated individual functions and classes to verify computational correctness:
</p>
<ul>
    <li><strong>Recommendation Math:</strong> Validated cosine similarity calculations between TF-IDF sparse vectors, ensuring values fall strictly within [0.0, 1.0].</li>
    <li><strong>Cart & Discount Math:</strong> Verified that promotional coupon <code>BOOKWORM15</code> deducts exactly 15% from the cart subtotal, taxes (5% GST) are computed accurately, and free shipping triggers at ₹499.</li>
    <li><strong>Stock Controls:</strong> Confirmed that attempting to add quantities exceeding available stock triggers a warning and clamps quantity to maximum inventory.</li>
</ul>

<h3 class="subsection-title">6.4.2 Usability Testing</h3>
<p>
Usability testing evaluated the visual clarity, responsiveness, and navigation flow of the interface across desktop, tablet, and mobile viewport resolutions. Interactive elements were tested for accessible color contrast, visual hover states, and clear form validation error messages.
</p>

<h3 class="subsection-title">6.4.3 Security & Explainability Testing</h3>
<ul>
    <li><strong>CSRF Defenses:</strong> Verified that all POST requests without valid CSRF tokens are rejected with HTTP 403 Forbidden.</li>
    <li><strong>Access Control:</strong> Confirmed that regular shoppers cannot access <code>/analytics/dashboard/</code> or <code>/admin/</code> without staff privileges.</li>
    <li><strong>Explainability Rationale:</strong> Tested <code>/recommendations/explain/&lt;id&gt;/</code> to guarantee that human-readable rationale points are returned for every recommendation.</li>
</ul>
''', pnum=p)
    p += 1

    # Page 47: Test Cases Table (Part 1)
    add_p(f'''
<h3 class="subsection-title">6.4.4 Test Cases Table</h3>
<table class="report-table">
    <thead>
        <tr>
            <th style="width: 25%;">Test Case</th>
            <th style="width: 40%;">Action / Input</th>
            <th style="width: 25%;">Expected Result</th>
            <th style="width: 10%;">Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>TC-01: User Registration</strong></td>
            <td>Submit unique username, valid email, and password</td>
            <td>Account created, auto profile initialized</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-02: User Login</strong></td>
            <td>Enter registered credentials</td>
            <td>Authenticated, redirected to homepage</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-03: Demo Persona Login</strong></td>
            <td>Click one-click persona "Alice (Sci-Fi)"</td>
            <td>Instant login as Alice with custom feed</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-04: Catalog Search</strong></td>
            <td>Search query "Dune" in catalog</td>
            <td>Relevant book cards displayed</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-05: Live Autocomplete</strong></td>
            <td>Type "clean" into global search bar</td>
            <td>Live dropdown suggestions displayed</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-06: Genre Filtering</strong></td>
            <td>Filter catalog by "Sci-Fi & Fantasy"</td>
            <td>Only matching genre books listed</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-07: Content Recs</strong></td>
            <td>Open book detail for "Dune"</td>
            <td>Thematically similar books displayed</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-08: Frequently Bought</strong></td>
            <td>Inspect book detail bundle section</td>
            <td>Companion books displayed with bundle add</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-09: Explainability API</strong></td>
            <td>Request <code>/recommendations/explain/&lt;id&gt;/</code></td>
            <td>Returns JSON with rationale points</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-10: Add to Cart</strong></td>
            <td>Click "Add to Cart" with quantity 2</td>
            <td>Cart updated, line items incremented</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-11: Stock Limitation</strong></td>
            <td>Attempt to add 99 copies of low-stock book</td>
            <td>Clamped to stock limit, warning shown</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
    </tbody>
</table>
''', pnum=p)
    p += 1

    # Page 48: Test Cases Table (Part 2) & Steps to Run
    add_p(f'''
<table class="report-table">
    <thead>
        <tr>
            <th style="width: 25%;">Test Case</th>
            <th style="width: 40%;">Action / Input</th>
            <th style="width: 25%;">Expected Result</th>
            <th style="width: 10%;">Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>TC-12: Apply Coupon</strong></td>
            <td>Enter coupon code <code>BOOKWORM15</code></td>
            <td>15% discount deducted from subtotal</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-13: Free Shipping</strong></td>
            <td>Cart total &gt; ₹499</td>
            <td>Shipping fee displayed as "FREE"</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-14: Multi-Item Bundle</strong></td>
            <td>Click "Add All 3 to Cart" on bundle</td>
            <td>All 3 books added to cart simultaneously</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-15: Wishlist Toggle</strong></td>
            <td>Click heart icon on book card</td>
            <td>Book saved to user wishlist</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-16: Checkout Flow</strong></td>
            <td>Submit shipping address and payment method</td>
            <td>Order created, stock decremented</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-17: Order Receipt</strong></td>
            <td>View order confirmation page</td>
            <td>Printable invoice with tracking displayed</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-18: Submit Review</strong></td>
            <td>Submit 5-star rating and comment</td>
            <td>Review posted, average rating updated</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-19: Reading Goal</strong></td>
            <td>Update annual reading goal in profile</td>
            <td>Goal saved, progress bar recalculated</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-20: Analytics Portal</strong></td>
            <td>Staff user visits <code>/analytics/dashboard/</code></td>
            <td>Gross sales, units sold, KPIs rendered</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-21: Re-Sync Matrix</strong></td>
            <td>Click "Re-Sync AI Matrix" on dashboard</td>
            <td>Similarity matrices recalculated live</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
        <tr>
            <td><strong>TC-22: Access Control</strong></td>
            <td>Non-staff user attempts to open dashboard</td>
            <td>HTTP 403 Forbidden / redirected</td>
            <td><strong style="color: #16a34a;">Pass</strong></td>
        </tr>
    </tbody>
</table>

<h2 class="section-title">6.5 Steps to Run the Project</h2>
<p>
The following instructions describe how to set up, configure, seed, and execute Reader's Haven on a development machine:
</p>
<ol>
    <li><strong>Clone & Navigate:</strong> Extract the project folder and open the root directory in the terminal.</li>
    <li><strong>Create Virtual Environment:</strong> Initialize and activate an isolated Python virtual environment:
        <br><code>python -m venv venv</code> &nbsp;&nbsp;|&nbsp;&nbsp; <code>.\venv\Scripts\activate</code></li>
    <li><strong>Install Dependencies:</strong> Install all required libraries:
        <br><code>pip install -r requirements.txt</code></li>
    <li><strong>Migrate Database:</strong> Apply all relational database migrations:
        <br><code>python manage.py migrate</code></li>
    <li><strong>Seed Initial Catalog Data:</strong> Populate authors, genres, books, demo personas, and interaction telemetry:
        <br><code>python manage.py seed_data</code></li>
    <li><strong>Start Development Server:</strong> Launch the local server on port 8000:
        <br><code>python manage.py runserver</code></li>
    <li><strong>Access Platform:</strong> Open <code>http://127.0.0.1:8000/</code> in any modern browser.</li>
</ol>
''', pnum=p)
    return p + 1

def get_ch7_ch9_pages(add_p, start_page=49):
    p = start_page

    # Page 49: Chapter 7 Intro & Auth
    add_p(f'''
<h1 class="chapter-title">CHAPTER 7. RESULTS</h1>
<h2 class="section-title">7.1 Introduction</h2>
<p>
The <strong>Online Bookstore Management System: Smart Commerce & AI-Powered Recommendations</strong> (Reader's Haven) was successfully engineered, integrated, and validated according to the architectural designs and functional requirements specified in preceding chapters. All six subsystem applications (<code>accounts</code>, <code>books</code>, <code>cart</code>, <code>orders</code>, <code>recommendations</code>, <code>analytics</code>) were verified in both simulated and browser runtime environments.
</p>
<p>
This chapter presents a comprehensive visual and empirical walkthrough of the operational platform through full-resolution screenshots captured from the active application.
</p>

<h2 class="section-title">7.2 Results & Screenshot Walkthrough</h2>
<h3 class="subsection-title">7.2.1 User Authentication & Demo Personas</h3>
<p>
The authentication module provides secure credential verification and password hashing. A standout usability feature is the <strong>One-Click Demo Personas selector</strong>, allowing evaluators and users to test different reading archetypes (Alice the Sci-Fi Fanatic, Bob the Fantasy Lover, Charlie the Tech Coder, and Diana the Mystery Reader) without manually re-registering.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_11_login.png" class="figure-img" style="max-height: 105mm;" alt="Login Page">
    <div class="figure-caption">Figure 7.1: User Login Page featuring One-Click Demo Personas</div>
</div>
''', pnum=p)
    p += 1

    # Page 50: Registration
    add_p(f'''
<p>
The <strong>Create Account (Registration)</strong> interface allows new readers to establish accounts with username, email, and password. Upon submission, the platform automatically initializes their user profile, connects any guest session shopping carts, and guides them into personalizing their reading preferences.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_12_register.png" class="figure-img" style="max-height: 115mm;" alt="Registration Page">
    <div class="figure-caption">Figure 7.2: User Registration and Reading Profile Onboarding Page</div>
</div>
''', pnum=p)
    p += 1

    # Page 51: Homepage
    add_p(f'''
<h3 class="subsection-title">7.2.2 Homepage & Discovery Showcase</h3>
<p>
The <strong>Homepage</strong> serves as the central showcase of the bookstore. It integrates an announcement bar offering promotional codes (<code>BOOKWORM15</code>), an expansive search bar with live autocomplete, quick category pills, an editorial hero masterpiece banner, and dynamic carousels highlighting trending volumes and personalized recommendations.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_1_homepage.png" class="figure-img" style="max-height: 115mm;" alt="Homepage">
    <div class="figure-caption">Figure 7.3: Homepage Hero Section & AI Discovery Showcase</div>
</div>
''', pnum=p)
    p += 1

    # Page 52: Catalog
    add_p(f'''
<h3 class="subsection-title">7.2.3 Book Catalog & Advanced Filtering</h3>
<p>
The <strong>Book Catalog</strong> allows visitors to explore the entire digital inventory. Shoppers can filter titles by genre (Classic Literature, Fantasy, Sci-Fi, Self-Help), book format (Hardcover, Paperback, eBook), price range, and star rating, or sort by popularity, rating, and publication date.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_2_catalog.png" class="figure-img" style="max-height: 115mm;" alt="Catalog Page">
    <div class="figure-caption">Figure 7.4: Book Catalog with Advanced Faceted Filter Sidebar</div>
</div>
''', pnum=p)
    p += 1

    # Page 53: Book Detail
    add_p(f'''
<h3 class="subsection-title">7.2.4 Book Detail, Reviews & Frequently Bought Together</h3>
<p>
The <strong>Book Detail</strong> page provides an exhaustive literary dossier for each title: publication year, page count, synopsis, author biography, ISBN, stock level, and star rating. Crucially, the page dynamically computes <em>"Frequently Bought Together"</em> companion book bundles and renders community customer reviews.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_3_book_detail.png" class="figure-img" style="max-height: 115mm;" alt="Book Detail Page">
    <div class="figure-caption">Figure 7.5: Book Detail Page with Metadata, Customer Reviews & Bundles</div>
</div>
''', pnum=p)
    p += 1

    # Page 54: For You Feed
    add_p(f'''
<h3 class="subsection-title">7.2.5 Personalized "For You" Feed & Hybrid Strategy</h3>
<p>
The dedicated <strong>"For You"</strong> portal represents the zenith of the machine learning recommendation pipeline. It dynamically tailors recommendations to the logged-in reader, displaying match percentages, transparent explainability badges, and distinct tabs representing Collaborative Filtering, Content-Based Similarity, and Popularity signals.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_4_recommendations.png" class="figure-img" style="max-height: 115mm;" alt="For You Recommendations Page">
    <div class="figure-caption">Figure 7.6: Dedicated Personalized "For You" Recommendation Feed</div>
</div>
''', pnum=p)
    p += 1

    # Page 55: Cart
    add_p(f'''
<h3 class="subsection-title">7.2.6 Shopping Cart, Coupon Engine & Bundles</h3>
<p>
The <strong>Shopping Cart</strong> interface enables seamless line-item quantity adjustments, instant deletion, and real-time coupon code redemption. Applying code <code>BOOKWORM15</code> immediately recalculates the cart total with a 15% discount, informs users of free shipping qualification (over ₹499), and computes 5% GST dynamically.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_5_cart.png" class="figure-img" style="max-height: 115mm;" alt="Shopping Cart Page">
    <div class="figure-caption">Figure 7.7: Shopping Cart with Active Line Items, Free Shipping & Discount Coupon</div>
</div>
''', pnum=p)
    p += 1

    # Page 56: Checkout
    add_p(f'''
<h3 class="subsection-title">7.2.7 Checkout & Payment Simulation</h3>
<p>
The <strong>Checkout</strong> workflow provides a streamlined two-column interface. Customers input shipping details (recipient name, address, city, state, postal code) on the left while reviewing their items, applied discounts, and simulated payment methods (Credit Card, UPI, Cash on Delivery) on the right.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_6_checkout.png" class="figure-img" style="max-height: 115mm;" alt="Checkout Page">
    <div class="figure-caption">Figure 7.8: Two-Column Checkout Workflow with Address and Order Breakdown</div>
</div>
''', pnum=p)
    p += 1

    # Page 57: Order History
    add_p(f'''
<h3 class="subsection-title">7.2.8 Order History & Printable Receipts</h3>
<p>
Upon successful order placement, the customer can review their past transactions in the <strong>Order History</strong> portal. Each order displays its unique order tracking number (e.g. <code>ORD-D108F619</code>), date, items purchased, total amount, delivery status (<em>Delivered</em>), and a one-click button to view the printable tax invoice.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_7_order_history.png" class="figure-img" style="max-height: 115mm;" alt="Order History Page">
    <div class="figure-caption">Figure 7.9: Customer Order History and Delivery Tracking Portal</div>
</div>
''', pnum=p)
    p += 1

    # Page 58: User Profile
    add_p(f'''
<h3 class="subsection-title">7.2.9 Reader Profile & Reading Challenge Tracker</h3>
<p>
The <strong>Reader Profile</strong> portal allows customers to update their biographical details, avatar, and preferred genres. It features an interactive <strong>Annual Reading Challenge</strong> progress tracker (e.g., 20 books goal) that updates automatically as books are completed, gamifying the literary experience.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_8_user_profile.png" class="figure-img" style="max-height: 115mm;" alt="Profile Page">
    <div class="figure-caption">Figure 7.10: Reader Profile with Annual Reading Challenge and Genre Tracker</div>
</div>
''', pnum=p)
    p += 1

    # Page 59: Analytics Dashboard
    add_p(f'''
<h3 class="subsection-title">7.2.10 Store Management & Analytics Telemetry</h3>
<p>
The <strong>Store Management & Analytics Dashboard</strong> provides executive oversight for bookstore administrators. It displays live Gross Sales Revenue (₹18,056.09 across 23 orders), Units Sold (61 books), Average Order Value (₹785), Catalog Rating (4.2 stars), AI Telemetry Signals (46 events), Genre Sales Distributions, and a one-click <em>Re-Sync AI Matrix</em> action button.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_9_analytics_dashboard.png" class="figure-img" style="max-height: 115mm;" alt="Analytics Dashboard">
    <div class="figure-caption">Figure 7.11: Store Management & Real-Time Analytics Telemetry Dashboard</div>
</div>
''', pnum=p)
    p += 1

    # Page 60: Django Admin & Overall Result
    add_p(f'''
<h3 class="subsection-title">7.2.11 Django Administrative Back-Office</h3>
<p>
The <strong>Django Admin Panel</strong> delivers back-office administrative power, enabling authorized staff to perform CRUD operations on Books, Authors, Genres, Orders, Coupons, and Reviews with complete audit history and relational integrity.
</p>
<div class="figure-container">
    <img src="screenshots/fig7_10_django_admin.png" class="figure-img" style="max-height: 95mm;" alt="Django Admin Panel">
    <div class="figure-caption">Figure 7.12: Django Administrative Back-Office Portal</div>
</div>

<h2 class="section-title">7.3 Overall Result</h2>
<p>
Comprehensive end-to-end testing verified that Reader's Haven successfully satisfies every functional and performance objective. The machine learning pipeline accurately categorizes book similarity, collaborative filtering matches community tastes, the checkout workflow operates reliably without race conditions, and the user interface delivers an elevated, responsive reading environment.
</p>
''', pnum=p)
    p += 1

    # Page 61: Chapter 8 Conclusion
    add_p(f'''
<h1 class="chapter-title">CHAPTER 8. CONCLUSION AND FUTURE SCOPE</h1>
<h2 class="section-title">8.1 Conclusion</h2>
<p>
The <strong>Online Bookstore Management System: Smart Commerce & AI-Powered Recommendations</strong> (Reader's Haven) was successfully designed, developed, and tested as an enterprise-grade digital bookstore web application. The project began with the observation that traditional online bookstores suffer from severe discovery friction, presenting static, generic catalogs that fail to understand the nuanced literary preferences of individual readers.
</p>
<p>
By integrating a multi-strategy machine learning recommendation engine directly into a Django 6.1 web application, Reader's Haven overcomes these limitations. The hybrid engine harmoniously combines TF-IDF synopsis vectorization for content similarity, item-item collaborative filtering for community behavior analysis, and Apriori association rule mining for basket bundles. Transparent explainability rationale empowers readers to understand why books are recommended, building lasting trust.
</p>
<p>
On the commerce front, the platform delivers a reliable, frictionless shopping experience featuring persistent carts, promotional coupon validation, atomic inventory stock decrementing, and printable receipts. The executive store analytics dashboard provides administrators with real-time telemetry on revenue, category demand, and inventory turnover. Adhering to the Spiral Model ensured that algorithmic and technical risks—such as matrix sparsity and cold-start bottlenecks—were identified and mitigated early.
</p>
<p>
The completed platform proves that modern machine learning techniques can be applied effectively within standard web frameworks to solve real-world e-commerce discovery challenges.
</p>

<h2 class="section-title">8.2 Future Scope and Enhancement</h2>
<p>
While Reader's Haven provides an exhaustive, fully functional solution, several future enhancements can expand its capabilities:
</p>
<ul>
    <li><strong>Deep Learning Sentence Transformers:</strong> Replacing classical TF-IDF with pre-trained BERT or RoBERTa sentence embeddings to capture deeper semantic relationships between book synopses.</li>
    <li><strong>Live Payment Gateway Integration:</strong> Integrating production payment gateways such as Razorpay, Stripe, or PayPal for live card and UPI settlements.</li>
    <li><strong>Automated PDF Receipt Streaming:</strong> Utilizing headless PDF rendering libraries to email branded PDF tax invoices to customers automatically upon checkout.</li>
    <li><strong>Audiobook & Digital E-Book Reader:</strong> Expanding product offerings to include streaming audiobooks and an in-browser EPUB/PDF digital reader.</li>
    <li><strong>Mobile Native Application:</strong> Developing complementary native iOS and Android applications utilizing React Native or Flutter communicating via Django REST Framework APIs.</li>
    <li><strong>Cloud Vector Database:</strong> Integrating vector database solutions (such as Pinecone or Milvus) for sub-millisecond approximate nearest neighbor (ANN) vector search across millions of book titles.</li>
</ul>
''', pnum=p)
    p += 1

    # Page 62: Chapter 9 References
    add_p(f'''
<h1 class="chapter-title">CHAPTER 9. REFERENCE</h1>
<ol style="line-height: 1.8; font-size: 11pt; margin-top: 25px;">
    <li>Django Software Foundation. <em>Django Documentation (Version 6.1)</em>. Available at: <a href="https://docs.djangoproject.com/en/6.1/">https://docs.djangoproject.com/en/6.1/</a></li>
    <li>Python Software Foundation. <em>Python 3.12 Documentation & Language Reference</em>. Available at: <a href="https://docs.python.org/3.12/">https://docs.python.org/3.12/</a></li>
    <li>Scikit-learn Developers. <em>Scikit-learn: Machine Learning in Python</em>. Available at: <a href="https://scikit-learn.org/stable/">https://scikit-learn.org/stable/</a></li>
    <li>Tailwind Labs. <em>Tailwind CSS Documentation</em>. Available at: <a href="https://tailwindcss.com/docs">https://tailwindcss.com/docs</a></li>
    <li>Lucide Community. <em>Lucide Icons: Beautiful & Consistent Vector Icons</em>. Available at: <a href="https://lucide.dev/">https://lucide.dev/</a></li>
    <li>SQLite Development Team. <em>SQLite Documentation & Architecture Guide</em>. Available at: <a href="https://www.sqlite.org/docs.html">https://www.sqlite.org/docs.html</a></li>
    <li>Mozilla Developer Network (MDN). <em>HTML5 & CSS3 Web Technology References</em>. Available at: <a href="https://developer.mozilla.org/en-US/docs/Web">https://developer.mozilla.org/en-US/docs/Web</a></li>
    <li>Charu C. Aggarwal. <em>Recommender Systems: The Textbook</em>. Springer International Publishing, 2016.</li>
    <li>Francesco Ricci, Lior Rokach, and Bracha Shapira. <em>Recommender Systems Handbook</em>. Springer, 3rd Edition, 2022.</li>
    <li>Roger S. Pressman and Bruce R. Maxim. <em>Software Engineering: A Practitioner's Approach</em>. McGraw-Hill Education, 9th Edition, 2020.</li>
    <li>Ian Sommerville. <em>Software Engineering</em>. Pearson Education, 10th Edition, 2016.</li>
    <li>Aurélien Géron. <em>Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow</em>. O'Reilly Media, 3rd Edition, 2022.</li>
    <li>Wes McKinney. <em>Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter</em>. O'Reilly Media, 3rd Edition, 2022.</li>
    <li>David Beazley. <em>Python Distilled</em>. Addison-Wesley Professional, 2021.</li>
    <li>University of Mumbai. <em>B.Sc. (Computer Science) Semester V & VI Syllabus & Project Guidelines</em>. University of Mumbai Press.</li>
</ol>
''', pnum=p)
    return p + 1

print("Chapters 6 through 9 complete.")
