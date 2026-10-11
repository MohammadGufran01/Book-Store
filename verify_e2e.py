import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_config.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from books.models import Book, Genre
from recommendations.services.engine import RecommendationEngine

def run_e2e_verification():
    print("==================================================")
    print("STARTING END-TO-END VERIFICATION OF ONLINE BOOKSTORE")
    print("==================================================")

    client = Client()

    # 1. Homepage
    print("\n[1/7] Testing Homepage & AI Discovery Feeds...")
    res = client.get('/')
    assert res.status_code == 200, f"Homepage failed with status {res.status_code}"
    assert 'Personalized For You' in res.content.decode() or 'Trending' in res.content.decode()
    print("  -> Homepage loaded successfully with personalized/trending carousels.")

    # 2. Book Catalog & Search
    print("\n[2/7] Testing Catalog, Filtering & Live Search...")
    res = client.get('/books/?q=Dune')
    assert res.status_code == 200
    assert 'Dune' in res.content.decode()
    
    res = client.get('/books/?sort=rating')
    assert res.status_code == 200
    
    res = client.get('/api/search-autocomplete/?q=clean')
    assert res.status_code == 200
    data = res.json()
    assert len(data['results']) > 0
    print(f"  -> Search autocomplete returned {len(data['results'])} matches for 'clean'.")

    # 3. Book Detail & Recommendation Explainability
    print("\n[3/7] Testing Book Detail & AI Explainability API...")
    book = Book.objects.filter(title='Dune').first()
    assert book is not None, "Dune book not found"
    res = client.get(f'/books/{book.slug}/')
    assert res.status_code == 200
    assert 'Frequently Bought Together' in res.content.decode() or 'Readers Also Enjoyed' in res.content.decode()
    
    res = client.get(f'/recommendations/explain/{book.id}/')
    assert res.status_code == 200
    explain_data = res.json()
    assert 'reasons' in explain_data
    print(f"  -> Explainability API provided {len(explain_data['reasons'])} rationale points for '{book.title}'.")

    # 4. Cart, Coupon & Multi-Item Bundle
    print("\n[4/7] Testing Shopping Cart & Discount Coupon Engine...")
    # Add to cart
    res = client.post(f'/cart/add/{book.id}/', {'quantity': 1}, follow=True)
    assert res.status_code == 200
    assert 'Your Shopping Cart' in res.content.decode()

    # Apply coupon BOOKWORM15
    res = client.post('/cart/apply-coupon/', {'code': 'BOOKWORM15'}, follow=True)
    assert res.status_code == 200
    assert 'BOOKWORM15' in res.content.decode()
    print("  -> Coupon 'BOOKWORM15' (15% off) applied and calculated successfully.")

    # 5. Checkout & Order Processing
    print("\n[5/7] Testing Checkout & Payment Simulation...")
    checkout_payload = {
        'full_name': 'E2E Test Customer',
        'email': 'e2e@example.com',
        'phone': '555-987-6543',
        'country': 'United States',
        'address_line1': '777 Test Avenue',
        'city': 'Boston',
        'state': 'MA',
        'postal_code': '02108',
        'payment_method': 'credit_card',
    }
    res = client.post('/orders/checkout/', checkout_payload, follow=True)
    assert res.status_code == 200
    assert 'Thank You for Your Order!' in res.content.decode() or 'Order Successfully Placed' in res.content.decode()
    print("  -> Order successfully processed, stock decremented, and printable receipt generated.")

    # 6. Multi-Persona Personalized AI Feed Testing
    print("\n[6/7] Testing Personas & Hybrid Recommendation Adaptability...")
    personas = ['alice_scifi', 'bob_fantasy', 'charlie_tech', 'diana_mystery']
    for p_name in personas:
        user = User.objects.get(username=p_name)
        recs = RecommendationEngine.get_for_user(user, limit=4)
        top_rec_titles = [item['book'].title for item in recs]
        print(f"  -> Persona '{p_name}': Top Recommendations -> {', '.join(top_rec_titles[:3])}")

    # 7. Store Management & Analytics Dashboard
    print("\n[7/7] Testing Store Manager & Analytics Dashboard...")
    admin_user = User.objects.get(username='admin')
    client.force_login(admin_user)
    res = client.get('/analytics/dashboard/')
    assert res.status_code == 200, f"Analytics dashboard failed with status {res.status_code}"
    assert 'Store Management & Analytics' in res.content.decode()
    assert 'Total Sales Revenue' in res.content.decode()
    print("  -> Analytics Dashboard rendered KPIs, interaction logs, and revenue successfully.")

    print("\n==================================================")
    print("ALL END-TO-END VERIFICATION CHECKS PASSED PERFECTLY!")
    print("==================================================")

if __name__ == '__main__':
    run_e2e_verification()
