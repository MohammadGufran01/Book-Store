import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Update Use Case Diagram with proper UML stick figure
fig, ax = plt.subplots(figsize=(9, 10), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 110)
ax.axis('off')

ax.text(50, 106, 'Use-Case Diagram', ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
ax.text(50, 102, "Reader's Haven - Smart Online Bookstore & AI Engine", ha='center', va='center', fontsize=10.5, color='#4b5563')

sys_box = patches.Rectangle((26, 4), 48, 94, fc='#fafafa', ec='#1f2937', lw=1.5, ls='-')
ax.add_patch(sys_box)
ax.text(50, 95.5, "Reader's Haven System Boundary", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1f2937')

def draw_actor(ax, x, y, label):
    # Head
    head = patches.Circle((x, y+4), 1.8, fc='white', ec='#1f2937', lw=1.4)
    ax.add_patch(head)
    # Body
    ax.plot([x, x], [y+2.2, y-2.5], color='#1f2937', lw=1.5)
    # Arms
    ax.plot([x-2.5, x+2.5], [y+0.5, y+0.5], color='#1f2937', lw=1.5)
    # Legs
    ax.plot([x, x-2], [y-2.5, y-6], color='#1f2937', lw=1.5)
    ax.plot([x, x+2], [y-2.5, y-6], color='#1f2937', lw=1.5)
    # Label
    ax.text(x, y-9, label, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#111827')

draw_actor(ax, 11, 55, 'Online Reader /\nShopper')
draw_actor(ax, 89, 55, 'Store Admin /\nManager')

usecases = [
    (50, 89, 'User Registration & Login'),
    (50, 81, 'Browse Catalog & Live Autocomplete'),
    (50, 73, 'View Book Details & Rationale'),
    (50, 65, 'View Personalized AI Recommendations'),
    (50, 57, 'Manage Shopping Cart & Wishlist'),
    (50, 49, 'Apply Promotional Coupons'),
    (50, 41, 'Checkout & Simulated Payment'),
    (50, 33, 'Submit Book Reviews & Ratings'),
    (50, 25, 'Manage Reading Goals & Profile'),
    (50, 17, 'Monitor Revenue Analytics & KPIs'),
    (50, 9, 'Inventory & Catalog Management')
]

for ux, uy, label in usecases:
    el = patches.Ellipse((ux, uy), 38, 5.5, fc='#ffffff', ec='#2563eb', lw=1.2)
    ax.add_patch(el)
    ax.text(ux, uy, label, ha='center', va='center', fontsize=8, color='#0f172a')

# Customer links
for i in range(9):
    uy = usecases[i][1]
    ax.plot([14, 31], [55, uy], color='#64748b', lw=1)

# Admin links
for i in [0, 9, 10]:
    uy = usecases[i][1]
    ax.plot([86, 69], [55, uy], color='#64748b', lw=1)

plt.tight_layout()
plt.savefig('report_output/diagrams/use_case_diagram.png', bbox_inches='tight')
plt.close()

# 2. Update Plagiarism graphic
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.axis('off')

ax.text(50, 44, 'PLAGIARISM REPORT', ha='center', va='center', fontsize=18, fontweight='bold', color='#111827')
ax.text(50, 39, "Reader's Haven Online Bookstore & AI Recommendation System", ha='center', va='center', fontsize=10.5, color='#6b7280')

cards = [
    (6, 'Plagiarism / Similarity', '0%', '#ef4444', '#fee2e2'),
    (29, 'Exact Match', '0%', '#f97316', '#ffedd5'),
    (52, 'Partial Match', '0%', '#3b82f6', '#dbeafe'),
    (75, 'Unique Content', '100%', '#16a34a', '#dcfce7')
]

for x, title, val, col, bg in cards:
    b = patches.FancyBboxPatch((x, 5), 19, 28, boxstyle='round,pad=1.2', fc='#ffffff', ec='#e5e7eb', lw=1.4)
    ax.add_patch(b)
    c = patches.Circle((x+9.5, 25), 3.2, fc=bg, ec=col, lw=1.2)
    ax.add_patch(c)
    ax.text(x+9.5, 25, '%', ha='center', va='center', fontsize=11, fontweight='bold', color=col)
    ax.text(x+9.5, 17, title, ha='center', va='center', fontsize=8, fontweight='bold', color='#4b5563')
    ax.text(x+9.5, 9, val, ha='center', va='center', fontsize=20, fontweight='bold', color=col)

plt.tight_layout()
plt.savefig('report_output/diagrams/fig_plagiarism.png', bbox_inches='tight')
plt.close()
print('use_case_diagram.png and fig_plagiarism.png updated successfully')
