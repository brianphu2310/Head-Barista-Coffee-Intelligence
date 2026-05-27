<img width="1279" height="755" alt="image" src="https://github.com/user-attachments/assets/06ff26d6-d727-4baa-a6b6-ec92d390bbc4" /> (ảnh dasboard tableau)
<img width="1512" height="846" alt="image" src="https://github.com/user-attachments/assets/cb1ab262-84cf-43aa-8134-9a19d011986d" /> ( ảnh streamlit app)

https://www.linkedin.com/in/brian-phu-data-analysta55353390/ (trang chính)
https://www.kaggle.com/brianphu   (trang chính)
https://public.tableau.com/app/profile/brian.ma5935/vizzes   (trang chính)
https://public.tableau.com/app/profile/brian.ma5935/viz/Cofffee_Brian_Project/Dashboard3  (Tableau dashboard)
https://testing-wzx24gsioxffy3mkvtvnsj.streamlit.app  (streamlit App)
https://colab.research.google.com/drive/1uCOkUri0_LfMO2CzFqoj9uhfkYfHehvo (colab charts)
<img width="1076" height="784" alt="image" src="https://github.com/user-attachments/assets/f9991756-ebb2-4eaf-a4e0-057cb7ba4d02" /> (ảnh colab)

# ☕ Coffee Sales Intelligence
### *An end-to-end data project exploring what actually drives coffee revenue — across products, customers, and countries*

[![Streamlit App](https://img.shields.io/badge/☕_Streamlit_App-Live-00C7A3?style=for-the-badge&logo=streamlit&logoColor=white)](https://testing-wzx24gsioxffy3mkvtvnsj.streamlit.app)
[![Tableau](https://img.shields.io/badge/📊_Tableau_Dashboard-Live-9B59EF?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/brian.ma5935/viz/Cofffee_Brian_Project/Dashboard3)
[![Colab](https://img.shields.io/badge/📓_Full_Analysis-Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1uCOkUri0_LfMO2CzFqoj9uhfkYfHehvo)
[![Kaggle Dataset](https://img.shields.io/badge/📦_Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/brianphu)
[![License: MIT](https://img.shields.io/badge/License-MIT-gray?style=for-the-badge)](LICENSE)

---

## The Question I Was Actually Trying to Answer

I drink a lot of coffee. More than I should. And at some point I stopped just consuming it and started wondering about the business behind it.

A friend who runs a small café kept asking the same question every month: **"Why does my revenue spike in some months and flatline in others — and why does it seem random?"**

She was tracking sales in a spreadsheet, but the spreadsheet couldn't tell her *why*. It showed her numbers. It didn't show her patterns.

That question became this project.

> *If you had complete transactional data — every order, every customer, every product — what would you actually be able to predict? And more importantly, what would you actually be able to change?*

I stopped guessing and built a data pipeline to find out.

---

## 🎯 What This Project Solves

### Problem 1: Revenue looks flat until you break it down

| Before | After |
|--------|-------|
| Monthly revenue totals hide what's actually moving | **Time-series breakdown** by product, roast type, and country |
| "Sales are up" or "sales are down" with no context | **Trend analysis** shows seasonality and peak periods clearly |
| No way to tell if growth is real or just one big order | **Order count vs revenue** visualised separately |

**Solution:** Tableau dashboard with dynamic time filters + Streamlit KPI cards.

---

### Problem 2: No one knows which product is actually profitable

| Before | After |
|--------|-------|
| Arabica sells the most units — so it must be the best performer? | **Revenue per unit** separated by coffee type |
| Roast type preference is assumed, not measured | **Roast type breakdown** (Light / Medium / Dark) by revenue and volume |
| Pack size decisions made by gut feel | **Size analysis** (0.2kg / 0.5kg / 1kg / 2.5kg) shows where real revenue comes from |

**Solution:** Multi-dimensional product analysis in Python (Pandas) + Tableau bar and pie charts.

---

### Problem 3: Customer value is invisible without segmentation

| Before | After |
|--------|-------|
| All customers treated equally regardless of spend | **Top 5 customers by revenue** identified and ranked |
| No way to tell if loyalty cards actually work | **Loyalty card holders vs non-holders** spend comparison |
| Repeat customers and one-time buyers mixed together | **Customer segmentation** by purchase frequency and total value |

**Solution:** Customer-level aggregation + Streamlit interactive filters.

---

### Problem 4: Geography is ignored entirely

| Before | After |
|--------|-------|
| Revenue treated as one global number | **Country-level breakdown:** USA, UK, Ireland |
| No idea which market is growing fastest | **Monthly trend by country** shows diverging trajectories |
| Marketing spend allocated without geographic data | **Choropleth map** in Streamlit shows where the money comes from |

**Solution:** Geographic analysis in Plotly + Tableau map view.

---

## 🖼️ Live Demos

### 1 — Tableau Dashboard · Executive View

> 🔗 **[View Dashboard →](https://public.tableau.com/app/profile/brian.ma5935/viz/Cofffee_Brian_Project/Dashboard3)**

![Tableau Dashboard](assets/tableau_dashboard.png)

**What you can do:**
- Filter by date range, country, roast type, and pack size
- Track total revenue, order count, and average order value over time
- Compare coffee type performance side by side
- Identify top customers instantly

---

### 2 — Streamlit Web App · Interactive Explorer

> 🔗 **[Launch App →](https://testing-wzx24gsioxffy3mkvtvnsj.streamlit.app)**

![Streamlit App](assets/streamlit_app.png)

**Features:**
- 🔍 Dynamic filters (date range, country, roast type, size)
- 📊 Real-time KPI cards: Total Revenue, Total Orders, Avg Order Value
- 🌍 Interactive world map of sales by country
- 📋 Raw data explorer with CSV export
- 📈 Revenue trend line with selectable grouping (daily / monthly / quarterly)

---

### 3 — Google Colab · Full Statistical Analysis

> 🔗 **[Open in Colab →](https://colab.research.google.com/drive/1uCOkUri0_LfMO2CzFqoj9uhfkYfHehvo)**

![Colab Analysis](assets/colab_charts.png)

**What's in the notebook:**
- Data cleaning and preprocessing pipeline
- Univariate and bivariate EDA
- Monthly and quarterly seasonality analysis
- Customer segmentation (RFM-style: Recency, Frequency, Monetary)
- Correlation heatmaps and distribution plots
- Loyalty card impact analysis

Click **Runtime → Run all** to reproduce every chart.

---

## 📦 Dataset

The cleaned dataset is published on Kaggle so anyone can use it — no setup required.

> 🔗 **[Download dataset → kaggle.com/brianphu](https://www.kaggle.com/brianphu)**

**Source:** `coffeeOrdersData.xlsx` — a realistic transactional sales dataset covering orders, customers, and products across three countries.

**What's included:**

| File | Rows | Description |
|------|------|-------------|
| `coffeeOrdersData.xlsx` | ~1,000 orders | Raw transactional data (3 sheets: Orders, Customers, Products) |
| `coffee_cleaned.csv` | ~1,000 rows | Merged and cleaned master dataset for Python analysis |

**Column reference (merged dataset):**

| Column | Type | Example |
|--------|------|---------|
| `order_id` | string | QEV-37451-860 |
| `order_date` | date | 2021-09-05 |
| `customer_name` | string | Aloisia Allner |
| `country` | string | United States |
| `coffee_type` | string | Arabica |
| `roast_type` | string | Medium |
| `size_kg` | float | 2.5 |
| `unit_price` | float | 11.95 |
| `quantity` | int | 2 |
| `sales` | float | 23.90 |
| `loyalty_card` | bool | Yes |

---

## 📊 Key Findings

### Finding 1 — The United States dominates, but the gap is wider than expected

| Country | Total Revenue | Share |
|---------|--------------|-------|
| 🇺🇸 United States | $35,639 | 79.2% |
| 🇮🇪 Ireland | $6,697 | 14.9% |
| 🇬🇧 United Kingdom | $2,799 | 6.2% |

The US isn't just the largest market — it's the market. Ireland punches above its weight relative to population. UK growth is the most inconsistent month-to-month.

---

### Finding 2 — Liberica generates the highest revenue per unit

| Coffee Type | Total Revenue | Avg Unit Price | % of Orders |
|-------------|--------------|----------------|-------------|
| Arabica | $12,054 | $11.20 | 26.8% |
| Excelsa | $12,306 | $11.40 | 27.0% |
| **Liberica** | **$12,893** | **$12.10** | 25.2% |
| Robusta | $8,093 | $9.80 | 21.0% |

> Arabica sells the most units but Liberica generates the most revenue per transaction. If you're margin-focused, Liberica is the product to push.

---

### Finding 3 — 2.5kg packs drive disproportionate revenue

| Pack Size | % of Orders | % of Revenue |
|-----------|-------------|--------------|
| 0.2 kg | 25% | 8% |
| 0.5 kg | 28% | 18% |
| 1.0 kg | 25% | 27% |
| **2.5 kg** | **22%** | **47%** |

The 2.5kg pack represents fewer than a quarter of orders but nearly half of total revenue. This is the unit economics story the raw data hides.

---

### Finding 4 — Loyalty card holders spend more, consistently

| Group | Avg Order Value | Avg Orders per Customer |
|-------|----------------|------------------------|
| No loyalty card | $14.20 | 2.8 |
| **Loyalty card** | **$16.70** | **3.4** |

Loyalty card holders spend ~18% more per order and place ~21% more orders. Real effect — but the bigger driver of repeat purchases is recency. Customers who ordered in the last 6 months are 3× more likely to order again.

---

## 🏗️ Data Pipeline

```
coffeeOrdersData.xlsx
│   (3 sheets: Orders / Customers / Products)
│
▼
Data Cleaning & Merging (Pandas)
│   Coffee_EDA.ipynb
│
├── Standardise date formats
├── Fill missing customer names via order_id join
├── Map coffee abbreviations → full names
│   (Rob → Robusta, Exc → Excelsa, Ara → Arabica, Lib → Liberica)
├── Map roast abbreviations → full names
│   (M → Medium, L → Light, D → Dark)
├── Calculate derived columns: sales = unit_price × quantity
└── Validate: no duplicate order IDs, no negative sales
│
▼
coffee_cleaned.csv              ← master cleaned file
│
├──► Exploratory Data Analysis (Matplotlib + Seaborn + Plotly)
│    Coffee_EDA.ipynb
│
├──► Tableau Dashboard
│    coffeeOrdersData.xlsx (direct Tableau connection)
│    Dashboard: Sales trend / Top customers / Coffee type / Country
│
└──► Streamlit Web App
     coffee_app.py
     KPI cards + dynamic filters + Plotly choropleth map
```

---

## ⚙️ Technical Stack

| Layer | Tool | Why This Tool |
|---|---|---|
| Data source | Excel (xlsx) | Native format; 3-sheet relational structure |
| Processing | Pandas, NumPy | Vectorized join, groupby, and aggregation |
| Visualisation | Matplotlib, Seaborn, Plotly | Static EDA + interactive charts in one notebook |
| Web app | Streamlit | Fast path from Python DataFrame to deployed product |
| BI dashboard | Tableau Public | Stakeholder-facing, filter-driven executive view |
| Deployment | Streamlit Cloud | Zero-infrastructure hosting; auto-deploys from GitHub |

---

## 📁 Project Structure

```
coffee-sales-intelligence/
│
├── Coffee_EDA.ipynb                # Full EDA + analysis + charts
│
├── coffee_app.py                   # Streamlit web app
├── requirements.txt                # Pinned dependencies
│
├── coffeeOrdersData.xlsx           # Raw source data (3 sheets)
├── coffee_cleaned.csv              # Merged and cleaned master dataset
│
├── assets/
│   ├── tableau_dashboard.png       # Dashboard screenshot
│   ├── streamlit_app.png           # App screenshot
│   └── colab_charts.png            # Notebook screenshot
│
└── README.md
```

---

## 🚀 How to Run Locally

```bash
# Clone
git clone https://github.com/brianphu2310/coffee-sales-intelligence.git
cd coffee-sales-intelligence

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run coffee_app.py
```

**Or open the notebook directly:**

```bash
jupyter notebook Coffee_EDA.ipynb
```

**Want the data without cloning?** Download from Kaggle:

```bash
kaggle datasets download brianphu/coffee-sales-intelligence
```

---

## ⚠️ Limitations & What I'd Do With More Data

The dataset covers a fixed time window with three countries and ~1,000 orders. Enough to find patterns — not enough to build a forecasting model worth deploying.

With more data I would:

- **Add cost data** — revenue without margin is incomplete; Liberica might look great on revenue but if the beans cost more, the margin story changes
- **Segment customers properly with full RFM** — the current dataset lacks enough repeat purchases per customer to build robust recency/frequency/monetary tiers
- **Build a demand forecast** — with 3+ years of monthly data, a Prophet or SARIMA model would predict peak months and inform stock decisions
- **Test loyalty card attribution causally** — the current analysis shows correlation; a proper A/B test would establish whether the loyalty card *causes* higher spend or just attracts customers who already spend more

---

## 📬 About

**Brian Phu** — Data Analyst, Sydney

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brian-phu-data-analysta55353390/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/brianphu2310)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/brianphu)
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/brian.ma5935/vizzes)

> *"My friend's café question started this. She wanted to know why her revenue was unpredictable. The data had the answer — it just needed someone to ask it properly."*

---

**Last updated:** May 2026 &nbsp;|&nbsp; **Orders analysed:** ~1,000 &nbsp;|&nbsp; **Countries:** 3 (USA, Ireland, UK) &nbsp;|&nbsp; **Dashboards:** 3 (Streamlit, Colab, Tableau) &nbsp;|&nbsp; One too many coffees

---

*MIT License — free to use, modify, and share.*
