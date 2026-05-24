# SegmentIQ AI - Customer Analytics Dashboard

SegmentIQ is a premium, AI-powered customer segmentation platform. Built with a modern Flask backend and a highly polished glassmorphism frontend, it allows businesses to upload their customer data and instantly generate machine-learning driven insights and interactive visualizations.

## Features
- **Auto-Segmentation**: Upload a CSV and K-Means clustering automatically groups your customers.
- **AI Insights**: Generates plain-english business insights based on the data.
- **Interactive Dashboards**: Uses Plotly.js to render animated, responsive charts.
- **Secure Authentication**: Built-in user accounts and secure dataset storage per user.
- **Premium UI**: Custom CSS featuring floating gradients, glassmorphism, and GSAP animations.

## How to Run

1. **Install Python Requirements**
```bash
pip install -r requirements.txt
```

2. **Run the Application**
```bash
python app.py
```

3. **Open the Dashboard**
Navigate to `http://127.0.0.1:5000` in your web browser.

## Testing with Data
Use the `store_customers.csv` file from the parent directory. It contains `CustomerID`, `Gender`, `Age`, `Annual Income`, and `Spending Score`, which fits the model perfectly!
