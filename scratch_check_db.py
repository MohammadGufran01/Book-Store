import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in c.fetchall()]
print('Tables count:', len(tables))
check_tables = [
    'books_book', 'books_author', 'books_genre', 'books_review', 'books_bookinteraction',
    'orders_order', 'orders_orderitem', 'cart_cart', 'cart_cartitem', 'cart_coupon',
    'cart_wishlist', 'auth_user', 'accounts_userprofile'
]
for t in check_tables:
    if t in tables:
        c.execute(f'SELECT count(*) FROM {t}')
        print(f'{t}: {c.fetchone()[0]} rows')
    else:
        print(f'{t}: NOT FOUND')
