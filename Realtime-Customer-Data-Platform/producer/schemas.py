from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional


@dataclass
class CustomerEvent:
    event_id: str
    user_id: int
    session_id: str

    event_type: str
    event_timestamp: datetime

    product_id: Optional[str]
    product_name: Optional[str]
    category: Optional[str]

    price: float
    quantity: int

    country: str
    city: str

    device: str
    browser: str

    referral_source: str

    def to_dict(self):
        """
        Convert the event into a dictionary.
        """
        data = asdict(self)

        # Convert datetime into ISO-8601 string
        data["event_timestamp"] = self.event_timestamp.isoformat()

        return data