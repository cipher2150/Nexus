# Phase 1 - Real-Time Customer Event Simulator

The first phase of **Nexus** focuses on building a realistic customer event generator capable of producing high-quality clickstream data for a real-time customer data platform.

Instead of generating completely random events, this simulator models realistic customer journeys using a state machine, making the generated data suitable for streaming pipelines, analytics, and data engineering projects.

---

# Objective

Build a scalable event producer that continuously simulates customer interactions on an e-commerce platform and publishes them to Apache Kafka.

The generated events will later be consumed by Spark Structured Streaming and processed through a Medallion Architecture (Bronze → Silver → Gold).

---

# Architecture

```
Customer Simulator
        │
        ▼
Kafka Producer
        │
        ▼
customer-events Topic
```

---

# Features Implemented

## Realistic Customer Journey

Instead of generating random events, every customer follows a logical navigation flow.

Example:

```
Login
   │
   ▼
Page View
   │
   ▼
Search
   │
   ▼
View Product
   │
   ▼
Add to Cart
   │
   ├────────────► Remove from Cart
   │
   ▼
Purchase
   │
   ▼
Logout
```

---

## Stateful Session Management

Each customer has an active session containing:

- Session ID
- Current Journey Stage
- Current Product
- Country
- City
- Device
- Browser
- Referral Source

This ensures every event in a session remains consistent.

---

## Session Consistency

Each session maintains:

- Same Session ID
- Same Country
- Same City
- Same Device
- Same Browser
- Same Referral Source

until the customer logs out.

Example:

```
Session ID
↓

Login
↓

Page View
↓

Search
↓

View Product
↓

Purchase
↓

Logout
```

---

## Product Consistency

Once a customer views a product, the same product is carried through subsequent events such as:

- View Product
- Add to Cart
- Remove from Cart
- Purchase

This simulates realistic shopping behavior.

---

## Multiple Concurrent Users

The simulator supports multiple active customers simultaneously.

Example:

```
User 102
    Shopping

User 564
    Searching

User 918
    Purchasing

User 220
    Browsing
```

Each customer progresses independently through their own session.

---

## State Machine Based Navigation

Customer behavior is controlled using a state transition model.

```
Login
    │
    ▼
Page View
    │
    ▼
Search
    │
    ▼
View Product
    │
    ▼
Add to Cart
   / \
  /   \
Purchase Remove Cart
      │
      ▼
 Continue Browsing
```

This prevents unrealistic event sequences.

---

## Rich Event Metadata

Every generated event includes:

### User Information

- User ID
- Session ID

### Event Information

- Event ID
- Event Type
- Event Timestamp

### Product Information

- Product ID
- Product Name
- Category
- Price
- Quantity

### Customer Context

- Country
- City
- Device
- Browser
- Referral Source

---

# Event Types

The simulator currently supports:

- Login
- Logout
- Page View
- Search
- View Product
- Add to Cart
- Remove from Cart
- Purchase

---

# Sample Event

```json
{
  "event_id": "80147ac0-a36d-43fd-ade6-9f16ab513949",
  "user_id": 554,
  "session_id": "ff97ccb6-4b62-4943-aa2a-9755a7e243a3",
  "event_type": "view_product",
  "event_timestamp": "2026-07-02T18:23:15.533275",
  "product_id": "P1001",
  "product_name": "MacBook Air M4",
  "category": "Laptops",
  "price": 99999,
  "quantity": 1,
  "country": "United States",
  "city": "New York",
  "device": "Desktop",
  "browser": "Safari",
  "referral_source": "Google"
}
```

---

# Technologies Used

- Python
- Apache Kafka
- Faker
- UUID
- Dataclasses / Pydantic
- Docker (Upcoming)

---

# Project Structure

```
producer/

├── config.py
├── customer_simulator.py
├── kafka_producer.py
├── schemas.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Current Status

- ✅ Realistic customer journey simulation
- ✅ Stateful session management
- ✅ Product consistency
- ✅ Location consistency
- ✅ Device consistency
- ✅ Multiple concurrent users
- ✅ Kafka producer integration
- ✅ Continuous event generation

---

