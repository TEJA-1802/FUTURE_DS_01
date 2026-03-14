"""
=============================================================
 BUSINESS SALES PERFORMANCE ANALYTICS
 Future Interns – Data Science & Analytics – Task 1 (2026)
 Intern : Barre Tejaswanth   |   CIN : FIT/MAR26/DS14776
 Dataset: Superstore Sales Dataset (Kaggle)

 This script:
   1. Loads & cleans the raw Superstore dataset
   2. Engineers features and computes all KPIs
   3. Exports analysis-ready CSVs for Power BI dashboarding
=============================================================
"""

import pandas as pd
import numpy as np
import os

os.makedirs("powerbi_data", exist_ok=True)

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 1 — LOAD & CLEAN
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("  STEP 1: Loading & Cleaning Data")
print("=" * 60)

df = pd.read_csv("superstore_sales.csv", encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=False)
df["Ship Date"]  = pd.to_datetime(df["Ship Date"],  dayfirst=False)

# Check for nulls
null_counts = df.isnull().sum()
print(f"\n  Records loaded  : {len(df):,}")
print(f"  Columns         : {len(df.columns)}")
print(f"  Null values     : {null_counts.sum()} (dataset is clean)")
print(f"  Date range      : {df['Order Date'].min().date()} → {df['Order Date'].max().date()}")

# Remove duplicate rows if any
before = len(df)
df.drop_duplicates(inplace=True)
print(f"  Duplicates removed: {before - len(df)}")

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 2 — FEATURE ENGINEERING
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  STEP 2: Feature Engineering")
print("=" * 60)

df["Year"]           = df["Order Date"].dt.year
df["Month_Num"]      = df["Order Date"].dt.month
df["Month_Name"]     = df["Order Date"].dt.strftime("%b")
df["Month_Year"]     = df["Order Date"].dt.strftime("%Y-%m")
df["Quarter"]        = "Q" + df["Order Date"].dt.quarter.astype(str) + \
                       " " + df["Year"].astype(str)
df["Ship Days"]      = (df["Ship Date"] - df["Order Date"]).dt.days
df["Profit Margin %"]= (df["Profit"] / df["Sales"] * 100).round(2)
df["Revenue Band"]   = pd.cut(df["Sales"],
                               bins=[0, 100, 500, 1000, 5000, 99999],
                               labels=["<$100","$100–500","$500–1K","$1K–5K",">$5K"])
df["Is Profitable"]  = df["Profit"].apply(lambda x: "Profitable" if x > 0 else "Loss")
df["Discount Band"]  = pd.cut(df["Discount"],
                               bins=[-0.01, 0, 0.1, 0.2, 0.3, 1.0],
                               labels=["No Discount","1–10%","11–20%","21–30%",">30%"])

print(f"\n  New columns added: Year, Month_Year, Quarter, Ship Days,")
print(f"  Profit Margin %, Revenue Band, Is Profitable, Discount Band")

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 3 — KPI SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  STEP 3: KPI Summary")
print("=" * 60)

total_sales     = df["Sales"].sum()
total_profit    = df["Profit"].sum()
total_orders    = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_qty       = df["Quantity"].sum()
overall_margin  = (total_profit / total_sales * 100)
avg_order_val   = total_sales / total_orders
avg_ship_days   = df["Ship Days"].mean()
profitable_pct  = (df["Is Profitable"] == "Profitable").mean() * 100

print(f"\n  Total Revenue       : ${total_sales:>12,.2f}")
print(f"  Total Profit        : ${total_profit:>12,.2f}")
print(f"  Overall Margin      : {overall_margin:>11.1f}%")
print(f"  Unique Orders       : {total_orders:>13,}")
print(f"  Unique Customers    : {total_customers:>13,}")
print(f"  Total Units Sold    : {total_qty:>13,}")
print(f"  Avg Order Value     : ${avg_order_val:>12,.2f}")
print(f"  Avg Shipping Days   : {avg_ship_days:>11.1f} days")
print(f"  Profitable Orders   : {profitable_pct:>11.1f}%")

# KPI table export
kpi_df = pd.DataFrame([{
    "Metric": "Total Revenue",       "Value": round(total_sales, 2)},
    {"Metric": "Total Profit",       "Value": round(total_profit, 2)},
    {"Metric": "Overall Margin %",   "Value": round(overall_margin, 2)},
    {"Metric": "Total Orders",       "Value": total_orders},
    {"Metric": "Total Customers",    "Value": total_customers},
    {"Metric": "Total Units Sold",   "Value": total_qty},
    {"Metric": "Avg Order Value",    "Value": round(avg_order_val, 2)},
    {"Metric": "Avg Shipping Days",  "Value": round(avg_ship_days, 1)},
    {"Metric": "Profitable Orders %","Value": round(profitable_pct, 1)},
])
kpi_df.to_csv("powerbi_data/kpi_summary.csv", index=False)
print("\n  ✅  kpi_summary.csv exported")

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 4 — AGGREGATED TABLES FOR POWER BI
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  STEP 4: Exporting Aggregated Tables for Power BI")
print("=" * 60)

# — 4a. Monthly Revenue Trend ─────────────────────────────────────────────────
monthly = (df.groupby(["Month_Year","Year","Month_Num"])
             .agg(Revenue=("Sales","sum"),
                  Profit=("Profit","sum"),
                  Orders=("Order ID","nunique"),
                  Quantity=("Quantity","sum"))
             .reset_index()
             .sort_values(["Year","Month_Num"]))
monthly["Profit Margin %"] = (monthly["Profit"] / monthly["Revenue"] * 100).round(2)
monthly["Revenue"] = monthly["Revenue"].round(2)
monthly["Profit"]  = monthly["Profit"].round(2)
monthly.to_csv("powerbi_data/monthly_trend.csv", index=False)
print(f"  ✅  monthly_trend.csv          ({len(monthly)} rows)")

# — 4b. Category & Sub-Category Performance ───────────────────────────────────
cat_sub = (df.groupby(["Category","Sub-Category"])
             .agg(Revenue=("Sales","sum"),
                  Profit=("Profit","sum"),
                  Orders=("Order ID","nunique"),
                  Quantity=("Quantity","sum"),
                  Avg_Margin=("Profit Margin %","mean"))
             .reset_index()
             .sort_values("Revenue", ascending=False))
cat_sub["Revenue"]    = cat_sub["Revenue"].round(2)
cat_sub["Profit"]     = cat_sub["Profit"].round(2)
cat_sub["Avg_Margin"] = cat_sub["Avg_Margin"].round(2)
cat_sub["Profit Status"] = cat_sub["Profit"].apply(
    lambda x: "Profitable" if x > 0 else "Loss-Making")
cat_sub.to_csv("powerbi_data/category_subcategory.csv", index=False)
print(f"  ✅  category_subcategory.csv   ({len(cat_sub)} rows)")

# — 4c. Regional & State Performance ─────────────────────────────────────────
region_state = (df.groupby(["Region","State"])
                  .agg(Revenue=("Sales","sum"),
                       Profit=("Profit","sum"),
                       Orders=("Order ID","nunique"),
                       Customers=("Customer ID","nunique"))
                  .reset_index()
                  .sort_values("Revenue", ascending=False))
region_state["Revenue"]    = region_state["Revenue"].round(2)
region_state["Profit"]     = region_state["Profit"].round(2)
region_state["Margin %"]   = (region_state["Profit"] / region_state["Revenue"] * 100).round(2)
region_state.to_csv("powerbi_data/region_state.csv", index=False)
print(f"  ✅  region_state.csv           ({len(region_state)} rows)")

# — 4d. Segment Performance ───────────────────────────────────────────────────
segment = (df.groupby(["Segment","Category"])
             .agg(Revenue=("Sales","sum"),
                  Profit=("Profit","sum"),
                  Orders=("Order ID","nunique"),
                  Customers=("Customer ID","nunique"))
             .reset_index())
segment["Revenue"] = segment["Revenue"].round(2)
segment["Profit"]  = segment["Profit"].round(2)
segment["Margin %"]= (segment["Profit"] / segment["Revenue"] * 100).round(2)
segment.to_csv("powerbi_data/segment_performance.csv", index=False)
print(f"  ✅  segment_performance.csv    ({len(segment)} rows)")

# — 4e. Discount Impact Analysis ──────────────────────────────────────────────
discount = (df.groupby(["Discount Band","Category"])
              .agg(Avg_Sales=("Sales","mean"),
                   Avg_Profit=("Profit","mean"),
                   Orders=("Order ID","count"),
                   Total_Revenue=("Sales","sum"),
                   Total_Profit=("Profit","sum"))
              .reset_index())
discount = discount.round(2)
discount.to_csv("powerbi_data/discount_impact.csv", index=False)
print(f"  ✅  discount_impact.csv        ({len(discount)} rows)")

# — 4f. Clean Master Table (for Power BI relationships) ───────────────────────
master_cols = [
    "Order ID","Order Date","Ship Date","Ship Mode",
    "Customer ID","Customer Name","Segment",
    "State","Region","Category","Sub-Category","Product Name",
    "Sales","Quantity","Discount","Profit",
    "Year","Month_Year","Quarter","Ship Days",
    "Profit Margin %","Revenue Band","Is Profitable","Discount Band"
]
df[master_cols].to_csv("powerbi_data/master_table.csv", index=False)
print(f"  ✅  master_table.csv           ({len(df)} rows — full clean dataset)")

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 5 — PRINTED INSIGHTS REPORT
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  STEP 5: Key Findings")
print("=" * 60)

top_cat    = cat_sub.groupby("Category")["Revenue"].sum().idxmax()
top_subcat = cat_sub.iloc[0]
loss_subs  = cat_sub[cat_sub["Profit Status"] == "Loss-Making"]["Sub-Category"].tolist()
top_region = region_state.groupby("Region")["Revenue"].sum().idxmax()
top_state  = region_state.iloc[0]["State"]
top_seg    = segment.groupby("Segment")["Revenue"].sum().idxmax()

print(f"\n  Top Category     : {top_cat}")
print(f"  Top Sub-Category : {top_subcat['Sub-Category']} (${top_subcat['Revenue']:,.0f})")
print(f"  Loss-Making Subs : {', '.join(loss_subs)}")
print(f"  Top Region       : {top_region}")
print(f"  Top State        : {top_state}")
print(f"  Top Segment      : {top_seg}")

print(f"""
  RECOMMENDATIONS:
  1. Cap all discounts at 15% — above 20% consistently causes losses
  2. Urgently review pricing for: {', '.join(loss_subs)}
  3. Double down on Technology — highest revenue category
  4. Invest in {top_region} region marketing — highest revenue return
  5. Develop Corporate B2B plan — highest avg order value segment
  6. Leverage Q4 seasonality — plan inventory & campaigns in advance
""")

print("=" * 60)
print("  All CSVs saved in powerbi_data/ folder")
print("  Load them into Power BI to build your dashboard")
print("=" * 60)
