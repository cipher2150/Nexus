# Nexus

> An end-to-end real-time data platform that ingests, processes, and analyzes customer interaction events using Apache Kafka, Databricks, PySpark, and Delta Lake. The platform follows the Medallion (Bronze–Silver–Gold) Architecture and powers real-time clickstream analytics with AI-generated business insights.

---

## Overview

Modern organizations generate millions of customer events every day, such as logins, page views, searches, purchases, and clicks. Processing this data in real time enables businesses to understand customer behaviour, monitor key metrics, and make data-driven decisions.

This project simulates a production-grade streaming data platform by combining a **Customer Data Platform (CDP)** with a **Realtime Clickstream Analytics Platform**.

The platform:

- Streams customer events in real time
- Validates and processes incoming data
- Stores data using Delta Lake (Bronze, Silver, Gold)
- Builds analytics-ready datasets
- Computes business KPIs
- Generates AI-powered business insights

---

# Architecture

```text
                    Customer Events
      (Login, Search, Click, Purchase, Logout)
                           │
                           ▼
                Python Event Generator
                           │
                           ▼
                   Redpanda (Kafka)
                           │
                           ▼
                     Bronze Parquet
                           │
                           ▼
-------------------------------------------------------
                      (Databricks)
                Bronze Delta Table (Raw)
                           │
                           ▼
               Silver Delta Table (Clean)
                           │
                           ▼
              Gold Delta Tables (Business)
                           │
           ┌───────────────┴────────────────┐
           │                                │
           ▼                                ▼
 Customer Data Platform      Clickstream Analytics
           │                                │
           └───────────────┬────────────────┘
                           ▼
               AI Business Insights
```

---

# Features

### Customer Data Platform

- Real-time event ingestion
- Kafka streaming pipeline
- Databricks Structured Streaming
- Delta Lake (Bronze, Silver, Gold)
- Data validation and transformation
- SQL-ready business datasets

### Clickstream Analytics

- Daily Active Users (DAU)
- Monthly Active Users (MAU)
- Conversion Rate
- Bounce Rate
- Session Duration
- Revenue Analysis
- Product Performance
- User Behavior Analytics

### AI Insights

- Automated business summaries
- Revenue trend analysis
- Customer engagement insights
- Product performance summaries
- Executive reports using Generative AI

---

# Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python, SQL |
| Streaming | Apache Kafka |
| Processing | Apache Spark (PySpark) |
| Platform | Databricks |
| Lakehouse | Delta Lake |
| Analytics | Databricks SQL |
| AI | Gemini |
| Version Control | Git, GitHub |
| Containerization | Docker |

---

# Medallion Architecture

## Bronze Layer

- Raw streaming events
- Immutable data
- Source of truth

## Silver Layer

- Data validation
- Data cleaning
- Deduplication
- Schema enforcement

## Gold Layer

Business-ready datasets for analytics:

- Customer Metrics
- Session Metrics
- Revenue Metrics
- Product Metrics

---

# Business KPIs

The platform computes real-time metrics including:

- Daily Active Users (DAU)
- Monthly Active Users (MAU)
- Conversion Rate
- Bounce Rate
- Top Products
- Customer Engagement
- Returning Users
- New Users

---


# Data Flow

```text
Generate Events
        │
        ▼
Kafka Topic
        │
        ▼
Databricks Streaming
        │
        ▼
Bronze
        │
        ▼
Silver
        │
        ▼
Gold
        │
 ┌──────┴───────┐
 ▼              ▼
Analytics    AI Insights
```

---



---

# Project Highlights

- End-to-end real-time streaming data pipeline
- Lakehouse architecture using Delta Lake
- Medallion (Bronze–Silver–Gold) data model
- Real-time customer analytics
- SQL-based business metrics
- AI-generated business insights
- Modular and scalable architecture

---

# Future Improvements

- Real-time dashboarding
- Advanced anomaly detection
- Customer segmentation
- Predictive analytics
- Multi-source event ingestion
- Automated workflow orchestration

---

# Author

**Rajshekhar Prasad Saxena**

Data Engineer | Backend Developer
