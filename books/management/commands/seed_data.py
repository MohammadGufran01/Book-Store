from decimal import Decimal
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from books.models import Genre, Author, Book, Review, BookInteraction
from accounts.models import UserProfile
from cart.models import Coupon, Wishlist
from orders.models import Order, OrderItem


class Command(BaseCommand):
    help = 'Seeds database with realistic catalog, demo user personas, reviews, and orders for testing recommendations.'

    def handle(self, *args, **options):
        self.stdout.write("Starting database seeding...")

        # 1. Superuser / Admin
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@readershaven.com',
                'first_name': 'Store',
                'last_name': 'Manager',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Created admin user (admin / admin123)"))

        # 2. Coupons
        coupons_data = [
            {'code': 'BOOKWORM15', 'discount_percent': 15, 'min_spend': Decimal('499.00')},
            {'code': 'WELCOME10', 'discount_percent': 10, 'min_spend': Decimal('0.00')},
            {'code': 'BIGREADER200', 'discount_amount': Decimal('200.00'), 'min_spend': Decimal('1499.00')},
        ]
        for c_data in coupons_data:
            Coupon.objects.update_or_create(
                code=c_data['code'],
                defaults={
                    'discount_percent': c_data.get('discount_percent', 0),
                    'discount_amount': c_data.get('discount_amount', Decimal('0.00')),
                    'min_spend': c_data.get('min_spend', Decimal('0.00')),
                    'active': True
                }
            )

        # 3. Genres
        genres_data = [
            {'name': 'Science Fiction', 'icon': 'rocket', 'description': 'Explorations of future technologies, space frontiers, and time travel.'},
            {'name': 'Fantasy & Magic', 'icon': 'sparkles', 'description': 'Epic worlds, mythic quests, mythical beasts, and arcane sorcery.'},
            {'name': 'Mystery & Thriller', 'icon': 'fingerprint', 'description': 'Grips of suspense, detective inquiries, and intricate puzzles.'},
            {'name': 'Tech & Programming', 'icon': 'code-2', 'description': 'Software architecture, algorithms, AI systems, and developer craft.'},
            {'name': 'Non-Fiction & Science', 'icon': 'brain', 'description': 'Human evolution, cosmos, behavioral psychology, and astrophysics.'},
            {'name': 'Classic Literature', 'icon': 'book-open', 'description': 'Timeless prose and foundational novels that shaped world culture.'},
            {'name': 'Self-Help & Habits', 'icon': 'target', 'description': 'Personal mastery, productivity systems, mindfulness, and habits.'},
            {'name': 'History & Biography', 'icon': 'landmark', 'description': 'Extraordinary lives and monumental epochs that sculpted civilization.'},
            {'name': 'Romance & Drama', 'icon': 'heart', 'description': 'Heartfelt journeys of affection, intimacy, and emotional bonds.'},
        ]

        genre_map = {}
        for g_info in genres_data:
            genre_obj, _ = Genre.objects.get_or_create(
                name=g_info['name'],
                defaults={'icon': g_info['icon'], 'description': g_info['description']}
            )
            genre_map[g_info['name']] = genre_obj

        # 4. Authors
        authors_data = [
            {'name': 'Frank Herbert', 'born_year': '1920', 'bio': 'American science fiction author best known for the masterpiece Dune series.', 'photo_url': 'https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Isaac Asimov', 'born_year': '1920', 'bio': 'Prolific writer and biochemist renowned for Foundation and Robot series.', 'photo_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=300'},
            {'name': 'J.R.R. Tolkien', 'born_year': '1892', 'bio': 'Oxford scholar and father of modern high fantasy, creator of Middle-earth.', 'photo_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Brandon Sanderson', 'born_year': '1975', 'bio': 'Epic fantasy innovator acclaimed for Mistborn and The Stormlight Archive.', 'photo_url': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Agatha Christie', 'born_year': '1890', 'bio': 'The Queen of Mystery, creator of Hercule Poirot and Miss Marple.', 'photo_url': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Robert C. Martin', 'born_year': '1952', 'bio': 'Software pioneer, co-author of Agile Manifesto and Clean Code guru.', 'photo_url': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Martin Kleppmann', 'born_year': '1983', 'bio': 'Distributed systems researcher at University of Cambridge and author.', 'photo_url': 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&q=80&w=300'},
            {'name': 'James Clear', 'born_year': '1986', 'bio': 'Author and speaker focused on habits, decision-making, and continuous improvement.', 'photo_url': 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Yuval Noah Harari', 'born_year': '1976', 'bio': 'Historian, philosopher, and bestselling author of Sapiens.', 'photo_url': 'https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Jane Austen', 'born_year': '1775', 'bio': 'English novelist celebrated for Pride and Prejudice and social wit.', 'photo_url': 'https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Arthur Conan Doyle', 'born_year': '1859', 'bio': 'British physician and writer who created the detective Sherlock Holmes.', 'photo_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&q=80&w=300'},
            {'name': 'Walter Isaacson', 'born_year': '1952', 'bio': 'Biographer of Steve Jobs, Albert Einstein, Leonardo da Vinci, and Elon Musk.', 'photo_url': 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&q=80&w=300'},
        ]

        author_map = {}
        for a_info in authors_data:
            author_obj, _ = Author.objects.get_or_create(
                name=a_info['name'],
                defaults={'born_year': a_info['born_year'], 'bio': a_info['bio'], 'photo_url': a_info['photo_url']}
            )
            author_map[a_info['name']] = author_obj

        # 5. Books Dataset (36 Curated titles with rich synopses & covers)
        books_data = [
            # Sci-Fi
            {
                'title': 'Dune',
                'author': 'Frank Herbert',
                'genres': ['Science Fiction'],
                'price': Decimal('699.00'),
                'discount_price': Decimal('549.00'),
                'stock': 24,
                'format': 'Hardcover',
                'pages': 688,
                'publisher': 'Chilton Books',
                'publication_year': 1965,
                'cover_url': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&q=80&w=600',
                'is_featured': True,
                'is_bestseller': True,
                'synopsis': "Set on the desert planet Arrakis, Dune tells the story of Paul Atreides, a young nobleman caught in a galactic power struggle for control of the universe's most vital resource: spice melange. A triumph of world-building, politics, ecology, and prophecy."
            },
            {
                'title': 'Dune Messiah',
                'author': 'Frank Herbert',
                'genres': ['Science Fiction'],
                'price': Decimal('499.00'),
                'stock': 15,
                'format': 'Paperback',
                'pages': 336,
                'publisher': 'Putnam',
                'publication_year': 1969,
                'cover_url': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&q=80&w=600',
                'is_featured': False,
                'is_bestseller': False,
                'synopsis': "Twelve years after his ascent to Emperor of the Known Universe, Paul Atreides grapples with the fanatical jihad waged in his name, political betrayal, and the tragic consequences of prescience."
            },
            {
                'title': 'Foundation',
                'author': 'Isaac Asimov',
                'genres': ['Science Fiction'],
                'price': Decimal('599.00'),
                'discount_price': Decimal('449.00'),
                'stock': 18,
                'format': 'Paperback',
                'pages': 255,
                'publisher': 'Gnome Press',
                'publication_year': 1951,
                'cover_url': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=600',
                'is_featured': True,
                'is_bestseller': True,
                'synopsis': "Hari Seldon uses psychohistory—a mathematical science of predicting mass human behavior—to preserve human knowledge and shorten the dark ages following the collapse of the Galactic Empire."
            },
            {
                'title': 'Foundation and Empire',
                'author': 'Isaac Asimov',
                'genres': ['Science Fiction'],
                'price': Decimal('499.00'),
                'stock': 12,
                'format': 'Paperback',
                'pages': 288,
                'publisher': 'Gnome Press',
                'publication_year': 1952,
                'cover_url': 'https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&q=80&w=600',
                'synopsis': "The Foundation faces threats from the remnants of the Imperial fleet and a mysterious mutant known as the Mule, whose mental abilities shatter psychohistorical calculations."
            },
            {
                'title': 'I, Robot',
                'author': 'Isaac Asimov',
                'genres': ['Science Fiction', 'Tech & Programming'],
                'price': Decimal('450.00'),
                'stock': 20,
                'format': 'Paperback',
                'pages': 224,
                'publisher': 'Gnome Press',
                'publication_year': 1950,
                'cover_url': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&q=80&w=600',
                'synopsis': "A cornerstone of artificial intelligence literature introducing the Three Laws of Robotics through interconnected stories of robo-psychologist Dr. Susan Calvin."
            },

            # Fantasy
            {
                'title': 'The Fellowship of the Ring',
                'author': 'J.R.R. Tolkien',
                'genres': ['Fantasy & Magic', 'Classic Literature'],
                'price': Decimal('799.00'),
                'discount_price': Decimal('649.00'),
                'stock': 30,
                'format': 'Hardcover',
                'pages': 423,
                'publisher': 'Allen & Unwin',
                'publication_year': 1954,
                'cover_url': 'https://images.unsplash.com/photo-1506466010722-395aa2bef877?auto=format&fit=crop&q=80&w=600',
                'is_featured': True,
                'is_bestseller': True,
                'synopsis': "Frodo Baggins inherits the One Ring of power and embarks on a perilous quest across Middle-earth accompanied by a fellowship of hobbits, elves, dwarves, and men to destroy it in Mount Doom."
            },
            {
                'title': 'The Two Towers',
                'author': 'J.R.R. Tolkien',
                'genres': ['Fantasy & Magic', 'Classic Literature'],
                'price': Decimal('799.00'),
                'stock': 25,
                'format': 'Hardcover',
                'pages': 352,
                'publisher': 'Allen & Unwin',
                'publication_year': 1954,
                'cover_url': 'https://images.unsplash.com/photo-1514539079130-25950c84af65?auto=format&fit=crop&q=80&w=600',
                'synopsis': "The Fellowship is fractured: Frodo and Sam journey toward Mordor guided by Gollum, while Aragorn, Legolas, and Gimli rally Rohan against Saruman's armies."
            },
            {
                'title': 'The Return of the King',
                'author': 'J.R.R. Tolkien',
                'genres': ['Fantasy & Magic', 'Classic Literature'],
                'price': Decimal('799.00'),
                'stock': 22,
                'format': 'Hardcover',
                'pages': 416,
                'publisher': 'Allen & Unwin',
                'publication_year': 1955,
                'cover_url': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&q=80&w=600',
                'synopsis': "The climactic battle for Minas Tirith and Middle-earth unfolds as Frodo and Sam reach Mount Doom to end Sauron's dominion forever."
            },
            {
                'title': 'The Way of Kings',
                'author': 'Brandon Sanderson',
                'genres': ['Fantasy & Magic'],
                'price': Decimal('999.00'),
                'discount_price': Decimal('799.00'),
                'stock': 16,
                'format': 'Hardcover',
                'pages': 1007,
                'publisher': 'Tor Books',
                'publication_year': 2010,
                'cover_url': 'https://images.unsplash.com/photo-1532012164546-f432f2e3edd4?auto=format&fit=crop&q=80&w=600',
                'is_featured': True,
                'is_bestseller': True,
                'synopsis': "On Roshar, a world swept by devastating highstorms, a slave bridge-runner named Kaladin and a highprince named Dalinar must rediscover ancient radiant powers to unite a fractured kingdom."
            },
            {
                'title': 'Words of Radiance',
                'author': 'Brandon Sanderson',
                'genres': ['Fantasy & Magic'],
                'price': Decimal('999.00'),
                'stock': 14,
                'format': 'Hardcover',
                'pages': 1087,
                'publisher': 'Tor Books',
                'publication_year': 2014,
                'cover_url': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&q=80&w=600',
                'synopsis': "The Knights Radiant must stand again as the Everstorm looms and assassins stalk the rulers of the Shattered Plains."
            },
            {
                'title': 'Mistborn: The Final Empire',
                'author': 'Brandon Sanderson',
                'genres': ['Fantasy & Magic'],
                'price': Decimal('599.00'),
                'discount_price': Decimal('449.00'),
                'stock': 28,
                'format': 'Paperback',
                'pages': 541,
                'publisher': 'Tor Books',
                'publication_year': 2006,
                'cover_url': 'https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&q=80&w=600',
                'is_bestseller': True,
                'synopsis': "In a world where ash falls from the sky and the immortal Lord Ruler reigns supreme, a master thief and a street urchin use metal-based Allomantic magic to plot an impossible heist: overthrowing a god."
            },

            # Tech & Programming
            {
                'title': 'Clean Code: A Handbook of Agile Software Craftsmanship',
                'author': 'Robert C. Martin',
                'genres': ['Tech & Programming'],
                'price': Decimal('1299.00'),
                'discount_price': Decimal('999.00'),
                'stock': 20,
                'format': 'Paperback',
                'pages': 464,
                'publisher': 'Prentice Hall',
                'publication_year': 2008,
                'cover_url': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&q=80&w=600',
                'is_featured': True,
                'is_bestseller': True,
                'synopsis': "Even bad code can function. But if code isn't clean, it can bring a development organization to its knees. Learn meaningful naming, solid functions, unit testing, refactoring, and code smells."
            },
            {
                'title': 'Clean Architecture: A Craftsman\'s Guide to Software Structure',
                'author': 'Robert C. Martin',
                'genres': ['Tech & Programming'],
                'price': Decimal('1199.00'),
                'discount_price': Decimal('899.00'),
                'stock': 18,
                'format': 'Paperback',
                'pages': 432,
                'publisher': 'Prentice Hall',
                'publication_year': 2017,
                'cover_url': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&q=80&w=600',
                'synopsis': "Rules of software design, component principles, dependency inversion, and boundaries that keep enterprise systems maintainable over decades."
            },
            {
                'title': 'Designing Data-Intensive Applications',
                'author': 'Martin Kleppmann',
                'genres': ['Tech & Programming'],
                'price': Decimal('1499.00'),
                'discount_price': Decimal('1199.00'),
                'stock': 22,
                'format': 'Paperback',
                'pages': 616,
                'publisher': "O'Reilly Media",
                'publication_year': 2017,
                'cover_url': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&q=80&w=600',
                'is_featured': True,
                'is_bestseller': True,
                'synopsis': "The definitive guide to distributed databases, replication, partitioning, stream processing, transactions, and consensus protocols in high-scale cloud architectures."
            },

            # Mystery & Thriller
            {
                'title': 'Murder on the Orient Express',
                'author': 'Agatha Christie',
                'genres': ['Mystery & Thriller', 'Classic Literature'],
                'price': Decimal('399.00'),
                'discount_price': Decimal('299.00'),
                'stock': 25,
                'format': 'Paperback',
                'pages': 256,
                'publisher': 'Collins Crime Club',
                'publication_year': 1934,
                'cover_url': 'https://images.unsplash.com/photo-1476275466078-4007374efbbe?auto=format&fit=crop&q=80&w=600',
                'is_bestseller': True,
                'synopsis': "Just after midnight, a snowdrift stops the Orient Express in its tracks. In the morning, an American millionaire lies dead, stabbed a dozen times. Detective Hercule Poirot must identify the killer among twelve trapped passengers."
            },
            {
                'title': 'And Then There Were None',
                'author': 'Agatha Christie',
                'genres': ['Mystery & Thriller', 'Classic Literature'],
                'price': Decimal('399.00'),
                'discount_price': Decimal('299.00'),
                'stock': 19,
                'format': 'Paperback',
                'pages': 272,
                'publisher': 'Collins Crime Club',
                'publication_year': 1939,
                'cover_url': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&q=80&w=600',
                'is_bestseller': True,
                'synopsis': "Ten strangers are lured to an isolated island off the Devon coast. One by one, they are murdered in accordance with a sinister nursery rhyme."
            },
            {
                'title': 'The Hound of the Baskervilles',
                'author': 'Arthur Conan Doyle',
                'genres': ['Mystery & Thriller', 'Classic Literature'],
                'price': Decimal('349.00'),
                'stock': 17,
                'format': 'Paperback',
                'pages': 256,
                'publisher': 'George Newnes',
                'publication_year': 1902,
                'cover_url': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&q=80&w=600',
                'synopsis': "Sherlock Holmes and Dr. Watson investigate the legendary curse of a demonic hound haunting the eerie moors of Devonshire following the death of Sir Charles Baskerville."
            },
            {
                'title': 'A Study in Scarlet',
                'author': 'Arthur Conan Doyle',
                'genres': ['Mystery & Thriller', 'Classic Literature'],
                'price': Decimal('299.00'),
                'stock': 15,
                'format': 'Paperback',
                'pages': 192,
                'publisher': 'Ward Lock & Co',
                'publication_year': 1887,
                'cover_url': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&q=80&w=600',
                'synopsis': "The very first appearance of Sherlock Holmes and Dr. John Watson, tackling a bizarre murder in an abandoned London house tied to a tale of vengeance in the American West."
            },

            # Self-Help & Non-Fiction
            {
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'genres': ['Self-Help & Habits'],
                'price': Decimal('699.00'),
                'discount_price': Decimal('499.00'),
                'stock': 35,
                'format': 'Hardcover',
                'pages': 320,
                'publisher': 'Avery',
                'publication_year': 2018,
                'cover_url': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&q=80&w=600',
                'is_featured': True,
                'is_bestseller': True,
                'synopsis': "A transformative framework for improving every day. Learn the Four Laws of Behavior Change to build good habits, break bad ones, and master small behaviors that lead to remarkable results."
            },
            {
                'title': 'Sapiens: A Brief History of Humankind',
                'author': 'Yuval Noah Harari',
                'genres': ['Non-Fiction & Science', 'History & Biography'],
                'price': Decimal('799.00'),
                'discount_price': Decimal('599.00'),
                'stock': 26,
                'format': 'Paperback',
                'pages': 443,
                'publisher': 'Harvill Secker',
                'publication_year': 2014,
                'cover_url': 'https://images.unsplash.com/photo-1532012164546-f432f2e3edd4?auto=format&fit=crop&q=80&w=600',
                'is_featured': True,
                'is_bestseller': True,
                'synopsis': "From the Cognitive Revolution to modern biotechnology, Harari explores how an insignificant ape became the ruler of planet Earth through the superpower of shared fiction."
            },
            {
                'title': 'Homo Deus: A Brief History of Tomorrow',
                'author': 'Yuval Noah Harari',
                'genres': ['Non-Fiction & Science', 'Science Fiction'],
                'price': Decimal('749.00'),
                'stock': 18,
                'format': 'Paperback',
                'pages': 448,
                'publisher': 'Harvill Secker',
                'publication_year': 2016,
                'cover_url': 'https://images.unsplash.com/photo-1507668077129-56e32842fceb?auto=format&fit=crop&q=80&w=600',
                'synopsis': "An exploration into the future of humanity: artificial intelligence, algorithms, immortality, and the ethical dilemmas of creating godlike technologies."
            },
            {
                'title': 'Steve Jobs',
                'author': 'Walter Isaacson',
                'genres': ['History & Biography', 'Tech & Programming'],
                'price': Decimal('899.00'),
                'discount_price': Decimal('699.00'),
                'stock': 21,
                'format': 'Hardcover',
                'pages': 656,
                'publisher': 'Simon & Schuster',
                'publication_year': 2011,
                'cover_url': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=600',
                'is_bestseller': True,
                'synopsis': "The exclusive, bestselling biography based on more than forty interviews with Steve Jobs and hundreds with family, rivals, and colleagues detailing his obsessive drive for perfection."
            },

            # Romance & Classic
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'genres': ['Classic Literature', 'Romance & Drama'],
                'price': Decimal('349.00'),
                'discount_price': Decimal('249.00'),
                'stock': 32,
                'format': 'Paperback',
                'pages': 432,
                'publisher': 'T. Egerton',
                'publication_year': 1813,
                'cover_url': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&q=80&w=600',
                'is_bestseller': True,
                'synopsis': "The romantic clash between the opinionated Elizabeth Bennet and the proud, aristocratic Mr. Darcy in 19th-century England, exploring themes of social standing and true love."
            },
            {
                'title': 'Sense and Sensibility',
                'author': 'Jane Austen',
                'genres': ['Classic Literature', 'Romance & Drama'],
                'price': Decimal('349.00'),
                'stock': 19,
                'format': 'Paperback',
                'pages': 409,
                'publisher': 'Thomas Egerton',
                'publication_year': 1811,
                'cover_url': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&q=80&w=600',
                'synopsis': "The story of the Dashwood sisters, Elinor and Marianne, who embody good sense and emotional sensibility as they navigate courtship and heartbreaks."
            }
        ]

        book_objects = {}
        for b_data in books_data:
            author_obj = author_map.get(b_data['author'])
            if not author_obj:
                continue

            book_obj, created = Book.objects.update_or_create(
                title=b_data['title'],
                defaults={
                    'author': author_obj,
                    'price': b_data['price'],
                    'discount_price': b_data.get('discount_price'),
                    'stock': b_data.get('stock', 15),
                    'format': b_data.get('format', 'Paperback'),
                    'pages': b_data.get('pages', 300),
                    'publisher': b_data.get('publisher', 'Global Publishing'),
                    'publication_year': b_data.get('publication_year', 2020),
                    'cover_url': b_data.get('cover_url', ''),
                    'is_featured': b_data.get('is_featured', False),
                    'is_bestseller': b_data.get('is_bestseller', False),
                    'synopsis': b_data['synopsis'],
                    'is_active': True
                }
            )
            
            # Link genres
            book_genres = [genre_map[g_name] for g_name in b_data['genres'] if g_name in genre_map]
            book_obj.genres.set(book_genres)
            book_objects[b_data['title']] = book_obj

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(book_objects)} books."))

        # 6. Seed Demo Personas with rich reading habits
        demo_users_spec = [
            {
                'username': 'alice_scifi',
                'email': 'alice@example.com',
                'first_name': 'Alice',
                'last_name': 'Vance',
                'password': 'password123',
                'fav_genres': ['Science Fiction', 'Non-Fiction & Science'],
                'avatar_url': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=200',
                'bio': 'Passionate about hard science fiction, space operas, and astrophysics.',
                'ratings': {
                    'Dune': (5, 'A masterpiece of cosmic proportions', 'The depth of Arrakis politics and the world-building is unmatched in all of literature.'),
                    'Foundation': (5, 'Psychohistory is brilliant', 'Asimov constructed an incredible universe based on mathematical prediction.'),
                    'I, Robot': (4, 'Fascinating AI ethics', 'The three laws are timeless logic puzzles.'),
                    'Homo Deus': (4, 'Provocative look at our AI future', 'Harari raises essential philosophical questions.'),
                },
                'purchases': ['Dune', 'Foundation', 'I, Robot'],
                'wishlist': ['Dune Messiah', 'Foundation and Empire']
            },
            {
                'username': 'bob_fantasy',
                'email': 'bob@example.com',
                'first_name': 'Bob',
                'last_name': 'Brandybuck',
                'password': 'password123',
                'fav_genres': ['Fantasy & Magic', 'Classic Literature'],
                'avatar_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=200',
                'bio': 'Epic fantasy enthusiast. Currently re-reading Middle-earth and the Cosmere.',
                'ratings': {
                    'The Fellowship of the Ring': (5, 'The grandaddy of high fantasy', 'Tolkien set the standard that every modern fantasy author strives for.'),
                    'The Way of Kings': (5, 'Unbelievable stormlight epic', 'Kaladin and Dalinar are incredible characters. Sanderson at his absolute best.'),
                    'Mistborn: The Final Empire': (5, 'Unique magic system', 'Allomancy is such an original concept and the heist plot was thrilling.'),
                    'Words of Radiance': (5, 'Even better than book one!', 'The climax had me on the edge of my seat.'),
                },
                'purchases': ['The Fellowship of the Ring', 'The Way of Kings', 'Mistborn: The Final Empire'],
                'wishlist': ['The Two Towers', 'The Return of the King']
            },
            {
                'username': 'charlie_tech',
                'email': 'charlie@example.com',
                'first_name': 'Charlie',
                'last_name': 'Dev',
                'password': 'password123',
                'fav_genres': ['Tech & Programming', 'Self-Help & Habits'],
                'avatar_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&q=80&w=200',
                'bio': 'Senior Software Architect. Obsessed with clean architectures and atomic productivity.',
                'ratings': {
                    'Clean Code: A Handbook of Agile Software Craftsmanship': (5, 'Required reading for all developers', 'Completely revolutionized how I write tests and structure functions.'),
                    'Designing Data-Intensive Applications': (5, 'The bible of distributed systems', 'Explains consensus, replication, and storage engines better than any academic paper.'),
                    'Atomic Habits': (5, 'Game changing daily systems', 'The 1% daily improvement rule changed my career and focus.'),
                    'Clean Architecture: A Craftsman\'s Guide to Software Structure': (4, 'Solid architectural foundations', 'Crucial patterns for large enterprise codebases.'),
                },
                'purchases': ['Clean Code: A Handbook of Agile Software Craftsmanship', 'Designing Data-Intensive Applications', 'Atomic Habits'],
                'wishlist': ['Steve Jobs']
            },
            {
                'username': 'diana_mystery',
                'email': 'diana@example.com',
                'first_name': 'Diana',
                'last_name': 'Marple',
                'password': 'password123',
                'fav_genres': ['Mystery & Thriller', 'Classic Literature', 'Romance & Drama'],
                'avatar_url': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=200',
                'bio': 'Lover of cozy mysteries, whodunits, and 19th century English romance.',
                'ratings': {
                    'Murder on the Orient Express': (5, 'Poirot at his absolute peak', 'The ending is one of the most brilliant twists in detective history.'),
                    'And Then There Were None': (5, 'Chilling and unforgettable', 'Masterful suspense from start to finish.'),
                    'The Hound of the Baskervilles': (4, 'Classic Sherlock atmospheric gothic', 'Dartmoor atmosphere was thrilling.'),
                    'Pride and Prejudice': (5, 'Elizabeth and Darcy forever', 'Sharp social satire and enduring romance.'),
                },
                'purchases': ['Murder on the Orient Express', 'And Then There Were None', 'Pride and Prejudice'],
                'wishlist': ['A Study in Scarlet', 'Sense and Sensibility']
            }
        ]

        for u_spec in demo_users_spec:
            user_obj, u_created = User.objects.get_or_create(
                username=u_spec['username'],
                defaults={
                    'email': u_spec['email'],
                    'first_name': u_spec['first_name'],
                    'last_name': u_spec['last_name'],
                }
            )
            user_obj.set_password(u_spec['password'])
            user_obj.save()

            # Profile
            profile, _ = UserProfile.objects.get_or_create(user=user_obj)
            profile.avatar_url = u_spec['avatar_url']
            profile.bio = u_spec['bio']
            profile.address_line1 = '123 Fiction Boulevard'
            profile.city = 'Bibliopolis'
            profile.state = 'CA'
            profile.postal_code = '90210'
            profile.reading_goal = 20
            
            fav_genre_objs = [genre_map[g_name] for g_name in u_spec['fav_genres'] if g_name in genre_map]
            profile.favorite_genres.set(fav_genre_objs)
            profile.save()

            # Reviews & Ratings
            for book_title, r_info in u_spec['ratings'].items():
                if book_title in book_objects:
                    b_obj = book_objects[book_title]
                    rating_val, headline, body = r_info
                    Review.objects.update_or_create(
                        book=b_obj,
                        user=user_obj,
                        defaults={
                            'rating': rating_val,
                            'headline': headline,
                            'body': body,
                            'is_verified_purchase': True,
                            'helpful_votes': random.randint(3, 18)
                        }
                    )
                    # Log interaction
                    BookInteraction.objects.create(
                        user=user_obj,
                        book=b_obj,
                        interaction_type='rate',
                        score=float(rating_val)
                    )

            # Orders & Past Purchases
            purchased_book_objs = [book_objects[t] for t in u_spec['purchases'] if t in book_objects]
            if purchased_book_objs:
                order_subtotal = sum(b.effective_price for b in purchased_book_objs)
                order = Order.objects.create(
                    user=user_obj,
                    full_name=f"{user_obj.first_name} {user_obj.last_name}",
                    email=user_obj.email,
                    phone='+1 555-019-2834',
                    address_line1='123 Fiction Boulevard',
                    city='Bibliopolis',
                    state='CA',
                    postal_code='90210',
                    subtotal=order_subtotal,
                    total_amount=order_subtotal,
                    status='Delivered',
                    payment_status='Paid',
                    payment_method='credit_card'
                )
                for b_obj in purchased_book_objs:
                    OrderItem.objects.create(
                        order=order,
                        book=b_obj,
                        book_title=b_obj.title,
                        book_author=b_obj.author.name,
                        price=b_obj.effective_price,
                        quantity=1
                    )
                    BookInteraction.objects.create(
                        user=user_obj,
                        book=b_obj,
                        interaction_type='purchase',
                        score=5.0
                    )

            # Wishlists
            for wish_title in u_spec['wishlist']:
                if wish_title in book_objects:
                    w_obj = book_objects[wish_title]
                    Wishlist.objects.get_or_create(user=user_obj, book=w_obj)
                    BookInteraction.objects.create(
                        user=user_obj,
                        book=w_obj,
                        interaction_type='wishlist',
                        score=3.5
                    )

        # Seed market basket co-occurrences (Orders with multiple books frequently bought together)
        co_order_combos = [
            ['Dune', 'Dune Messiah', 'Foundation'],
            ['The Fellowship of the Ring', 'The Two Towers', 'The Return of the King'],
            ['Clean Code: A Handbook of Agile Software Craftsmanship', 'Clean Architecture: A Craftsman\'s Guide to Software Structure', 'Designing Data-Intensive Applications'],
            ['Murder on the Orient Express', 'And Then There Were None', 'The Hound of the Baskervilles'],
            ['Atomic Habits', 'Sapiens: A Brief History of Humankind', 'Steve Jobs'],
            ['Pride and Prejudice', 'Sense and Sensibility'],
        ]

        for combo_titles in co_order_combos:
            combo_books = [book_objects[t] for t in combo_titles if t in book_objects]
            if len(combo_books) >= 2:
                combo_subtotal = sum(b.effective_price for b in combo_books)
                mock_order = Order.objects.create(
                    full_name='Sample Customer',
                    email='customer@example.com',
                    phone='+1 555-432-1928',
                    address_line1='456 Reader Way',
                    city='Metropolis',
                    state='NY',
                    postal_code='10001',
                    subtotal=combo_subtotal,
                    total_amount=combo_subtotal,
                    status='Delivered',
                    payment_status='Paid',
                    payment_method='credit_card'
                )
                for b_obj in combo_books:
                    OrderItem.objects.create(
                        order=mock_order,
                        book=b_obj,
                        book_title=b_obj.title,
                        book_author=b_obj.author.name,
                        price=b_obj.effective_price,
                        quantity=1
                    )

        self.stdout.write(self.style.SUCCESS("Successfully seeded catalog, demo users, ratings, and orders!"))
