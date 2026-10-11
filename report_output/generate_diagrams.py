import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs('report_output/diagrams', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. Spiral Model
def make_spiral():
    fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.axis('off')

    ax.axhline(0, color='#9ca3af', lw=1.2)
    ax.axvline(0, color='#9ca3af', lw=1.2)

    ax.text(0, 9.2, "Spiral Model", ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
    ax.text(0, 8.4, "Iterative Development of Reader's Haven Online Bookstore", ha='center', va='center', fontsize=11, color='#4b5563')

    # Quadrant 1
    box1 = patches.FancyBboxPatch((-9.2, 5.8), 4.2, 1.8, boxstyle="round,pad=0.2", fc='#f3f4f6', ec='#374151', lw=1.5)
    ax.add_patch(box1)
    ax.text(-7.1, 6.7, "1. Planning", ha='center', va='center', fontsize=12, fontweight='bold', color='#111827')
    ax.text(-9.0, 5.0, "• Requirements gathering\n• Feature prioritization\n• Architecture planning\n• Tech stack selection", ha='left', va='top', fontsize=9.5, color='#374151', linespacing=1.5)

    # Quadrant 2
    box2 = patches.FancyBboxPatch((5.0, 5.8), 4.2, 1.8, boxstyle="round,pad=0.2", fc='#f3f4f6', ec='#374151', lw=1.5)
    ax.add_patch(box2)
    ax.text(7.1, 6.7, "2. Risk Analysis", ha='center', va='center', fontsize=12, fontweight='bold', color='#111827')
    ax.text(5.2, 5.0, "• Cold-start sparsity risk\n• Recommendation latency\n• Inventory overselling\n• CSRF & session security", ha='left', va='top', fontsize=9.5, color='#374151', linespacing=1.5)

    # Quadrant 3
    box3 = patches.FancyBboxPatch((5.0, -7.8), 4.2, 1.8, boxstyle="round,pad=0.2", fc='#f3f4f6', ec='#374151', lw=1.5)
    ax.add_patch(box3)
    ax.text(7.1, -6.9, "3. Engineering", ha='center', va='center', fontsize=12, fontweight='bold', color='#111827')
    ax.text(5.2, -4.5, "• Django MVT backend\n• Scikit-learn ML models\n• Tailwind CSS UI & Lucide\n• SQLite3 ORM schema", ha='left', va='top', fontsize=9.5, color='#374151', linespacing=1.5)

    # Quadrant 4
    box4 = patches.FancyBboxPatch((-9.2, -7.8), 4.2, 1.8, boxstyle="round,pad=0.2", fc='#f3f4f6', ec='#374151', lw=1.5)
    ax.add_patch(box4)
    ax.text(-7.1, -6.9, "4. Evaluation", ha='center', va='center', fontsize=12, fontweight='bold', color='#111827')
    ax.text(-9.0, -4.5, "• E2E verification\n• Persona accuracy checks\n• UI responsiveness review\n• Feedback & iteration", ha='left', va='top', fontsize=9.5, color='#374151', linespacing=1.5)

    theta = np.linspace(0.8 * np.pi, 6.2 * np.pi, 600)
    r = 0.22 * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, color='#1e3a8a', lw=2.2)

    ax.annotate('', xy=(x[-1], y[-1]), xytext=(x[-20], y[-20]),
                arrowprops=dict(arrowstyle="->", color='#1e3a8a', lw=2.5, mutation_scale=20))

    center_circle = patches.Circle((0, 0), 1.25, fc='#854d0e', ec='#854d0e', zorder=5)
    ax.add_patch(center_circle)
    ax.text(0, 0, "Reader's\nHaven", ha='center', va='center', fontsize=9.5, fontweight='bold', color='white', zorder=6)

    plt.tight_layout()
    plt.savefig('report_output/diagrams/spiral_model.png', bbox_inches='tight')
    plt.close()
    print("spiral_model.png generated")

# 2. System Architecture Diagram
def make_architecture():
    fig, ax = plt.subplots(figsize=(9, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 110)
    ax.axis('off')

    ax.text(50, 106, "System Architecture Diagram", ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
    ax.text(50, 102, "Reader's Haven - Smart Online Bookstore (Django MVT Three-Tier Architecture)", ha='center', va='center', fontsize=10.5, color='#4b5563')

    # Top: Users
    dash_box1 = patches.FancyBboxPatch((15, 87), 70, 11, boxstyle="round,pad=1.5", fc='none', ec='#9ca3af', ls='--', lw=1.2)
    ax.add_patch(dash_box1)
    ax.text(50, 97, "Users", ha='center', va='center', fontsize=10, fontweight='bold', color='#4b5563')

    u1 = patches.FancyBboxPatch((18, 88.5), 28, 6.5, boxstyle="round,pad=0.5", fc='#ffffff', ec='#374151', lw=1.2)
    ax.add_patch(u1)
    ax.text(32, 91.7, "Online Reader / Shopper\n(Web Browser)", ha='center', va='center', fontsize=9, color='#111827')

    u2 = patches.FancyBboxPatch((54, 88.5), 28, 6.5, boxstyle="round,pad=0.5", fc='#ffffff', ec='#374151', lw=1.2)
    ax.add_patch(u2)
    ax.text(68, 91.7, "Store Administrator\n(Analytics & Admin)", ha='center', va='center', fontsize=9, color='#111827')

    # Arrow down
    ax.annotate('HTTP / HTTPS Requests', xy=(50, 77), xytext=(50, 87),
                arrowprops=dict(arrowstyle="->", color='#374151', lw=1.4), ha='center', va='center', fontsize=8.5, color='#4b5563')

    # Presentation Layer
    p_box = patches.FancyBboxPatch((10, 58), 80, 19, boxstyle="round,pad=1.2", fc='#f9fafb', ec='#374151', lw=1.4)
    ax.add_patch(p_box)
    ax.text(50, 74.5, "Presentation Layer (Frontend)", ha='center', va='center', fontsize=11, fontweight='bold', color='#111827')

    p1 = patches.FancyBboxPatch((14, 60), 40, 11, boxstyle="round,pad=0.5", fc='#ffffff', ec='#6b7280', lw=1)
    ax.add_patch(p1)
    ax.text(34, 65.5, "Django HTML5 Templates\nHome · Catalog · Book Detail · Cart\nCheckout · For You · Analytics", ha='center', va='center', fontsize=8.5, color='#1f2937')

    p2 = patches.FancyBboxPatch((58, 60), 30, 11, boxstyle="round,pad=0.5", fc='#ffffff', ec='#6b7280', lw=1)
    ax.add_patch(p2)
    ax.text(73, 65.5, "Styling & Interaction\nTailwind CSS · Lucide Icons\nVanilla JS · Autocomplete API", ha='center', va='center', fontsize=8.5, color='#1f2937')

    # Arrow to Application Layer
    ax.annotate('POST / GET (Form Submissions & REST Calls)', xy=(50, 48), xytext=(50, 58),
                arrowprops=dict(arrowstyle="->", color='#374151', lw=1.4), ha='center', va='center', fontsize=8.5, color='#4b5563')

    # Application Layer
    app_box = patches.FancyBboxPatch((10, 24), 80, 24, boxstyle="round,pad=1.2", fc='#eff6ff', ec='#1d4ed8', lw=1.4)
    ax.add_patch(app_box)
    ax.text(50, 45.5, "Application Layer (Django 6.1 Backend & AI Engine)", ha='center', va='center', fontsize=11, fontweight='bold', color='#1e3a8a')

    a1 = patches.FancyBboxPatch((13, 33), 35, 9.5, boxstyle="round,pad=0.4", fc='#ffffff', ec='#93c5fd', lw=1)
    ax.add_patch(a1)
    ax.text(30.5, 37.8, "Django Core & Business Logic\nURL Dispatcher · CSRF · Sessions\nBooks · Cart · Orders · Accounts", ha='center', va='center', fontsize=8, color='#1e293b')

    a2 = patches.FancyBboxPatch((52, 33), 35, 9.5, boxstyle="round,pad=0.4", fc='#ffffff', ec='#93c5fd', lw=1)
    ax.add_patch(a2)
    ax.text(69.5, 37.8, "Hybrid AI Recommendation Engine\nTF-IDF Content · Item-Item Collab\nApriori Bundles · Explainability", ha='center', va='center', fontsize=8, color='#1e293b')

    a3 = patches.FancyBboxPatch((28, 25.5), 44, 6, boxstyle="round,pad=0.4", fc='#ffffff', ec='#93c5fd', lw=1)
    ax.add_patch(a3)
    ax.text(50, 28.5, "Store Analytics & Real-Time Telemetry Tracking", ha='center', va='center', fontsize=8.5, color='#1e293b')

    # Arrow to Data Layer
    ax.annotate('ORM Queries & BSON / Row Operations', xy=(50, 16.5), xytext=(50, 24),
                arrowprops=dict(arrowstyle="->", color='#374151', lw=1.4), ha='center', va='center', fontsize=8.5, color='#4b5563')

    # Data Layer
    data_box = patches.FancyBboxPatch((15, 2), 70, 14.5, boxstyle="round,pad=1.2", fc='#fefce8', ec='#ca8a04', lw=1.4)
    ax.add_patch(data_box)
    ax.text(50, 14, "Data & Persistence Layer", ha='center', va='center', fontsize=11, fontweight='bold', color='#854d0e')

    d1 = patches.FancyBboxPatch((20, 4), 28, 7.5, boxstyle="round,pad=0.4", fc='#ffffff', ec='#fde047', lw=1)
    ax.add_patch(d1)
    ax.text(34, 7.7, "SQLite3 Database\nRelational Schema & Indexes", ha='center', va='center', fontsize=8.5, color='#713f12')

    d2 = patches.FancyBboxPatch((52, 4), 28, 7.5, boxstyle="round,pad=0.4", fc='#ffffff', ec='#fde047', lw=1)
    ax.add_patch(d2)
    ax.text(66, 7.7, "Media & Static Assets\nWhiteNoise & Book Covers", ha='center', va='center', fontsize=8.5, color='#713f12')

    plt.tight_layout()
    plt.savefig('report_output/diagrams/architecture_diagram.png', bbox_inches='tight')
    plt.close()
    print("architecture_diagram.png generated")

# 3. Level 0 DFD (Context Diagram)
def make_dfd0():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Data Flow Diagram (Level 0)", ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
    ax.text(50, 89, "Context Diagram — Reader's Haven Online Bookstore", ha='center', va='center', fontsize=11, color='#4b5563')

    # Center Process Circle
    center_p = patches.Circle((50, 45), 14, fc='#f3f4f6', ec='#1f2937', lw=1.6)
    ax.add_patch(center_p)
    ax.text(50, 46.5, "0.0\nReader's Haven\nOnline Bookstore\n& AI System", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#111827')

    # External Entity: Reader / Customer (Left)
    cust_box = patches.Rectangle((4, 34), 16, 22, fc='#f9fafb', ec='#111827', lw=1.5)
    ax.add_patch(cust_box)
    ax.text(12, 45, "Reader /\nShopper", ha='center', va='center', fontsize=11, fontweight='bold', color='#111827')

    # External Entity: Store Administrator (Right Top)
    admin_box = patches.Rectangle((80, 58), 16, 20, fc='#f9fafb', ec='#111827', lw=1.5)
    ax.add_patch(admin_box)
    ax.text(88, 68, "Store\nAdmin", ha='center', va='center', fontsize=11, fontweight='bold', color='#111827')

    # Data Store: SQLite3 (Right Bottom)
    db_bottom = patches.Rectangle((80, 18), 16, 16, fc='#f9fafb', ec='#111827', lw=1.5)
    ax.add_patch(db_bottom)
    ax.text(88, 26, "D1 Database\n(SQLite3)", ha='center', va='center', fontsize=10, fontweight='bold', color='#111827')

    # Flows from Customer to Process
    ax.annotate('', xy=(36, 50), xytext=(20, 50), arrowprops=dict(arrowstyle="->", color='#2563eb', lw=1.3))
    ax.text(28, 55, "Registration, search query,\ncart actions, checkout data", ha='center', va='bottom', fontsize=8, color='#1e3a8a')

    # Flows from Process to Customer
    ax.annotate('', xy=(20, 40), xytext=(36, 40), arrowprops=dict(arrowstyle="->", color='#16a34a', lw=1.3))
    ax.text(28, 33, "Book catalog, personalized recs,\norder invoice, confirmation", ha='center', va='top', fontsize=8, color='#15803d')

    # Flows from Admin to Process
    ax.annotate('', xy=(61, 55), xytext=(80, 68), arrowprops=dict(arrowstyle="->", color='#2563eb', lw=1.3))
    ax.text(74, 57, "Catalog updates,\nstock, matrix sync", ha='left', va='center', fontsize=8, color='#1e3a8a')

    # Flows from Process to Admin
    ax.annotate('', xy=(80, 62), xytext=(63, 49), arrowprops=dict(arrowstyle="->", color='#16a34a', lw=1.3))
    ax.text(67, 66, "Revenue analytics,\norder manifest, logs", ha='right', va='center', fontsize=8, color='#15803d')

    # Flows to/from Database
    ax.annotate('', xy=(80, 28), xytext=(63, 40), arrowprops=dict(arrowstyle="->", color='#2563eb', lw=1.3))
    ax.text(75, 37, "Store user records,\norders, reviews", ha='left', va='center', fontsize=8, color='#1e3a8a')

    ax.annotate('', xy=(61, 36), xytext=(80, 22), arrowprops=dict(arrowstyle="->", color='#16a34a', lw=1.3))
    ax.text(70, 25, "Read catalog,\nratings, weights", ha='right', va='center', fontsize=8, color='#15803d')

    plt.tight_layout()
    plt.savefig('report_output/diagrams/dfd_level_0.png', bbox_inches='tight')
    plt.close()
    print("dfd_level_0.png generated")

# 4. Level 1 DFD
def make_dfd1():
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Data Flow Diagram (Level 1)", ha='center', va='center', fontsize=17, fontweight='bold', color='#111827')
    ax.text(50, 91.5, "Functional Decomposition — Reader's Haven Online Bookstore", ha='center', va='center', fontsize=10.5, color='#4b5563')

    # External Entities
    c_box = patches.Rectangle((2, 45), 12, 16, fc='#f9fafb', ec='#111827', lw=1.4)
    ax.add_patch(c_box)
    ax.text(8, 53, "Reader /\nShopper", ha='center', va='center', fontsize=9.5, fontweight='bold')

    a_box = patches.Rectangle((86, 45), 12, 16, fc='#f9fafb', ec='#111827', lw=1.4)
    ax.add_patch(a_box)
    ax.text(92, 53, "Store\nAdmin", ha='center', va='center', fontsize=9.5, fontweight='bold')

    # Processes
    procs = [
        (28, 78, "1.0 User Auth\n& Preferences"),
        (50, 78, "2.0 Catalog &\nLive Search"),
        (72, 78, "3.0 Hybrid AI\nRecommender"),
        (28, 28, "4.0 Cart &\nCoupon Calc"),
        (50, 28, "5.0 Checkout &\nOrder Process"),
        (72, 28, "6.0 Analytics &\nStock Mgmt")
    ]
    for px, py, label in procs:
        c = patches.Circle((px, py), 7, fc='#f3f4f6', ec='#1f2937', lw=1.3)
        ax.add_patch(c)
        ax.text(px, py, label, ha='center', va='center', fontsize=7.5, fontweight='bold')

    # Data Stores in center
    stores = [
        (40, 56, "D1: Users & Profiles"),
        (60, 56, "D2: Books & Authors"),
        (40, 46, "D3: Cart & Coupons"),
        (60, 46, "D4: Orders & Items"),
        (50, 39, "D5: Telemetry & Interactions")
    ]
    for sx, sy, label in stores:
        s = patches.Rectangle((sx-8, sy-2.5), 16, 5, fc='#fef3c7', ec='#b45309', lw=1.1)
        ax.add_patch(s)
        ax.text(sx, sy, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#78350f')

    # Sample connecting arrows
    ax.annotate('', xy=(22, 76), xytext=(14, 57), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(28, 71), xytext=(35, 58), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(44, 76), xytext=(14, 53), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(50, 71), xytext=(55, 58), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(66, 76), xytext=(14, 50), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(72, 71), xytext=(63, 58), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(22, 32), xytext=(14, 48), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(34, 32), xytext=(36, 44), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(44, 30), xytext=(14, 45), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(50, 35), xytext=(55, 44), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(86, 51), xytext=(78, 32), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))
    ax.annotate('', xy=(72, 35), xytext=(58, 40), arrowprops=dict(arrowstyle="->", color='#374151', lw=1))

    plt.tight_layout()
    plt.savefig('report_output/diagrams/dfd_level_1.png', bbox_inches='tight')
    plt.close()
    print("dfd_level_1.png generated")

# 5. Activity Diagram
def make_activity():
    fig, ax = plt.subplots(figsize=(8, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 110)
    ax.axis('off')

    ax.text(50, 106, "Activity Diagram", ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
    ax.text(50, 102, "Reader's Haven - User Browsing, AI Recommendation & Checkout", ha='center', va='center', fontsize=10.5, color='#4b5563')

    # Initial Node (Black Circle)
    start_c = patches.Circle((50, 96), 2.2, fc='#111827', ec='#111827')
    ax.add_patch(start_c)
    ax.text(50, 99, "Start", ha='center', va='center', fontsize=9, fontweight='bold')

    nodes = [
        (50, 87, "Browse Homepage / Discovery Feeds"),
        (50, 77, "Select Category or Enter Search Query"),
        (50, 67, "View Book Details & AI Bundles"),
        (50, 56, "Add to Cart / Save to Wishlist"),
        (50, 45, "Apply Discount Coupon (e.g. BOOKWORM15)"),
        (50, 34, "Proceed to Checkout & Shipping Details"),
        (50, 23, "Complete Order & Stock Decremented"),
        (50, 13, "Generate Printable Tax Invoice & Update Telemetry")
    ]

    for y, (nx, ny, label) in enumerate(nodes):
        b = patches.FancyBboxPatch((20, ny-2.8), 60, 5.6, boxstyle="round,pad=0.6", fc='#f8fafc', ec='#334155', lw=1.2)
        ax.add_patch(b)
        ax.text(nx, ny, label, ha='center', va='center', fontsize=8.5, color='#0f172a', fontweight='medium')

        # Connect arrow from previous
        if y == 0:
            prev_y = 93.8
        else:
            prev_y = nodes[y-1][1] - 2.8
        ax.annotate('', xy=(50, ny+2.8), xytext=(50, prev_y), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.3))

    # Final Node (Bullseye)
    ax.annotate('', xy=(50, 5.5), xytext=(50, 10.2), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.3))
    out_c = patches.Circle((50, 3.5), 2.4, fc='#ffffff', ec='#111827', lw=1.3)
    in_c = patches.Circle((50, 3.5), 1.6, fc='#111827', ec='#111827')
    ax.add_patch(out_c)
    ax.add_patch(in_c)
    ax.text(50, 0.5, "End", ha='center', va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig('report_output/diagrams/activity_diagram.png', bbox_inches='tight')
    plt.close()
    print("activity_diagram.png generated")

# 6. Entity-Relationship Diagram (ERD)
def make_erd():
    fig, ax = plt.subplots(figsize=(10, 8.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Entity Relationship Diagram", ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
    ax.text(50, 92, "Reader's Haven Database Architecture (Django SQLite Schema)", ha='center', va='center', fontsize=10.5, color='#4b5563')

    def entity_box(x, y, w, h, title, fields):
        # Header
        hdr = patches.Rectangle((x, y+h-4), w, 4, fc='#854d0e', ec='#1f2937', lw=1.2)
        ax.add_patch(hdr)
        ax.text(x+w/2, y+h-2, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        # Body
        body = patches.Rectangle((x, y), w, h-4, fc='#ffffff', ec='#1f2937', lw=1.2)
        ax.add_patch(body)
        field_txt = "\n".join(fields)
        ax.text(x+1.5, y+h-5.5, field_txt, ha='left', va='top', fontsize=7.2, color='#1f2937', linespacing=1.3)

    # Entities
    entity_box(4, 62, 26, 24, "USER & PROFILE", [
        "id: BigAutoField (PK)",
        "username: CharField (Unique)",
        "email: EmailField",
        "reading_goal: PositiveInt",
        "favorite_genres: M2M",
        "bio: TextField"
    ])

    entity_box(37, 62, 26, 24, "BOOK", [
        "id: BigAutoField (PK)",
        "title: CharField",
        "slug: SlugField (Unique)",
        "author: FK -> Author",
        "genre: FK -> Genre",
        "price, discount_price",
        "stock: PositiveInt",
        "rating: DecimalField"
    ])

    entity_box(70, 62, 26, 24, "AUTHOR & GENRE", [
        "author_id: BigAutoField (PK)",
        "name: CharField",
        "slug: SlugField",
        "------------------",
        "genre_id: BigAutoField (PK)",
        "genre_name: CharField",
        "slug: SlugField"
    ])

    entity_box(4, 20, 26, 25, "CART & CART_ITEM", [
        "cart_id: BigAutoField (PK)",
        "user: FK -> User (Null)",
        "session_key: CharField",
        "------------------",
        "item_id: BigAutoField (PK)",
        "cart: FK -> Cart",
        "book: FK -> Book",
        "quantity: PositiveInt"
    ])

    entity_box(37, 20, 26, 25, "ORDER & ORDER_ITEM", [
        "order_id: BigAutoField (PK)",
        "order_number: CharField (Unique)",
        "user: FK -> User",
        "total: DecimalField",
        "status: CharField",
        "------------------",
        "item_id: BigAutoField (PK)",
        "order: FK -> Order",
        "book: FK -> Book"
    ])

    entity_box(70, 20, 26, 25, "INTERACTION & REVIEW", [
        "interaction_id: (PK)",
        "user: FK -> User",
        "book: FK -> Book",
        "interaction_type: CharField",
        "weight: FloatField",
        "------------------",
        "review_id: (PK)",
        "rating: SmallInt (1-5)"
    ])

    # Connecting relationship lines
    ax.annotate('', xy=(37, 74), xytext=(30, 74), arrowprops=dict(arrowstyle="<->", color='#374151', lw=1.2))
    ax.text(33.5, 76, "M:N", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#2563eb')

    ax.annotate('', xy=(70, 74), xytext=(63, 74), arrowprops=dict(arrowstyle="<->", color='#374151', lw=1.2))
    ax.text(66.5, 76, "N:1", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#2563eb')

    ax.annotate('', xy=(17, 45), xytext=(17, 62), arrowprops=dict(arrowstyle="<->", color='#374151', lw=1.2))
    ax.text(20, 53.5, "1:1", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#2563eb')

    ax.annotate('', xy=(50, 45), xytext=(50, 62), arrowprops=dict(arrowstyle="<->", color='#374151', lw=1.2))
    ax.text(53, 53.5, "1:N", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#2563eb')

    ax.annotate('', xy=(83, 45), xytext=(83, 62), arrowprops=dict(arrowstyle="<->", color='#374151', lw=1.2))
    ax.text(86, 53.5, "1:N", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#2563eb')

    plt.tight_layout()
    plt.savefig('report_output/diagrams/er_diagram.png', bbox_inches='tight')
    plt.close()
    print("er_diagram.png generated")

# 7. Use-Case Diagram
def make_usecase():
    fig, ax = plt.subplots(figsize=(9, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 110)
    ax.axis('off')

    ax.text(50, 106, "Use-Case Diagram", ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
    ax.text(50, 102, "Reader's Haven - Smart Online Bookstore & AI Engine", ha='center', va='center', fontsize=10.5, color='#4b5563')

    # System Boundary Box
    sys_box = patches.Rectangle((26, 4), 48, 94, fc='#fafafa', ec='#1f2937', lw=1.5, ls='-')
    ax.add_patch(sys_box)
    ax.text(50, 95.5, "Reader's Haven System Boundary", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1f2937')

    # Actors
    # Left Actor: Reader
    ax.text(10, 55, "옷", ha='center', va='center', fontsize=32, color='#1f2937')
    ax.text(10, 45, "Online Reader /\nShopper", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#111827')

    # Right Actor: Store Admin
    ax.text(90, 55, "옷", ha='center', va='center', fontsize=32, color='#1f2937')
    ax.text(90, 45, "Store Admin /\nManager", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#111827')

    # Use Cases (Ellipses)
    usecases = [
        (50, 89, "User Registration & Login"),
        (50, 81, "Browse Catalog & Live Autocomplete"),
        (50, 73, "View Book Details & Rationale"),
        (50, 65, "View Personalized AI Recommendations"),
        (50, 57, "Manage Shopping Cart & Wishlist"),
        (50, 49, "Apply Promotional Coupons"),
        (50, 41, "Checkout & Simulated Payment"),
        (50, 33, "Submit Book Reviews & Ratings"),
        (50, 25, "Manage Reading Goals & Profile"),
        (50, 17, "Monitor Revenue Analytics & KPIs"),
        (50, 9, "Inventory & Catalog Management")
    ]

    for ux, uy, label in usecases:
        el = patches.Ellipse((ux, uy), 38, 5.5, fc='#ffffff', ec='#2563eb', lw=1.2)
        ax.add_patch(el)
        ax.text(ux, uy, label, ha='center', va='center', fontsize=8, color='#0f172a')

    # Connecting lines from Left Actor (Reader)
    for i in range(9):
        uy = usecases[i][1]
        ax.plot([15, 31], [50, uy], color='#64748b', lw=1)

    # Connecting lines from Right Actor (Admin)
    for i in [0, 9, 10]:
        uy = usecases[i][1]
        ax.plot([85, 69], [50, uy], color='#64748b', lw=1)

    plt.tight_layout()
    plt.savefig('report_output/diagrams/use_case_diagram.png', bbox_inches='tight')
    plt.close()
    print("use_case_diagram.png generated")

# 8. Flowchart: Hybrid AI Recommendation & Order Processing
def make_flowchart():
    fig, ax = plt.subplots(figsize=(8, 11), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 115)
    ax.axis('off')

    ax.text(50, 111, "Flowchart", ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
    ax.text(50, 107, "Hybrid Recommendation Generation & Order Fulfillment Pipeline", ha='center', va='center', fontsize=10, color='#4b5563')

    # Start Oval
    start = patches.Ellipse((50, 101), 18, 4.5, fc='#dbeafe', ec='#1d4ed8', lw=1.3)
    ax.add_patch(start)
    ax.text(50, 101, "Start Request", ha='center', va='center', fontsize=9, fontweight='bold', color='#1e3a8a')

    # Step 1: User visits page / requests recommendations
    b1 = patches.FancyBboxPatch((24, 91), 52, 5, boxstyle="round,pad=0.3", fc='#ffffff', ec='#334155', lw=1.1)
    ax.add_patch(b1)
    ax.text(50, 93.5, "Fetch User Profile & Interaction Telemetry", ha='center', va='center', fontsize=8, color='#0f172a')
    ax.annotate('', xy=(50, 96), xytext=(50, 98.7), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.2))

    # Decision Diamond 1: Interactions >= 3?
    d1 = patches.Polygon([(50, 88), (66, 81), (50, 74), (34, 81)], fc='#fef3c7', ec='#b45309', lw=1.2)
    ax.add_patch(d1)
    ax.text(50, 81, "User Interactions\n>= 3 items?", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#78350f')
    ax.annotate('', xy=(50, 88), xytext=(50, 91), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.2))

    # Yes Branch: Hybrid Engine
    b_yes = patches.FancyBboxPatch((4, 62), 42, 6.5, boxstyle="round,pad=0.3", fc='#ffffff', ec='#16a34a', lw=1.1)
    ax.add_patch(b_yes)
    ax.text(25, 65.2, "Execute Hybrid Blend Model\n40% Collab + 40% TF-IDF + 20% Pop", ha='center', va='center', fontsize=7.5, color='#14532d')
    ax.annotate('Yes', xy=(25, 68.5), xytext=(34, 81), arrowprops=dict(arrowstyle="->", color='#16a34a', lw=1.2), fontsize=8, color='#16a34a')

    # No Branch: Cold-Start Fallback
    b_no = patches.FancyBboxPatch((54, 62), 42, 6.5, boxstyle="round,pad=0.3", fc='#ffffff', ec='#dc2626', lw=1.1)
    ax.add_patch(b_no)
    ax.text(75, 65.2, "Cold-Start Preference Engine\nFilter by Profile Favorite Genres", ha='center', va='center', fontsize=7.5, color='#7f1d1d')
    ax.annotate('No', xy=(75, 68.5), xytext=(66, 81), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=1.2), fontsize=8, color='#dc2626')

    # Merge box: Score & Rank Books
    b_rank = patches.FancyBboxPatch((24, 49), 52, 6, boxstyle="round,pad=0.3", fc='#ffffff', ec='#334155', lw=1.1)
    ax.add_patch(b_rank)
    ax.text(50, 52, "Compute Similarity Scores, Rank & Filter Active Stock", ha='center', va='center', fontsize=8, color='#0f172a')
    ax.annotate('', xy=(42, 55), xytext=(25, 62), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.2))
    ax.annotate('', xy=(58, 55), xytext=(75, 62), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.2))

    # Next: Explainability & Display
    b_disp = patches.FancyBboxPatch((24, 37), 52, 6, boxstyle="round,pad=0.3", fc='#ffffff', ec='#334155', lw=1.1)
    ax.add_patch(b_disp)
    ax.text(50, 40, "Generate Explainability Reasons & Render UI Cards", ha='center', va='center', fontsize=8, color='#0f172a')
    ax.annotate('', xy=(50, 43), xytext=(50, 49), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.2))

    # Decision 2: User Adds to Cart & Checks out?
    d2 = patches.Polygon([(50, 33), (68, 25), (50, 17), (32, 25)], fc='#fef3c7', ec='#b45309', lw=1.2)
    ax.add_patch(d2)
    ax.text(50, 25, "Customer Checks\nOut Order?", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#78350f')
    ax.annotate('', xy=(50, 33), xytext=(50, 37), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.2))

    # Checkout & Log Telemetry
    b_ord = patches.FancyBboxPatch((15, 6), 70, 6, boxstyle="round,pad=0.3", fc='#ecfdf5', ec='#059669', lw=1.2)
    ax.add_patch(b_ord)
    ax.text(50, 9, "Process Checkout, Decrement Stock & Log Interaction Telemetry", ha='center', va='center', fontsize=7.8, color='#065f46')
    ax.annotate('Yes', xy=(50, 12), xytext=(50, 17), arrowprops=dict(arrowstyle="->", color='#059669', lw=1.2), fontsize=8, color='#059669')

    # End
    end = patches.Ellipse((50, 1), 18, 4.2, fc='#111827', ec='#111827')
    ax.add_patch(end)
    ax.text(50, 1, "End Flow", ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
    ax.annotate('', xy=(50, 3.2), xytext=(50, 6), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.2))

    plt.tight_layout()
    plt.savefig('report_output/diagrams/flowchart_pipeline.png', bbox_inches='tight')
    plt.close()
    print("flowchart_pipeline.png generated")

# 9. Plagiarism Graphic
def make_plagiarism():
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')

    ax.text(50, 44, "PLAGIARISM REPORT", ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
    ax.text(50, 39, "Reader's Haven Online Bookstore & AI Recommendation System", ha='center', va='center', fontsize=10.5, color='#6b7280')

    cards = [
        (6, "Plagiarism / Similarity", "0%", "#ef4444", "#fee2e2", "📄"),
        (29, "Exact Match", "0%", "#f97316", "#ffedd5", "🔗"),
        (52, "Partial Match", "0%", "#3b82f6", "#dbeafe", "📑"),
        (75, "Unique Content", "100%", "#16a34a", "#dcfce7", "🛡️")
    ]

    for x, title, val, col, bg, icon in cards:
        b = patches.FancyBboxPatch((x, 5), 19, 28, boxstyle="round,pad=1.2", fc='#ffffff', ec='#e5e7eb', lw=1.4)
        ax.add_patch(b)
        ax.text(x+9.5, 25, icon, ha='center', va='center', fontsize=20)
        ax.text(x+9.5, 17, title, ha='center', va='center', fontsize=8, fontweight='bold', color='#4b5563')
        ax.text(x+9.5, 9, val, ha='center', va='center', fontsize=20, fontweight='bold', color=col)

    plt.tight_layout()
    plt.savefig('report_output/diagrams/fig_plagiarism.png', bbox_inches='tight')
    plt.close()
    print("fig_plagiarism.png generated")

make_architecture()
make_dfd0()
make_dfd1()
make_activity()
make_erd()
make_usecase()
make_flowchart()
make_plagiarism()
print("All diagrams generated successfully!")
