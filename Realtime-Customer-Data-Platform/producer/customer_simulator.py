import random
from uuid import uuid4
from datetime import datetime

from faker import Faker

from config import (
    PRODUCTS,
    COUNTRIES,
    CITIES,
    DEVICES,
    BROWSERS,
    REFERRAL_SOURCES,
)

from schemas import CustomerEvent


class CustomerSimulator:
    """
    Simulates realistic customer journeys.

    Each user has one active session.
    Events follow a logical order instead of being completely random.
    """

    # State Machine
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

    def __init__(self, total_users: int = 1000):

        self.fake = Faker()

        self.total_users = total_users

        # Stores active sessions
        self.active_sessions = {}

    def _random_user(self):
        """
        Pick a random user.
        """
        return random.randint(1, self.total_users)

    def _new_session(self):
        """
        Generate a session id.
        """
        return str(uuid4())

    def _choose_product(self):
        """
        Select a random product.
        """
        return random.choice(PRODUCTS)

    def _create_login_event(self, user_id: int):

        session_id = self._new_session()

        country = random.choice(COUNTRIES)

        self.active_sessions[user_id] = {
            "session_id": session_id,
            "current_stage": "login",
            "current_product": None,

            "country": country,
            "city": random.choice(CITIES[country]),
            "device": random.choice(DEVICES),
            "browser": random.choice(BROWSERS),
            "referral_source": random.choice(REFERRAL_SOURCES)
        }

        return CustomerEvent(
            event_id=str(uuid4()),
            user_id=user_id,
            session_id=session_id,

            event_type="login",
            event_timestamp=datetime.utcnow(),

            product_id=None,
            product_name=None,
            category=None,

            price=0,
            quantity=0,

            country=self.active_sessions[user_id]["country"],
            city=self.active_sessions[user_id]["city"],

            device=self.active_sessions[user_id]["device"],
            browser=self.active_sessions[user_id]["browser"],

            referral_source=self.active_sessions[user_id]["referral_source"]
        )

    def _create_next_event(self, user_id: int):

        session = self.active_sessions[user_id]

        current_stage = session["current_stage"]

        next_event = random.choice(
            self.STATE_TRANSITIONS[current_stage]
        )

        session["current_stage"] = next_event

        # -------------------------
        # Product Consistency
        # -------------------------
        current_product = session["current_product"]

        if current_product is None:
            product = self._choose_product()
        else:
            product = current_product

        if next_event == "view_product":
            session["current_product"] = product

        product_id = None
        product_name = None
        category = None
        price = 0
        quantity = 0

        if next_event == "view_product":
            product_id = product["id"]
            product_name = product["name"]
            category = product["category"]
            price = product["price"]

            quantity = 1

        elif next_event in [
            "add_to_cart",
            "remove_from_cart",
            "purchase"
        ]:

            product_id = product["id"]
            product_name = product["name"]
            category = product["category"]
            price = product["price"]

            quantity = random.randint(1, 3)

        # -------------------------
        # Country & City Consistency
        # -------------------------
        country = random.choice(COUNTRIES)
        city = random.choice(CITIES[country])

        event = CustomerEvent(

            event_id=str(uuid4()),

            user_id=user_id,

            session_id=session["session_id"],

            event_type=next_event,

            event_timestamp=datetime.utcnow(),

            product_id=product_id,
            product_name=product_name,
            category=category,

            price=price,
            quantity=quantity,

            country=session["country"],
            city=session["city"],

            device=session["device"],
            browser=session["browser"],

            referral_source=session["referral_source"]

        )

        # Clear product after purchase
        if next_event in ["purchase", "remove_from_cart"]:
            session["current_product"] = None

        # End session on logout
        if next_event == "logout":
            del self.active_sessions[user_id]

        return event
    
    def generate_event(self):
        """
        Generate one realistic customer event.
        """

        # Continue an existing session 70% of the time
        if self.active_sessions and random.random() < 0.7:
            user_id = random.choice(list(self.active_sessions.keys()))
            return self._create_next_event(user_id)

        # Otherwise create a new session
        user_id = self._random_user()

        # Ensure the chosen user is not already active
        while user_id in self.active_sessions:
            user_id = self._random_user()

        return self._create_login_event(user_id)