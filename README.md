# Blinkit Quick Commerce Analytics | 2023–2024

A full-stack data analytics portfolio project analyzing Blinkit e-commerce data across **2,500+ customers** and **1,061+ orders**.

## 📊 Project Overview

This project demonstrates end-to-end data analytics: from SQL database queries through Python EDA to interactive Tableau visualization.

### Key Findings
- **Regular customers generate MORE revenue than Premium** — counterintuitive insight that challenges typical customer segmentation assumptions
- **30% of orders face delays** — significant operational issue for a speed-first delivery brand
- **Instant & Frozen Food has highest margin (40%)** — not Grocery as expected
- **Tier-2/3 cities (Saharsa, Orai) drive real growth** — Blinkit's expansion opportunity
- **Average order value: ₹2,227** with slight right skew from high-value orders

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Database | MySQL (blinkit_analytics) |
| EDA | Python (pandas, matplotlib, seaborn) |
| Visualization | Tableau Public |
| Data Export | CSV |

---

## 📁 Project Structure

```
blinkit-analytics/
├── README.md
├── blinkit_eda.py                    # Python exploratory data analysis
├── data/
│   ├── customers.csv                 # 2,500 customers
│   ├── orders.csv                    # 1,061 orders
│   ├── products.csv                  # 268 products
│   └── orders_customers.csv          # Joined customer-order data
└── visualizations/
    ├── chart1_segment_revenue.png    # Revenue by customer segment
    ├── chart2_delivery_performance.png # Delivery on-time % analysis
    ├── chart3_category_margin.png    # Margin % by product category
    └── chart4_order_distribution.png # Order value distribution
```

---

## 📊 Tableau Dashboard

**Live Dashboard:** [Blinkit Quick Commerce Analytics](https://public.tableau.com/views/BlinkITEcomAnalyticsFindings2023-24/BlinkitAnalyticsDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Dashboard Components
1. **Delivery Performance** — Pie chart showing on-time vs delayed deliveries
2. **Revenue by Area** — Top performing cities/areas by revenue
3. **Category Margin** — Average margin percentage by product category
4. **Revenue by Segment** — Revenue comparison across customer segments

---

## 📈 Database Schema

### Tables
| Table | Rows | Key Columns |
|-------|------|-------------|
| blinkit_customers | 2,500 | customer_id, segment, city, lifetime_value |
| blinkit_orders | 1,061 | order_id, customer_id, order_total, delivery_status |
| blinkit_products | 268 | product_id, category, margin_percentage |

---

## 🐍 Python Analysis (blinkit_eda.py)

### Output
- 4 publication-ready PNG charts
- Descriptive statistics exported to CSV
- Data cleaning and transformation pipeline

### Libraries Used
- `pandas` — Data manipulation
- `matplotlib` — Static visualizations
- `seaborn` — Statistical graphics
- `mysql.connector` — Database connection

---

## 🚀 How to Use

### 1. Set Up Database
```sql
CREATE DATABASE blinkit_analytics;
USE blinkit_analytics;
-- Import table schemas and data
```

### 2. Run Python Analysis
```bash
python blinkit_eda.py
```

### 3. View Tableau Dashboard
Click the dashboard link above to explore interactive visualizations.

---

## 💡 Business Insights

### Segment Strategy Rethink
- Regular customers (highest volume) outperform Premium segment
- Consider retention programs focused on high-frequency buyers

### Operations Priority
- 30% delayed delivery rate is critical for speed-focused brand
- Opportunity to improve SLA and competitive advantage

### Product Mix Optimization
- Instant & Frozen Food category drives highest margins
- Balance high-margin niche products with high-volume staples

### Geographic Expansion
- Tier-2/3 cities show strong revenue potential
- Saharsa, Orai, Udaipur are growth hotspots

---

## 📝 SQL Queries Executed (Q1–Q10)
Queries cover:
- Revenue analysis by segment, area, and category
- Delivery performance metrics
- Profit margin by category
- Order distribution and trends

---

## 📧 Contact & Portfolio

- **GitHub:** [salimarshad07](https://github.com/salimarshad07)
- **Portfolio:** [salim-portfolio-amber.vercel.app](https://salim-portfolio-amber.vercel.app)
- **LinkedIn:** [Connect here](https://linkedin.com/in/salimarshad07)

---

## 📄 License

This project is open source and available for educational and portfolio purposes.

---

**Built with ❤️ by Salim Arshad | Data Analytics Portfolio Project**
