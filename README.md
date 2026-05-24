<h1 align="center">
  🚀 SegmentIQ AI - Customer Analytics Platform
</h1>

<p align="center">
  <strong>An AI-powered Customer Segmentation Dashboard & Data Science Pipeline</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
</p>

---

## 📌 Overview

Welcome to the **Customer Segmentation Project**. This repository demonstrates a complete, end-to-end data science lifecycle—from raw exploratory data analysis and K-Means clustering to a fully functional, production-ready SaaS application with an interactive Glassmorphism UI.

The goal of this project is to intelligently group customers based on their **demographics and purchasing behavior** to unlock actionable business insights, identify "Champions", and prevent "At-Risk" customer churn.

---

## 📂 Repository Structure

```text
├── SegmentIQ/                   # 🌟 The Main AI Web Application (Flask + Plotly)
├── notebooks_and_scripts/       # 📊 Raw Data Science scripts & static visualizations
├── data/                        # 📁 Raw customer datasets (CSV)
├── internship_docs/             # 📝 Original assignment and presentation templates
├── SEGMENTATION_ANALYSIS.md     # 🧠 Detailed business findings and segment insights
└── README.md                    # 📖 You are here!
```

---

## 🌟 1. The SegmentIQ AI Web App

The highlight of this repository is **SegmentIQ**, a full-stack Flask application that brings the Machine Learning models to life. 

### ✨ Features
- **Auto-Segmentation**: Users can upload raw CSV datasets. The backend automatically scales the data, determines the optimal `k` via the Silhouette Method, and clusters the customers using Scikit-Learn.
- **Interactive Dashboards**: Uses Plotly.js to render animated, responsive 2D scatter plots and Elbow method charts.
- **Smart AI Insights**: Dynamically generates plain-English business insights based on the uploaded data.
- **Premium UI**: Built with a custom "Glassmorphism" design system, dark mode, and smooth GSAP animations.
- **Secure Auth**: Full user registration, login, and session management using Flask-Login and Bcrypt.

### 🚀 How to Run the App Locally

1. Navigate to the web app directory:
   ```bash
   cd SegmentIQ
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask server:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser. Register an account, and upload `store_customers.csv` from the `data/` folder to see the AI in action!

---

## 📊 2. The Data Science Pipeline

If you are interested in the raw data analysis, check out the `notebooks_and_scripts/` directory. It contains the original `segmentation.py` script.

### Methodology
1. **Data Preprocessing**: Handled missing values and standardized features (`Age`, `Annual Income`, `Spending Score`) using `StandardScaler`.
2. **Optimal Cluster Selection**: Used the Elbow Method and Silhouette Scores to mathematically determine the best number of segments.
3. **K-Means Clustering**: Segmented the customers into distinct profiles.
4. **Static Visualization**: Generated Seaborn pair plots, box plots, and scatter plots to visualize the distributions.

---

## 💡 Key Findings & Actionable Insights

Through the K-Means clustering algorithm, we successfully identified critical customer segments. You can read the full breakdown in the [SEGMENTATION_ANALYSIS.md](SEGMENTATION_ANALYSIS.md) file.

**Highlight Insights:**
- 🏆 **The "Champions"**: High-frequency buyers with incredible lifetime value. *Action: Enroll in VIP loyalty programs.*
- 💰 **The "High Income, Low Spenders"**: Older demographic with vast purchasing power but conservative spending. *Action: Target with premium/luxury upsells.*
- ⚠️ **The "At-Risk"**: Infrequent buyers with terrible satisfaction scores. *Action: Immediate customer success intervention to prevent churn.*

---

<p align="center">
  <i>Built with ❤️ for advanced data analytics and beautiful UI engineering.</i>
</p>
