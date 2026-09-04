"""
FuturePath AI - Career knowledge base.

Each career has:
- keywords: words/phrases the matcher looks for in what the student says
  (interests, subjects, activities, work-style words)
- holland: rough Holland Code tags (R-I-A-S-E-C) for future psychometric work
- resources: free/affordable ways to start learning, mixing global platforms
  with Sri Lanka-relevant options (VTA, NAITA, university MOOCs, YouTube)

This file is deliberately a plain Python data structure (not a database) so
it's easy to read, edit, and extend without any setup. Swap it for a real
DB once you have enough users to want persistence, editing via an admin UI,
or per-user analytics.
"""

CAREERS = [
    {
        "id": "software-dev",
        "title": "Software / Web Developer",
        "sector": "Technology",
        "keywords": [
            "coding", "code", "programming", "software", "app", "website",
            "computer", "logic", "puzzle", "build", "debug", "game dev",
            "problem solving", "maths", "math", "algorithm", "tech"
        ],
        "holland": ["I", "R"],
        "description": (
            "Designs and builds the applications, websites, and systems "
            "people use every day. High global demand, strong remote/"
            "freelance opportunities from Sri Lanka."
        ),
        "core_skills": ["Programming fundamentals (Python or JavaScript)", "Git/GitHub", "Problem solving", "HTML/CSS", "APIs & databases"],
        "resources": [
            {"name": "CS50x (Harvard, free)", "url": "https://cs50.harvard.edu/x/", "cost": "Free"},
            {"name": "The Odin Project (full-stack web)", "url": "https://www.theodinproject.com/", "cost": "Free"},
            {"name": "freeCodeCamp", "url": "https://www.freecodecamp.org/", "cost": "Free"},
            {"name": "NVQ / NAITA Software Engineering courses", "url": "https://www.naita.gov.lk/", "cost": "Low-cost, government-run"},
        ],
    },
    {
        "id": "data-ai",
        "title": "Data Science / AI & Machine Learning",
        "sector": "Technology",
        "keywords": [
            "data", "statistics", "numbers", "analysis", "ai", "artificial intelligence",
            "machine learning", "excel", "patterns", "research", "prediction",
            "maths", "math", "curious", "experiment"
        ],
        "holland": ["I", "C"],
        "description": (
            "Turns raw data into predictions and insights that drive decisions. "
            "One of the fastest-growing fields globally, with strong remote "
            "freelance demand."
        ),
        "core_skills": ["Python (pandas, numpy)", "Statistics basics", "SQL", "Data visualization", "Intro machine learning"],
        "resources": [
            {"name": "Kaggle Learn (free micro-courses)", "url": "https://www.kaggle.com/learn", "cost": "Free"},
            {"name": "Google Data Analytics Certificate (Coursera)", "url": "https://www.coursera.org/professional-certificates/google-data-analytics", "cost": "Free to audit"},
            {"name": "fast.ai Practical Deep Learning", "url": "https://course.fast.ai/", "cost": "Free"},
        ],
    },
    {
        "id": "uiux",
        "title": "UI/UX Designer",
        "sector": "Technology / Creative",
        "keywords": [
            "design", "drawing", "art", "creative", "visual", "colors",
            "user experience", "apps", "figma", "sketch", "layout", "aesthetics",
            "empathy", "people"
        ],
        "holland": ["A", "I"],
        "description": (
            "Designs digital products so they're easy and pleasant to use — "
            "blends creativity with problem-solving for real users."
        ),
        "core_skills": ["Figma", "Wireframing & prototyping", "User research basics", "Visual/typography fundamentals"],
        "resources": [
            {"name": "Google UX Design Certificate (Coursera)", "url": "https://www.coursera.org/professional-certificates/google-ux-design", "cost": "Free to audit"},
            {"name": "Figma's own free tutorials", "url": "https://www.figma.com/resources/learn-design/", "cost": "Free"},
        ],
    },
    {
        "id": "digital-marketing",
        "title": "Digital Marketing Specialist",
        "sector": "Business / Creative",
        "keywords": [
            "marketing", "social media", "content", "branding", "advertising",
            "writing", "communication", "business", "trends", "photography",
            "video", "influencer", "sales"
        ],
        "holland": ["E", "A"],
        "description": (
            "Plans and runs campaigns across social media, search, and content "
            "to grow a brand — a fast entry point into tech-adjacent, "
            "freelance-friendly work."
        ),
        "core_skills": ["Social media strategy", "SEO basics", "Content writing", "Analytics (Meta/Google)", "Basic design (Canva)"],
        "resources": [
            {"name": "Google Digital Garage (free certified courses)", "url": "https://learndigital.withgoogle.com/digitalgarage", "cost": "Free"},
            {"name": "HubSpot Academy", "url": "https://academy.hubspot.com/", "cost": "Free"},
        ],
    },
    {
        "id": "renewable-energy",
        "title": "Renewable Energy Technician / Engineer",
        "sector": "Engineering / Green Economy",
        "keywords": [
            "energy", "environment", "climate", "solar", "electrical",
            "engineering", "hands-on", "building", "machines", "sustainability",
            "physics", "outdoors"
        ],
        "holland": ["R", "I"],
        "description": (
            "Installs and maintains solar and other renewable systems — a "
            "growing sector in Sri Lanka as the country expands green energy."
        ),
        "core_skills": ["Basic electrical theory", "Solar PV system design", "Safety practices", "Technical drawing"],
        "resources": [
            {"name": "NAITA / VTA electrical & renewable energy courses", "url": "https://www.naita.gov.lk/", "cost": "Low-cost, government-run"},
            {"name": "Solar Energy International free intro courses", "url": "https://www.solarenergy.org/", "cost": "Free/low-cost"},
        ],
    },
    {
        "id": "healthcare",
        "title": "Healthcare / Nursing",
        "sector": "Health & Social Care",
        "keywords": [
            "helping people", "medicine", "care", "nursing", "biology",
            "hospital", "compassion", "science", "patients", "health"
        ],
        "holland": ["S", "I"],
        "description": (
            "Direct, people-centered work caring for patients — stable local "
            "demand and strong international mobility for qualified nurses."
        ),
        "core_skills": ["Biology & anatomy fundamentals", "Communication & empathy", "First aid / clinical basics"],
        "resources": [
            {"name": "Sri Lanka Ministry of Health nursing school info", "url": "https://www.health.gov.lk/", "cost": "Varies"},
            {"name": "Coursera 'Introduction to Healthcare' courses", "url": "https://www.coursera.org/", "cost": "Free to audit"},
        ],
    },
    {
        "id": "accounting-finance",
        "title": "Accounting / Finance",
        "sector": "Business",
        "keywords": [
            "numbers", "accounting", "finance", "budget", "maths", "math",
            "organized", "detail", "business", "banking", "money"
        ],
        "holland": ["C", "E"],
        "description": (
            "Manages money, budgets, and financial reporting for organizations — "
            "a stable, in-demand path with respected local qualifications."
        ),
        "core_skills": ["Bookkeeping fundamentals", "Excel", "Financial reporting basics"],
        "resources": [
            {"name": "CA Sri Lanka / AAT Sri Lanka entry qualifications", "url": "https://www.casrilanka.com/", "cost": "Paid, staged"},
            {"name": "Coursera 'Introduction to Finance'", "url": "https://www.coursera.org/", "cost": "Free to audit"},
        ],
    },
    {
        "id": "tourism-hospitality",
        "title": "Tourism & Hospitality Management",
        "sector": "Services",
        "keywords": [
            "travel", "people", "hospitality", "hotel", "culture", "languages",
            "outdoors", "customer service", "events", "friendly"
        ],
        "holland": ["S", "E"],
        "description": (
            "Manages guest experiences across hotels, tours, and events — a "
            "core pillar of the Sri Lankan economy with strong people-skills fit."
        ),
        "core_skills": ["Customer service", "English/foreign language skills", "Basic hotel/event operations"],
        "resources": [
            {"name": "Sri Lanka Institute of Tourism & Hotel Management (SLITHM)", "url": "https://slithm.lk/", "cost": "Paid"},
        ],
    },
    {
        "id": "agri-tech",
        "title": "Agri-Tech / Agricultural Sciences",
        "sector": "Agriculture / Technology",
        "keywords": [
            "farming", "agriculture", "plants", "nature", "outdoors", "biology",
            "environment", "food", "science", "hands-on"
        ],
        "holland": ["R", "I"],
        "description": (
            "Applies science and technology (sensors, data, better techniques) "
            "to make farming more productive and sustainable — an emerging "
            "field in Sri Lanka blending tradition with innovation."
        ),
        "core_skills": ["Agricultural science basics", "Data collection", "Sustainable farming techniques"],
        "resources": [
            {"name": "University of Peradeniya / open agri-science MOOCs", "url": "https://www.coursera.org/", "cost": "Free to audit"},
        ],
    },
    {
        "id": "teaching",
        "title": "Teaching / Education",
        "sector": "Education",
        "keywords": [
            "teaching", "explaining", "helping people", "patience", "kids",
            "communication", "mentoring", "subject", "school"
        ],
        "holland": ["S", "A"],
        "description": (
            "Shapes the next generation by teaching a subject you love — "
            "consistently needed, with routes into both public and private "
            "education."
        ),
        "core_skills": ["Subject mastery", "Lesson planning", "Communication & patience"],
        "resources": [
            {"name": "National Colleges of Education", "url": "https://moe.gov.lk/", "cost": "Varies"},
        ],
    },
    {
        "id": "graphic-design",
        "title": "Graphic Design / Illustration",
        "sector": "Creative",
        "keywords": [
            "art", "drawing", "illustration", "design", "creative", "colors",
            "visual", "photoshop", "branding", "animation"
        ],
        "holland": ["A"],
        "description": (
            "Creates visual content — branding, illustration, motion graphics — "
            "for clients locally and on global freelance platforms."
        ),
        "core_skills": ["Adobe Photoshop/Illustrator (or free alternatives like GIMP/Inkscape)", "Typography", "Branding basics"],
        "resources": [
            {"name": "Canva Design School (free)", "url": "https://www.canva.com/designschool/", "cost": "Free"},
            {"name": "YouTube: Adobe / GIMP tutorials", "url": "https://www.youtube.com/", "cost": "Free"},
        ],
    },
    {
        "id": "entrepreneurship",
        "title": "Entrepreneurship / Freelancing",
        "sector": "Business",
        "keywords": [
            "business", "own business", "startup", "independent", "freelance",
            "leadership", "risk", "ideas", "self-employed", "sell"
        ],
        "holland": ["E"],
        "description": (
            "Builds an independent income through a business or freelance "
            "career — pairs well with a technical or creative skill from "
            "another path on this list."
        ),
        "core_skills": ["Basic business planning", "Client communication", "A sellable skill (design, dev, marketing, etc.)"],
        "resources": [
            {"name": "Google Digital Garage - Grow your business online", "url": "https://learndigital.withgoogle.com/digitalgarage", "cost": "Free"},
        ],
    },
]

# Small helper so app.py doesn't repeat this lookup logic
def get_career(career_id: str):
    for c in CAREERS:
        if c["id"] == career_id:
            return c
    return None
