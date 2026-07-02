# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "customer-events"

# Event Types
EVENT_TYPES = [
    "login",
    "logout",
    "page_view",
    "search",
    "view_product",
    "add_to_cart",
    "remove_from_cart",
    "purchase"
]

STATE_TRANSITIONS = {

    "login": [
        "page_view",
        "page_view",
        "search",
        "view_product"
    ],

    "page_view": [
        "page_view",
        "view_product",
        "view_product",
        "search"
    ],

    "search": [
        "search",
        "view_product",
        "view_product",
        "page_view"
    ],

    "view_product": [
        "add_to_cart",
        "page_view",
        "search"
    ],

    "add_to_cart": [
        "purchase",
        "remove_from_cart",
        "view_product",
        "page_view",
        "search",
        "view_product"
    ],

    "remove_from_cart": [
        "page_view",
        "search",
        "logout"
    ],

    "purchase": [
        "logout"
    ]
}

# Countries
COUNTRIES = [
    "India",
    "United States",
    "United Kingdom",
    "Germany",
    "Canada",
    "Australia"
]

# Cities
CITIES = {
    "India": ["Hyderabad", "Bengaluru", "Mumbai", "Delhi"],
    "United States": ["New York", "Seattle", "San Francisco"],
    "United Kingdom": ["London", "Manchester"],
    "Germany": ["Berlin", "Munich"],
    "Canada": ["Toronto", "Vancouver"],
    "Australia": ["Sydney", "Melbourne"]
}

# Devices
DEVICES = [
    "Desktop",
    "Mobile",
    "Tablet"
]

# Browsers
BROWSERS = [
    "Chrome",
    "Safari",
    "Firefox",
    "Edge"
]

# Marketing Sources
REFERRAL_SOURCES = [
    "Google",
    "Direct",
    "Facebook",
    "Instagram",
    "LinkedIn",
    "Email"
]

# Product Catalog
PRODUCTS = [
    {
        "id": "P1001",
        "name": "MacBook Air M4",
        "category": "Laptops",
        "price": 99999
    },
    {
        "id": "P1002",
        "name": "iPhone 16",
        "category": "Smartphones",
        "price": 79999
    },
    {
        "id": "P1003",
        "name": "Sony WH-1000XM6",
        "category": "Headphones",
        "price": 29999
    },
    {
        "id": "P1004",
        "name": "Samsung Monitor",
        "category": "Monitors",
        "price": 24999
    },
    {
        "id": "P1005",
        "name": "Mechanical Keyboard",
        "category": "Accessories",
        "price": 6999
    }
]