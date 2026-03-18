# 📊 Business Sales Performance Analytics
**Future Interns – Data Science & Analytics | Task 1 (2026)**

> **Intern:** Barre Tejaswanth | **CIN:** FIT/MAR26/DS14776

---

## 🎯 Objective
Analyze 4 years of real Superstore sales data (2014–2017) to uncover revenue trends, top-performing products, high-value categories, and regional performance — and deliver actionable business recommendations.

---

## 🛠️ Tools Used
| Tool | Purpose |
|------|---------|
| Python 3 | Data cleaning, feature engineering, KPI analysis |
| Pandas & NumPy | Data manipulation and computation |
| Power BI | Interactive dashboard and visual storytelling |

---

## 📁 Repository Structure
```
FUTURE_DS_01/
├── Sample_-_Superstore.csv       ← Raw dataset (9,994 transactions, 2014–2017)
├── sales_analysis.py             ← Python: cleaning, KPIs, exports Power BI CSVs
├── files(1)/
│   ├── master_table.csv          ← Full cleaned dataset with engineered features
│   ├── kpi_summary.csv           ← 9 headline KPIs
│   ├── monthly_trend.csv        ← Monthly revenue & profit trend
│   ├── category_subcategory.csv  ← Performance by category and sub-category
│   ├── region_state.csv          ← Revenue breakdown by region and state
│   ├── segment_performance.csv   ← Customer segment analysis
│   └── discount_impact.csv       ← Discount band vs profit analysis
├── dashboard.pbix                ← Power BI dashboard file
└── README.md
```

---

## 📊 Key Performance Indicators

| Metric | Value |
|--------|-------|
| Total Revenue | $2,297,200 |
| Total Profit | $286,397 |
| Overall Profit Margin | 12.5% |
| Unique Orders | 5,009 |
| Unique Customers | 793 |
| Total Units Sold | 37,873 |
| Avg Order Value | $458.61 |
| Avg Shipping Days | 4.0 days |
| Profitable Orders | 80.6% |

---

## 🔍 Key Business Insights

### 1. 💻 Technology Is the Revenue Engine
Technology leads all categories. Phones ($330K) is the single top sub-category. Copiers deliver the highest profit margin despite lower volume.

### 2. 🌍 West Region & California Dominate
The West region generates the highest revenue. California alone contributes nearly 20% of total revenue — a critical market to protect and grow.

### 3. 📉 Tables, Bookcases & Supplies Are Loss-Making
These three sub-categories are generating **negative profit** despite meaningful revenue. The business is selling them at a loss — requires immediate pricing intervention.

### 4. 🏷️ High Discounts Destroy Profitability
Orders discounted above 20% consistently produce negative average profit. The current discount strategy is a silent revenue killer.

### 5. 📈 Strong Q4 Seasonality Across All Years
Q4 consistently outperforms all quarters — indicating strong end-of-year purchasing patterns to leverage for strategic planning.

### 6. 👤 Corporate Segment Has Highest Order Value
While Consumers drive volume, Corporate orders have a significantly higher average transaction value — a high-priority segment for B2B development.

---

## ✅ Actionable Recommendations

| Priority | Recommendation | Expected Impact |
|----------|---------------|----------------|
| 🔴 High | Cap all discounts at 15% — above 20% causes direct losses | Margin protection |
| 🔴 High | Review pricing for Tables, Bookcases & Supplies | Stop revenue leakage |
| 🟠 Medium | Invest in Technology marketing — highest revenue + margin | Top-line growth |
| 🟠 Medium | Build a Corporate B2B program — higher avg order value | Revenue quality |
| 🟡 Low | Plan Q4 inventory buildup — capitalize on seasonal demand | Peak period gains |
| 🟡 Low | Deepen presence in California & New York — top 2 states | Market concentration |

---

## ▶️ How to Run the Python Analysis

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/FUTURE_DS_01.git
cd FUTURE_DS_01

# 2. Install dependencies
pip install pandas numpy

# 3. Run the analysis — outputs 6 CSVs into powerbi_data/
python sales_analysis.py

# 4. Open Power BI and load files from powerbi_data/
```

---

## 🔗 Program Details
- **Internship:** [Future Interns](https://futureinterns.com)
- **Task Reference:** [DS Task 1 (2026)](https://futureinterns.com/data-science-analytics-task-1-2026/)
- **Dataset:** [Superstore Sales – Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **LinkedIn:** [@Future Interns](https://www.linkedin.com/company/future-interns/)

---
*Submitted as part of the Future Interns Data Science & Analytics Internship Program, March 2026.*
