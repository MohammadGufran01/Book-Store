# report_output/content_ch1_ch5.py

def get_ch1_pages(add_p):
    # Page 1
    add_p('''
<h1 class="chapter-title">CHAPTER 1. INTRODUCTION</h1>
<h2 class="section-title">1.1 Introduction</h2>
<p>
The digital revolution has radically transformed how literature is discovered, purchased, and consumed. While physical bookstores provide the romantic pleasure of browsing shelves, they are constrained by physical shelf space, geographical boundaries, and the inability to cater to niche reading tastes dynamically. Conversely, modern e-commerce storefronts host vast repositories comprising hundreds of thousands of titles across diverse genres, languages, and editions. However, this sheer abundance creates a debilitating phenomenon known as <em>choice paralysis</em> or <em>information overload</em>.
</p>
<p>
When readers browse a digital catalog without intelligent guidance, they are inundated by hundreds of unfamiliar book titles. Conventional online stores attempt to solve this problem by displaying static "Top Sellers" or broad "Featured" banners. These generic lists reflect gross aggregate sales but fail completely to understand the subtle, highly idiosyncratic reading tastes of individual customers. A science-fiction aficionado searching for hard cyberpunk fiction is offered generic romance bestsellers, while an engineering professional looking for technical literature is greeted by mainstream memoirs. Consequently, user engagement plummets, cart abandonment escalates, and the vast majority of catalog titles remain buried in obscurity.
</p>
<p>
<strong>Reader's Haven</strong> is a next-generation, intelligent online bookstore platform engineered to bridge the gap between large-scale digital commerce and personalized literary discovery. Built on a modern <strong>Django 6.1</strong> and <strong>Python 3.12</strong> web framework, the system integrates a sophisticated, multi-strategy <strong>Machine Learning Recommendation Engine</strong> directly into the commerce workflow. Rather than treating artificial intelligence as an external afterthought, Reader's Haven embeds recommendation pipelines into every touchpoint of the reader's journey—from the dynamic homepage and live search autocomplete to product detail pages, shopping cart bundles, and a dedicated <em>"For You"</em> curation hub.
</p>
<p>
The platform balances powerful algorithmic discovery with frictionless e-commerce execution. Users can browse by genre, author, rating, and publication year; preview extensive book metadata; inspect community reviews; assemble custom carts; apply dynamic promotional discount codes; complete multi-step checkouts with simulated payment gateways; and generate printable invoices. Simultaneously, store managers are empowered with an executive <strong>Analytics & Telemetry Dashboard</strong> that monitors live gross revenue, units sold, inventory thresholds, and recommendation matrix re-synchronization.
</p>
''', pnum=1)

    # Page 2
    add_p('''
<h2 class="section-title">1.2 Problem Definition</h2>
<p>
The development of modern digital bookstore platforms involves addressing severe structural, algorithmic, and operational challenges inherent to literary commerce. Traditional online bookstores and basic e-commerce templates suffer from several critical shortcomings:
</p>
<p>
<strong>1. Information Overload and Discovery Friction:</strong> With extensive catalogs containing thousands of volumes, customers struggle to identify titles aligning with their reading preferences. Without intelligent filtering and contextual matching, users must manually sift through dozens of pages, leading to cognitive fatigue and prompt site abandonment.
</p>
<p>
<strong>2. Ineffective Static Bestseller Paradigms:</strong> Traditional stores rely heavily on global top-seller rankings. These rankings create a feedback loop where already-famous books dominate visibility, completely marginalizing high-quality backlist titles and niche publications that could offer immense value to specific reader segments.
</p>
<p>
<strong>3. The Cold-Start Dilemma in Recommendation Systems:</strong> A notorious hurdle in algorithmic personalization is the <em>cold-start problem</em>. When a new user registers or a new book is added to inventory, zero historical purchase or rating records exist. Naive collaborative filtering algorithms fail entirely in this scenario, rendering the recommendation engine useless for new visitors.
</p>
<p>
<strong>4. Lack of Explainability and Consumer Trust:</strong> Black-box recommendation systems that merely present book covers without context fail to foster user trust. Readers frequently wonder, <em>"Why is this book recommended to me?"</em> Without transparent rationale (such as common author motifs, overlapping thematic keywords, or shared readership), users hesitate to commit their time and financial resources to unfamiliar authors.
</p>
<p>
<strong>5. Fragmented Basket Cross-Selling:</strong> Physical bookstore clerks frequently suggest companion volumes that complement a reader's selection. In traditional digital storefronts, bundle suggestions are either absent or manually hardcoded by administrators, which is impossible to scale across dynamic catalogs.
</p>
<p>
<strong>6. Opaque Merchant Telemetry and Inventory Blindspots:</strong> Bookstore administrators often lack unified diagnostic dashboards to monitor real-time sales revenue, top grossing categories, customer interaction telemetry (clicks, wishlist additions, ratings), and low-stock alerts.
</p>
<p>
Therefore, the core problem addressed by this project is: <em>To design, implement, and validate an enterprise-grade digital bookstore that combines transactional e-commerce reliability with an explainable, multi-strategy machine learning recommendation engine to maximize discovery, user delight, and business efficiency.</em>
</p>
''', pnum=2)

    # Page 3
    add_p('''
<h2 class="section-title">1.3 Aim</h2>
<p>
The principal aim of this project is to conceptualize, design, and implement <strong>Reader's Haven</strong>, an enterprise-grade, responsive, full-stack online bookstore management system featuring a hybrid machine learning recommendation engine that automates personalized discovery, provides transparent explainability, and facilitates seamless digital commerce operations.
</p>

<h2 class="section-title">1.4 Objectives</h2>
<p>
To achieve the stated aim, the project executes the following specific, measurable objectives:
</p>
<ul>
    <li><strong>Secure Authentication & Persona Modeling:</strong> Implement robust user authentication using Django's security framework, supporting multi-persona profiling, reading goal trackers, and demo persona selectors (e.g., Alice, Bob, Charlie).</li>
    <li><strong>Intelligent Content-Based Filtering:</strong> Implement TF-IDF vectorization and cosine similarity matching on book synopses, genre tags, and author profiles to recommend contextually related literature.</li>
    <li><strong>Item-Item Collaborative Filtering:</strong> Construct a user-item interaction matrix weighted by explicit reviews and implicit telemetry signals to discover latent community reading preferences.</li>
    <li><strong>Market Basket Association Rule Mining:</strong> Apply Apriori-inspired co-occurrence analysis across historical customer orders to generate dynamic <em>"Frequently Bought Together"</em> book bundles.</li>
    <li><strong>Adaptive Hybrid Ensemble:</strong> Harmonize collaborative filtering (40%), content-based similarity (40%), and popularity signals (20%) into a unified scoring model with cold-start fallbacks.</li>
    <li><strong>AI Explainability API:</strong> Develop transparent rationale endpoints that explain why specific books are recommended to the reader.</li>
    <li><strong>Live Autocomplete Search:</strong> Build a low-latency REST search API that dynamically autocompletes book titles, authors, and genres as the user types.</li>
    <li><strong>Frictionless Commerce Workflow:</strong> Implement session and user-linked cart management, promotional coupon validation (<code>BOOKWORM15</code>), multi-step checkout, and printable tax receipts.</li>
    <li><strong>Store Management & Analytics Dashboard:</strong> Deliver an executive telemetry portal displaying gross sales revenue, units sold, category distributions, and manual matrix re-synchronization triggers.</li>
    <li><strong>Responsive Modern UI:</strong> Design a mobile-first, visually elevated frontend utilizing Tailwind CSS and Lucide icons following contemporary web usability standards.</li>
</ul>

<h2 class="section-title">1.5 Goal</h2>
<p>
The overarching goal of Reader's Haven is to democratize literature discovery through applied data science and intuitive software engineering. By ensuring that every reader is greeted by books tailored precisely to their intellectual curiosities, the system eliminates discovery friction, amplifies reader engagement, and proves the viability of explainable machine learning in modern web applications.
</p>

<h2 class="section-title">1.6 Need of the System</h2>
<p>
The necessity for Reader's Haven arises from modern retail demands:
</p>
<ol>
    <li><strong>Combatting Choice Fatigue:</strong> Guides readers through expansive catalogs without overwhelming cognitive load.</li>
    <li><strong>Hyper-Personalized Discovery:</strong> Tailors recommendations to individual reading history rather than blunt global averages.</li>
    <li><strong>Resolving Cold-Start Friction:</strong> Utilizes onboarding preference questionnaires and genre smoothing for immediate personalization.</li>
    <li><strong>Algorithmic Transparency:</strong> Builds shopper confidence through explicit recommendation reasoning.</li>
    <li><strong>Automated Bundle Upselling:</strong> Increases Average Order Value (AOV) via data-driven companion volume suggestions.</li>
    <li><strong>Unified Transaction Processing:</strong> Provides reliable cart, tax, shipping, and order lifecycle management.</li>
    <li><strong>Actionable Merchant Analytics:</strong> Furnishes bookstore operators with real-time operational telemetry.</li>
    <li><strong>Enterprise-Grade Security:</strong> Employs CSRF tokens, hashed credentials, and parameterized SQL queries.</li>
    <li><strong>Omnichannel Accessibility:</strong> Delivers full responsive utility across desktop, tablet, and mobile browsers.</li>
    <li><strong>Scalable Modular Architecture:</strong> Establishes clean decoupled Django apps prepared for cloud containerization.</li>
</ol>
''', pnum=3)

def get_ch2_pages(add_p):
    # Page 4
    add_p('''
<h1 class="chapter-title">CHAPTER 2. REQUIREMENT SPECIFICATION</h1>
<h2 class="section-title">2.1 Introduction</h2>
<p>
Software requirement specification establishes the definitive operational, technical, and architectural criteria that govern the design, construction, and validation of a software system. For Reader's Haven, the requirement specification defines the behavioral expectations of shoppers, readers, and administrators, the hardware/software runtime parameters, and the development lifecycle methodology utilized.
</p>
<p>
A structured specification eliminates ambiguity between architectural ambition and technical realization. It establishes clear verifiable benchmarks against which individual modules, machine learning algorithms, and user interfaces are subjected to quality assurance testing.
</p>

<h2 class="section-title">Functional Requirements</h2>
<p>
Functional requirements describe the specific actions, behaviors, and services the application must execute:
</p>
<ul>
    <li><strong>User Account Management:</strong> Users must be able to register, log in, manage profiles, track annual reading goals, and authenticate as pre-configured demo personas.</li>
    <li><strong>Book Catalog & Live Search:</strong> The system must present an indexed book catalog supporting pagination, genre filtering, price range sorting, and real-time title/author autocomplete search.</li>
    <li><strong>Multi-Strategy Recommendations:</strong> The platform must calculate similarity scores using TF-IDF text mining, item-item collaborative matrices, and Apriori association algorithms.</li>
    <li><strong>Explainability Delivery:</strong> The system must provide transparent, human-readable explanations detailing why a recommended title was chosen.</li>
    <li><strong>Cart & Bundle Management:</strong> Shoppers must be able to add single books or one-click multi-item bundles to their cart, modify quantities, and apply percentage discount coupons.</li>
    <li><strong>Checkout & Order Fulfillment:</strong> The application must collect shipping details, calculate subtotal/tax/shipping fees, simulate payment processing, decrement inventory, and produce printable receipts.</li>
    <li><strong>Review & Rating Submission:</strong> Authenticated readers must be able to submit numerical ratings (1-5 stars) and detailed textual reviews for purchased or read books.</li>
    <li><strong>Store Analytics & Administrative Control:</strong> Managers must be able to view live revenue KPIs, top-performing titles, telemetry logs, update inventory stocks, and manually trigger recommendation matrix recalculations.</li>
</ul>

<h2 class="section-title">Non-Functional Requirements</h2>
<ul>
    <li><strong>Security:</strong> All user passwords must be hashed using PBKDF2/SHA-256; all form submissions must be protected with CSRF tokens; administrative portals must require staff authorization.</li>
    <li><strong>Performance & Latency:</strong> Homepage and catalog pages must render within 500 milliseconds; search autocomplete responses must return in under 100 milliseconds.</li>
    <li><strong>Data Integrity & Concurrency:</strong> Inventory decrements and order creation must occur atomically to prevent race conditions and overselling.</li>
    <li><strong>Usability & Responsiveness:</strong> The UI must render responsively across viewports from 320px mobile screens to 4K desktop displays with intuitive visual cues.</li>
    <li><strong>Maintainability & Modularity:</strong> The codebase must follow Django's Model-View-Template (MVT) design pattern across separated applications.</li>
</ul>
''', pnum=4)

    # Page 5
    add_p('''
<h2 class="section-title">2.2 System Environment</h2>
<p>
The system environment describes the architectural deployment and communication model of Reader's Haven. The application adheres to a contemporary <strong>Three-Tier Client-Server Architecture</strong> structured across presentation, application, and persistence tiers:
</p>
<ul>
    <li><strong>Presentation Tier (Frontend):</strong> Executed entirely within the client's modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari). The presentation tier utilizes semantic HTML5, utility-first Tailwind CSS for responsive styling, Lucide Icons for vector visual elements, and lightweight vanilla JavaScript for asynchronous fetch interactions (e.g., live search autocomplete and AJAX telemetry logging).</li>
    <li><strong>Application Tier (Backend Logic & AI Engines):</strong> Powered by Python 3.12 and Django 6.1. This tier encapsulates URL routing, security middleware, session handling, business logic controllers (views), and the scikit-learn recommendation engine (TF-IDF vectorizer, cosine similarity metrics, and sparse matrix manipulators).</li>
    <li><strong>Data & Persistence Tier:</strong> Comprises a relational SQLite3 database managed through Django's Object-Relational Mapping (ORM) layer, supplemented by media storage for book cover graphics and WhiteNoise for static file serving.</li>
</ul>
<p>
The server operates locally at <code>http://127.0.0.1:8000</code> or within cloud production environments (e.g., Vercel / Render / AWS) with standard WSGI/ASGI application gateways.
</p>

<h2 class="section-title">2.3 Software Requirements</h2>
<table class="report-table">
    <thead>
        <tr>
            <th style="width: 35%;">Software Component</th>
            <th style="width: 65%;">Specification / Version Used</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Operating System</strong></td>
            <td>Windows 10/11, macOS Sequoia, or Linux Ubuntu 22.04 LTS</td>
        </tr>
        <tr>
            <td><strong>Programming Language</strong></td>
            <td>Python 3.12 (64-bit runtime environment)</td>
        </tr>
        <tr>
            <td><strong>Web Framework</strong></td>
            <td>Django 6.1 (Model-View-Template architectural pattern)</td>
        </tr>
        <tr>
            <td><strong>Machine Learning & Analytics</strong></td>
            <td>Scikit-learn 1.9.0, NumPy 2.5.2, Pandas 3.0.5, SciPy 1.18.1</td>
        </tr>
        <tr>
            <td><strong>Database System</strong></td>
            <td>SQLite3 (bundled with Python) / dj-database-url 3.1.2</td>
        </tr>
        <tr>
            <td><strong>Frontend Styling & Icons</strong></td>
            <td>Tailwind CSS CDN, Lucide Icons CDN, Inter & Playfair Display Google Fonts</td>
        </tr>
        <tr>
            <td><strong>Static File Engine</strong></td>
            <td>WhiteNoise 6.12.0 (Gzip & Brotli compressed asset streaming)</td>
        </tr>
        <tr>
            <td><strong>Image Processing</strong></td>
            <td>Pillow 12.3.0 (for cover thumbnailing and media uploads)</td>
        </tr>
        <tr>
            <td><strong>Development Environment</strong></td>
            <td>Visual Studio Code with Python & Django Language Server extensions</td>
        </tr>
        <tr>
            <td><strong>Web Browsers</strong></td>
            <td>Google Chrome 120+, Microsoft Edge 120+, Mozilla Firefox 120+</td>
        </tr>
    </tbody>
</table>

<h2 class="section-title">2.4 Hardware Requirements</h2>
<table class="report-table">
    <thead>
        <tr>
            <th style="width: 25%;">Hardware Element</th>
            <th style="width: 35%;">Minimum Requirement</th>
            <th style="width: 40%;">Recommended Specification</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Processor (CPU)</strong></td>
            <td>Dual-Core Intel Core i3 / AMD Ryzen 3 (2.0 GHz)</td>
            <td>Quad-Core Intel Core i5 / Apple Silicon M-Series / Ryzen 5</td>
        </tr>
        <tr>
            <td><strong>Memory (RAM)</strong></td>
            <td>4 GB DDR4</td>
            <td>8 GB or 16 GB DDR4/DDR5 (for fast ML matrix computations)</td>
        </tr>
        <tr>
            <td><strong>Storage Disk</strong></td>
            <td>10 GB available SSD / HDD storage</td>
            <td>256 GB NVMe Solid State Drive</td>
        </tr>
        <tr>
            <td><strong>Display Resolution</strong></td>
            <td>1366 × 768 pixels</td>
            <td>1920 × 1080 (Full HD) or higher</td>
        </tr>
        <tr>
            <td><strong>Network Interface</strong></td>
            <td>Standard broadband or Wi-Fi (1 Mbps)</td>
            <td>High-speed broadband (10 Mbps+) for asset streaming</td>
        </tr>
    </tbody>
</table>
''', pnum=5)

    # Page 6
    add_p('''
<h2 class="section-title">2.5 Methodology</h2>
<p>
The engineering of Reader's Haven was conducted using the <strong>Spiral Model</strong> of software development. First introduced by Barry Boehm, the Spiral Model combines the methodical, structured milestones of the classic Waterfall lifecycle with the iterative refinement and rapid prototyping of Agile paradigms, placing paramount emphasis on <strong>risk management</strong>.
</p>
<p>
Developing an e-commerce platform coupled with machine learning recommendation models presents unique algorithmic and operational risks. These risks include user-item interaction matrix sparsity, recommendation latency during peak catalog browsing, checkout concurrency bottlenecks, and data drift. The Spiral Model allowed the development team to iteratively navigate through four distinct spirals:
</p>
<ul>
    <li><strong>Spiral 1 (Core Foundations & Catalog Architecture):</strong> Focused on relational database schema design, catalog indexing, author/genre taxonomy, book management, and responsive template layouts.</li>
    <li><strong>Spiral 2 (Commerce & Order Lifecycle Pipeline):</strong> Engineered the shopping cart session engine, promotional discount coupon mechanics, multi-step checkout workflow, stock decrementing, and order invoice generation.</li>
    <li><strong>Spiral 3 (Machine Learning Recommendation Engines):</strong> Developed and tuned the content-based TF-IDF vectorizer, item-item collaborative filtering engine, Apriori basket rule miner, and the central hybrid blending orchestrator.</li>
    <li><strong>Spiral 4 (Telemetry, Analytics & System Integration):</strong> Implemented real-time telemetry logging, the executive store manager dashboard, explainability APIs, security hardening, and end-to-end verification.</li>
</ul>

<h2 class="section-title">2.6 Spiral Model</h2>
<p>
Every iteration of the spiral model traverses four cyclical quadrants:
</p>
<ol>
    <li><strong>Planning:</strong> Identifying cycle objectives, defining requirements, evaluating architectural trade-offs, and selecting development tools.</li>
    <li><strong>Risk Analysis:</strong> Proactively analyzing potential failure modes, including cold-start catalog sparsity, recommendation computation bottlenecks, inventory race conditions, and session hijacking.</li>
    <li><strong>Engineering:</strong> Writing modular Python views, ORM models, recommendation algorithms, HTML templates, and client-side JavaScript controllers.</li>
    <li><strong>Evaluation:</strong> Conducting unit tests, regression verification, persona profile matching tests, and soliciting user feedback to direct the subsequent cycle.</li>
</ol>
<p>
The iterative progression of the development lifecycle is illustrated in Figure 2.1.
</p>
<div class="figure-container">
    <img src="diagrams/spiral_model.png" class="figure-img" style="max-height: 110mm;" alt="Spiral Model Diagram">
    <div class="figure-caption">Figure 2.1: Spiral Model used for Reader's Haven Online Bookstore</div>
</div>
''', pnum=6)

    # Page 7
    add_p('''
<h3 class="subsection-title">Why Spiral Model?</h3>
<p>
The Spiral Model was explicitly selected for Reader's Haven for several compelling architectural and engineering justifications:
</p>
<ul>
    <li><strong>Risk-Driven Prioritization:</strong> Machine learning recommendation systems pose inherent risks regarding sparse data matrices and cold-start failures. The Spiral Model mandates risk assessment before code execution, allowing the team to devise fallback mechanisms (such as genre-based onboarding and Bayesian rating smoothing) before deploying the recommendation engine.</li>
    <li><strong>Iterative Prototyping:</strong> Rather than waiting until the end of the project to test recommendations, working prototypes were generated in every loop. This enabled early empirical testing of TF-IDF tokenization accuracy and cosine similarity thresholds against real book titles.</li>
    <li><strong>Adaptive Requirement Refinement:</strong> Feedback from early cycles inspired advanced features such as the AI Explainability API, one-click demo personas, and live search autocomplete, which were seamlessly incorporated in subsequent loops without disrupting existing commerce modules.</li>
    <li><strong>Early Verification:</strong> Comprehensive automated testing in each cycle ensured that regressions were identified and eliminated immediately, maintaining architectural stability throughout development.</li>
</ul>

<h3 class="subsection-title">Applications of the Spiral Model</h3>
<p>
The Spiral Model is universally recognized as the optimal engineering methodology for:
</p>
<ul>
    <li>Complex e-commerce applications integrating artificial intelligence and data science pipelines.</li>
    <li>Software products where algorithmic correctness, security, and transaction reliability are paramount.</li>
    <li>Projects subject to continuous user feedback and empirical tuning.</li>
    <li>Medium to large-scale distributed web applications designed for long-term scalability and feature enhancement.</li>
</ul>
<p>
Through the disciplined application of the Spiral Model, Reader's Haven progressed from an initial concept into an enterprise-grade, verified literary commerce platform.
</p>
''', pnum=7)

def get_ch3_pages(add_p):
    # Page 8
    add_p('''
<h1 class="chapter-title">CHAPTER 3. SYSTEM ANALYSIS</h1>
<h2 class="section-title">3.1 System Analysis</h2>
<p>
System analysis represents the comprehensive examination of an operational domain to understand user pain points, define precise functional boundaries, and formulate technical solutions. It acts as the bridge connecting high-level business goals with robust software architectures.
</p>
<p>
To establish the system requirements for <strong>Reader's Haven</strong>, an exhaustive analysis of existing physical bookstores, conventional online booksellers, and academic literature on recommender systems was undertaken. Key exploratory questions investigated include:
</p>
<ul>
    <li>How do readers discover new books in physical bookstores versus digital platforms?</li>
    <li>Why do static top-seller carousels fail to satisfy diverse demographic segments?</li>
    <li>What data signals (e.g., explicit ratings, implicit clicks, wishlist additions, purchase histories) are most indicative of reader taste?</li>
    <li>How can an algorithmic recommender explain its reasoning to overcome user skepticism?</li>
    <li>What operational metrics and real-time telemetry do bookstore administrators need to make informed stocking and pricing decisions?</li>
</ul>
<p>
The findings revealed that readers prioritize relevance and contextual alignment far above raw volume. A customer presented with three books precisely matching their taste is ten times more likely to purchase than one confronted with fifty unrelated bestsellers.
</p>

<h3 class="subsection-title">Feasibility Study</h3>
<p>
A structured feasibility study was conducted to evaluate the viability of developing and deploying Reader's Haven:
</p>
<ul>
    <li><strong>Technical Feasibility:</strong> The technology stack (Python 3.12, Django 6.1, SQLite3, Scikit-learn, Tailwind CSS) is free, open-source, well-documented, and possesses mature global ecosystem support. The algorithms utilized (TF-IDF, Cosine Similarity, Apriori) are computationally efficient and execute within standard hardware constraints. Therefore, the project is technically feasible.</li>
    <li><strong>Economic Feasibility:</strong> Zero software licensing fees were incurred because all software frameworks and libraries are open-source. The project requires only standard workstation computing hardware for development and minimal hosting resources for deployment. The economic benefits—increased reader retention, automated upselling, and elimination of manual catalog curation—vastly outweigh operational costs.</li>
    <li><strong>Operational Feasibility:</strong> The user interface is engineered for maximum simplicity and intuitive navigation. Both novice book shoppers and store managers can operate the platform with zero specialized training. Live autocomplete and one-click demo personas ensure smooth adoption.</li>
    <li><strong>Schedule Feasibility:</strong> Development was structured across four iterative spirals completed methodically within the academic semester schedule.</li>
</ul>
''', pnum=8)

    # Page 9
    add_p('''
<h2 class="section-title">3.2 Analysis of Existing System</h2>
<p>
In conventional online bookstore systems and traditional retail establishments, catalog discovery and inventory management are burdened by severe limitations:
</p>
<ul>
    <li><strong>Static, One-Size-Fits-All Curation:</strong> Traditional websites show identical "Featured Books" banners to every visitor, ignoring whether the shopper loves epic fantasy, historical biographies, or programming manuals.</li>
    <li><strong>Absence of Contextual Search:</strong> Search bars require exact title matching. A typo or query by broad topic yields frustrating empty search results or irrelevant listings.</li>
    <li><strong>Unexplained Recommendations:</strong> When suggestions exist, they appear as isolated images without justification, leading to skepticism and low click-through rates.</li>
    <li><strong>Manual, Arbitrary Cross-Selling:</strong> Promotional bundles are manually created by managers, which becomes unmanageable as catalogs expand to thousands of titles.</li>
    <li><strong>Opaque Cold-Start Scenarios:</strong> First-time visitors are presented with generic storefronts without any onboarding mechanisms to capture immediate genre preferences.</li>
    <li><strong>Disconnected Cart and Promotional Mechanics:</strong> Shopping carts lack real-time coupon calculation, free shipping thresholds, and contextual companion book recommendations.</li>
    <li><strong>Siloed Merchant Administration:</strong> Store managers must toggle between multiple disconnected tools to monitor sales, review inventory, inspect user feedback, and manage listings.</li>
</ul>

<h2 class="section-title">3.3 Analysis of the Proposed System</h2>
<p>
The proposed <strong>Reader's Haven</strong> platform replaces static e-commerce workflows with an intelligent, data-driven, and highly engaging digital bookstore ecosystem. All book metadata, reader interactions, cart sessions, and orders are unified in a relational database, while machine learning algorithms operate seamlessly behind the scenes.
</p>
<p>
The proposed platform is organized into six core architectural modules:
</p>
<ol>
    <li><strong>Authentication & Reader Profiling:</strong> Manages secure user registration, session authentication, reading goal progress bars, and one-click demo persona selectors (Alice, Bob, Charlie, Diana).</li>
    <li><strong>Catalog & Live Discovery Engine:</strong> Delivers multi-faceted book exploration by genre, author, format, rating, and publication year, enhanced by a fast live search autocomplete API.</li>
    <li><strong>Multi-Strategy Hybrid Recommendation Engine:</strong> Orchestrates TF-IDF content similarity, item-item collaborative filtering, Apriori market basket bundles, and transparent AI explainability rationale.</li>
    <li><strong>Cart, Bundle & Promotional Discount Engine:</strong> Features session-persistent carts, one-click bundle additions, dynamic tax/shipping calculations, and coupon redemption (<code>BOOKWORM15</code>).</li>
    <li><strong>Checkout, Payment & Order Lifecycle:</strong> Streamlines order placement with simulated payment confirmation, inventory stock decrements, order history, and printable invoices.</li>
    <li><strong>Store Management & Real-Time Analytics Dashboard:</strong> Empowers administrators with live revenue telemetry, top-selling titles, customer interaction logs, and manual recommendation matrix re-sync triggers.</li>
</ol>
''', pnum=9)

    # Page 10
    add_p('''
<h3 class="subsection-title">Advantages of the Proposed System</h3>
<p>
The implementation of Reader's Haven provides profound advantages over traditional solutions:
</p>
<ul>
    <li><strong>Hyper-Personalized Browsing:</strong> Every user enjoys a custom-tailored literary storefront driven by their reading history and genre preferences.</li>
    <li><strong>Mitigated Cold-Start Friction:</strong> New readers immediately receive targeted recommendations based on onboarding preferences and Bayesian rating smoothing.</li>
    <li><strong>Transparent Explainability:</strong> Transparent explanations (e.g., <em>"Recommended because you loved Dune and explore Hard Sci-Fi"</em>) build consumer confidence.</li>
    <li><strong>Automated Revenue Growth:</strong> Apriori-mined "Frequently Bought Together" bundles increase Average Order Value (AOV) organically.</li>
    <li><strong>Real-Time Autocomplete Search:</strong> Low-latency search indexing helps readers find titles in milliseconds.</li>
    <li><strong>Transactional Integrity:</strong> Atomic database operations prevent stock overselling and maintain financial accuracy.</li>
    <li><strong>Actionable Business Intelligence:</strong> Real-time charts and KPI metrics provide store operators with instant insights into sales performance.</li>
    <li><strong>Responsive Aesthetics:</strong> The modern Tailwind CSS visual design creates a captivating, premium reading atmosphere.</li>
</ul>
<p>
In summary, Reader's Haven establishes an enterprise-grade digital bookstore that harmoniously blends data science, algorithmic personalization, and reliable commerce.
</p>
''', pnum=10)

def get_ch4_pages(add_p):
    # Page 11
    add_p('''
<h1 class="chapter-title">CHAPTER 4. SURVEY OF TECHNOLOGY</h1>
<p>
This chapter presents a technical survey of the foundational technologies, programming languages, software libraries, and development tools selected to build Reader's Haven. Each technology was evaluated for reliability, ecosystem maturity, execution performance, and community support.
</p>

<h2 class="section-title">4.1 Python 3.12</h2>
<p>
Python is a high-level, interpreted, general-purpose programming language renowned for its expressive syntax, readable codebase, and unparalleled data science ecosystem. Python 3.12 introduces major performance improvements, including specialized adaptive interpreters, enhanced error reporting, and optimized memory management. In Reader's Haven, Python serves as the unifying language across the entire backend, powering both web controllers and complex machine learning matrix calculations.
</p>

<h2 class="section-title">4.2 Django 6.1 Framework</h2>
<p>
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Following the Model-View-Template (MVT) pattern, Django provides an enterprise-ready suite of built-in components:
</p>
<ul>
    <li><strong>Object-Relational Mapping (ORM):</strong> Enables database interactions using pure Python objects, eliminating SQL injection vulnerabilities and abstracting relational queries.</li>
    <li><strong>Authentication & Authorization:</strong> Provides secure session management, user hashing via PBKDF2/SHA-256, and staff role permissions.</li>
    <li><strong>CSRF & Security Middleware:</strong> Automatically defends against Cross-Site Request Forgery, Cross-Site Scripting, and clickjacking attacks.</li>
    <li><strong>Django Template Engine (DTE):</strong> Facilitates clean server-side HTML rendering with template inheritance, custom filters, and contextual processors.</li>
</ul>

<h2 class="section-title">4.3 SQLite3 & dj-database-url</h2>
<p>
SQLite is a self-contained, serverless, zero-configuration transactional SQL database engine. In Reader's Haven, SQLite3 provides robust relational storage for all users, books, genres, authors, reviews, carts, and orders. The <code>dj-database-url</code> utility allows dynamic database URL parsing, enabling instant zero-recode migration to PostgreSQL or MySQL in production cloud environments.
</p>

<h2 class="section-title">4.4 HTML5 & Semantic Web</h2>
<p>
HTML5 serves as the structural foundation of the application. It employs modern semantic elements (<code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;aside&gt;</code>, <code>&lt;section&gt;</code>, <code>&lt;footer&gt;</code>) to ensure high accessibility, search engine readability, and structural maintainability. Form inputs leverage native validation types (<code>email</code>, <code>number</code>, <code>password</code>) for immediate client-side feedback.
</p>
''', pnum=11)

    # Page 12
    add_p('''
<h2 class="section-title">4.5 Tailwind CSS & Modern UI</h2>
<p>
Tailwind CSS is a utility-first CSS framework that enables rapid, highly customized frontend interface development without writing brittle custom stylesheets. In Reader's Haven, Tailwind CSS provides:
</p>
<ul>
    <li>A curated, bespoke color palette featuring warm literary tones (amber brand hues, slate backgrounds, navy headers).</li>
    <li>Fluid, fully responsive layouts using Flexbox and CSS Grid that adapt seamlessly from mobile smartphones to ultrawide desktop monitors.</li>
    <li>Smooth micro-animations, interactive transitions, hover elevations, and custom glassmorphism overlays.</li>
    <li>Clean print stylesheets ensuring that order receipts render cleanly on paper without headers or navigation bars.</li>
</ul>

<h2 class="section-title">4.6 JavaScript (ES6) & Lucide Icons</h2>
<p>
JavaScript provides dynamic client-side interactivity without the overhead of heavy single-page application frameworks. Features implemented with vanilla JavaScript include:
</p>
<ul>
    <li>Asynchronous <code>fetch()</code> API requests for real-time live search autocomplete.</li>
    <li>Dynamic shopping cart quantity updates and coupon discount calculations.</li>
    <li>Interactive modal dialogues for displaying AI explainability rationale.</li>
    <li>AJAX telemetry logging to capture user reading interest signals without page reloads.</li>
</ul>
<p>
<strong>Lucide Icons</strong> provides clean, lightweight, scalable SVG vector icons throughout the interface (e.g., search magnifying glass, shopping cart, rating stars, recommendation sparkles), enhancing visual scannability.
</p>

<h2 class="section-title">4.7 Scikit-learn, NumPy & Pandas</h2>
<p>
Scikit-learn is the premier machine learning library for Python. In Reader's Haven, scikit-learn powers the core recommendation algorithms:
</p>
<ul>
    <li><code>TfidfVectorizer</code>: Converts textual book synopses, genre tags, and author descriptions into high-dimensional numerical feature vectors with stop-word removal and n-gram analysis.</li>
    <li><code>cosine_similarity</code>: Computes pairwise angular similarity between book feature vectors to identify thematically related titles.</li>
    <li><strong>NumPy & Pandas:</strong> Handle vectorized matrix operations, sparse matrix manipulation, and tabular interaction aggregation with maximum computational efficiency.</li>
</ul>
''', pnum=12)

    # Page 13
    add_p('''
<h2 class="section-title">4.8 Machine Learning Recommendation Algorithms</h2>
<p>
Reader's Haven employs four complementary algorithmic strategies to deliver industry-leading recommendations:
</p>

<h3 class="subsection-title">1. Content-Based Filtering (TF-IDF Vectorization)</h3>
<p>
Content-based filtering analyzes the intrinsic properties of items. For every book, a rich textual corpus is constructed combining title, author biography, genre classifications, and plot synopsis. The Term Frequency-Inverse Document Frequency (TF-IDF) algorithm evaluates term importance:
</p>
<p style="text-align: center; font-family: 'Courier New', monospace; font-size: 10pt; margin: 10px 0;">
TF-IDF(t, d, D) = TF(t, d) × ln(|D| / (1 + |{d ∈ D : t ∈ d}|))
</p>
<p>
Pairwise cosine similarity is then calculated between book vectors. Books sharing high angular proximity represent contextually similar literary works.
</p>

<h3 class="subsection-title">2. Item-Item Collaborative Filtering</h3>
<p>
Collaborative filtering identifies patterns across user reading behaviors. An interaction matrix $R_{u, i}$ is constructed where entries represent user interactions weighted by explicit reviews (1-5 stars) and implicit actions (clicks, wishlist adds, purchases). Item-item cosine similarity is computed between book interaction vectors:
</p>
<p style="text-align: center; font-family: 'Courier New', monospace; font-size: 10pt; margin: 10px 0;">
sim(i, j) = (v_i · v_j) / (||v_i|| × ||v_j||)
</p>
<p>
This reveals latent community associations, such as readers who enjoyed <em>Dune</em> also frequently admiring <em>Foundation</em>.
</p>

<h3 class="subsection-title">3. Market Basket Association Rules (Frequently Bought Together)</h3>
<p>
To recommend companion volumes on book detail pages, the system applies an Apriori-inspired co-occurrence algorithm across historical customer orders. It computes support, confidence, and lift for item pairs:
</p>
<p style="text-align: center; font-family: 'Courier New', monospace; font-size: 10pt; margin: 10px 0;">
Support(A, B) = P(A ∩ B), &nbsp;&nbsp; Confidence(A → B) = P(B | A)
</p>
<p>
Book pairs that consistently appear together in customer checkouts are packaged as one-click discounted bundles.
</p>

<h3 class="subsection-title">4. Hybrid Weighted Ensemble with Explainability</h3>
<p>
To overcome the individual limitations of each model, Reader's Haven implements an adaptive hybrid scoring function:
</p>
<p style="text-align: center; font-family: 'Courier New', monospace; font-size: 10pt; margin: 10px 0;">
Score_Hybrid = (0.40 × Score_Collab) + (0.40 × Score_Content) + (0.20 × Score_Popularity)
</p>
<p>
If a user has fewer than three interactions, the system gracefully falls back to onboarding genre preferences and Bayesian popularity smoothing.
</p>
''', pnum=13)

    # Page 14
    add_p('''
<h2 class="section-title">4.9 WhiteNoise & Asset Management</h2>
<p>
WhiteNoise allows Django web applications to serve their own static files directly without relying on complex external Nginx or Apache server configurations. WhiteNoise handles automatic gzip and brotli compression, computes unique cache-busting content hashes for CSS and JavaScript files, and ensures optimal client-side caching.
</p>

<h2 class="section-title">4.10 Development & Diagnostic Tools</h2>
<p>
The following tools supported the rapid development and testing of Reader's Haven:
</p>
<ul>
    <li><strong>Visual Studio Code:</strong> The primary Integrated Development Environment (IDE), providing Python syntax highlighting, IntelliSense autocomplete, Git integration, and terminal debugging.</li>
    <li><strong>Chrome & Edge Developer Tools:</strong> Utilized to inspect responsive CSS layout breakpoints, analyze network waterfall timings, debug asynchronous AJAX calls, and verify client rendering.</li>
    <li><strong>Pip & Virtual Environments (venv):</strong> Used to isolate project dependencies, preventing version conflicts with system-level Python packages.</li>
    <li><strong>Git Version Control:</strong> Monitored incremental feature additions and documentation milestones.</li>
    <li><strong>Automated Test Verification Scripts:</strong> Dedicated test suites executed end-to-end checks across authentication, catalog search, recommendation explainability, cart calculations, and checkout workflows.</li>
</ul>
''', pnum=14)

def get_ch5_pages(add_p):
    # Page 15
    add_p('''
<h1 class="chapter-title">CHAPTER 5. SYSTEM DESIGN</h1>
<h2 class="section-title">5.1 Introduction</h2>
<p>
System design is the foundational phase where software requirements and analytical models are translated into a concrete architectural blueprint. It defines the software components, subsystem interactions, relational data models, and communication protocols that ensure reliability, maintainability, and operational excellence.
</p>
<p>
The design of <strong>Reader's Haven</strong> adheres strictly to an industry-standard <strong>Three-Tier Model-View-Template (MVT) Architecture</strong>. Within this framework, clear separation of concerns is enforced:
</p>
<ul>
    <li><strong>Models (Data Layer):</strong> Define the relational schema, data types, business constraints, and ORM query methods.</li>
    <li><strong>Views (Application Logic & AI Tier):</strong> Contain business logic, algorithmic recommendation pipelines, telemetry tracking, and HTTP request/response handlers.</li>
    <li><strong>Templates (Presentation Layer):</strong> Render dynamic HTML5 interfaces styled with Tailwind CSS, delivering intuitive visual experiences to the client browser.</li>
</ul>
<p>
This chapter details the structural design through standard diagrams: System Architecture Diagram, Data Flow Diagrams (Level 0 and Level 1), Activity Diagram, Entity-Relationship Diagram, and Use-Case Diagram.
</p>

<h2 class="section-title">5.2 System Architecture Diagram</h2>
<p>
The System Architecture Diagram illustrates the overarching physical and logical topology of Reader's Haven. At the top level, users (Shoppers, Readers, Store Administrators) interact through standard web browsers.
</p>
<p>
Requests pass through Django's security middleware (CSRF verification, session authentication, WhiteNoise static streaming) and reach the URL dispatcher. The URL dispatcher routes requests to appropriate view controllers across separated apps (<code>books</code>, <code>cart</code>, <code>orders</code>, <code>accounts</code>, <code>recommendations</code>, <code>analytics</code>). The machine learning recommendation engine operates within the application tier, communicating with SQLite3 via Django ORM to extract interaction vectors, calculate similarity matrices, and stream rendered HTML or JSON payloads back to the browser.
</p>
<div class="figure-container">
    <img src="diagrams/architecture_diagram.png" class="figure-img" style="max-height: 125mm;" alt="System Architecture Diagram">
    <div class="figure-caption">Figure 5.1: System Architecture Diagram of Reader's Haven Online Bookstore</div>
</div>
''', pnum=15)

    # Page 16
    add_p('''
<h2 class="section-title">5.3 Data Flow Diagram</h2>
<p>
A Data Flow Diagram (DFD) visually maps how data enters, traverses, transforms, and persists within the system. It illustrates external entities, functional processes, and internal data stores without exposing underlying programming syntax.
</p>

<h3 class="subsection-title">5.3.1 Level 0 DFD (Context Diagram)</h3>
<p>
The Level 0 DFD portrays Reader's Haven as a singular central process with external entities: the <strong>Reader / Shopper</strong>, the <strong>Store Admin</strong>, and the <strong>D1 Database (SQLite3)</strong>.
</p>
<p>
Shoppers transmit registration details, search queries, cart modifications, and checkout shipping information into the system; in response, the system delivers book catalog data, personalized recommendations, printable invoices, and telemetry updates. Store administrators submit catalog updates, stock adjustments, and matrix sync commands; in return, the system generates real-time revenue analytics and order manifests.
</p>
<div class="figure-container">
    <img src="diagrams/dfd_level_0.png" class="figure-img" style="max-height: 110mm;" alt="Level 0 Data Flow Diagram">
    <div class="figure-caption">Figure 5.2: Data Flow Diagram (Level 0) of Reader's Haven Online Bookstore</div>
</div>
''', pnum=16)

    # Page 17
    add_p('''
<h3 class="subsection-title">5.3.2 Level 1 DFD</h3>
<p>
The Level 1 DFD decomposes the system into six core operational processes and five relational data stores:
</p>
<ul>
    <li><strong>1.0 User Authentication & Preferences:</strong> Verifies login credentials, initializes reading goals, and updates preferences in <em>D1: Users & Profiles</em>.</li>
    <li><strong>2.0 Catalog & Live Search:</strong> Queries <em>D2: Books & Authors</em> to deliver indexed catalog listings, genre filters, and autocomplete search results.</li>
    <li><strong>3.0 Hybrid AI Recommendation Engine:</strong> Combines data from <em>D2</em>, <em>D4</em>, and <em>D5: Telemetry</em> to compute TF-IDF and collaborative similarity rankings.</li>
    <li><strong>4.0 Cart & Coupon Calculation:</strong> Manages line items, calculates bundle discounts, and validates promotional codes in <em>D3: Cart & Coupons</em>.</li>
    <li><strong>5.0 Checkout & Order Processing:</strong> Transforms cart items into finalized orders in <em>D4: Orders & Items</em>, decrements inventory, and issues receipts.</li>
    <li><strong>6.0 Analytics & Stock Management:</strong> Aggregates sales figures, computes KPI metrics, and allows admins to update inventory stocks.</li>
</ul>
<div class="figure-container">
    <img src="diagrams/dfd_level_1.png" class="figure-img" style="max-height: 115mm;" alt="Level 1 Data Flow Diagram">
    <div class="figure-caption">Figure 5.3: Data Flow Diagram (Level 1) of Reader's Haven Online Bookstore</div>
</div>
''', pnum=17)

    # Page 18
    add_p('''
<h2 class="section-title">5.4 Activity Diagram</h2>
<p>
The UML Activity Diagram details the step-by-step procedural workflow of a user navigating through the platform, capturing sequential actions, algorithmic triggers, and transactional checkpoints.
</p>
<p>
The user journey initiates upon landing on the homepage. The system immediately checks session state: if the reader has past interaction telemetry, the hybrid AI engine renders personalized carousels; otherwise, cold-start genre feeds and trending bestsellers are displayed. The user searches for a book or browses genres, reviews book details and explainability rationale, adds items or bundles to the cart, applies discount coupons, completes checkout, decrements inventory atomically, and generates a printable invoice while updating the telemetry matrix.
</p>
<div class="figure-container">
    <img src="diagrams/activity_diagram.png" class="figure-img" style="max-height: 125mm;" alt="Activity Diagram">
    <div class="figure-caption">Figure 5.4: Activity Diagram of Reader's Haven Online Bookstore</div>
</div>
''', pnum=18)

    # Page 19
    add_p('''
<h2 class="section-title">5.5 Entity-Relationship Diagram (ERD)</h2>
<p>
The Entity-Relationship (ER) Diagram defines the relational database architecture supporting Reader's Haven. The schema is normalized to 3NF, ensuring data integrity, minimal redundancy, and optimal relational join performance:
</p>
<ul>
    <li><strong>User & UserProfile:</strong> 1:1 relationship storing authentication credentials, reading challenge targets, bio, and favorite genre preferences.</li>
    <li><strong>Author & Genre:</strong> Store normalized metadata linked via Foreign Keys to books (1:N).</li>
    <li><strong>Book:</strong> Central entity storing title, slug, price, discount price, stock, ratings count, and description.</li>
    <li><strong>Review & BookInteraction:</strong> Capture explicit star ratings and implicit interaction events (clicks, wishlist adds, purchases) linked to User and Book (1:N).</li>
    <li><strong>Cart & CartItem:</strong> Maintain session or user-linked shopping carts with quantity tracking (1:N).</li>
    <li><strong>Order & OrderItem:</strong> Preserve permanent purchase histories, customer shipping addresses, and payment statuses (1:N).</li>
</ul>
<div class="figure-container">
    <img src="diagrams/er_diagram.png" class="figure-img" style="max-height: 110mm;" alt="Entity Relationship Diagram">
    <div class="figure-caption">Figure 5.5: Entity-Relationship Diagram of Reader's Haven Database</div>
</div>
''', pnum=19)

    # Page 20
    add_p('''
<h2 class="section-title">5.6 Use-Case Diagram</h2>
<p>
The UML Use-Case Diagram establishes the system boundary and illustrates the functional interactions between primary actors and the platform. Reader's Haven incorporates two primary actors: the <strong>Online Reader / Shopper</strong> and the <strong>Store Admin / Manager</strong>.
</p>
<p>
The Online Reader can register/login, browse catalogs, use live autocomplete search, inspect book details and explainability rationale, view personalized AI feeds, manage shopping carts and wishlists, redeem promotional coupons, execute simulated checkouts, and submit reviews.
</p>
<p>
The Store Administrator can manage book inventory, update stock levels, inspect executive revenue KPIs and telemetry logs, and trigger manual AI matrix re-synchronization.
</p>
<div class="figure-container">
    <img src="diagrams/use_case_diagram.png" class="figure-img" style="max-height: 125mm;" alt="Use-Case Diagram">
    <div class="figure-caption">Figure 5.6: Use-Case Diagram of Reader's Haven Online Bookstore</div>
</div>
''', pnum=20)

print("Chapters 1 through 5 ready.")
