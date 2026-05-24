# Customer Segmentation Analysis Report

This report summarizes the findings from the Customer Segmentation project using K-Means clustering.

## 1. Store Customers (Demographics & Spending)

**Methodology:**
- Dataset: 1000 store customers (`store_customers.csv`).
- Features Used: Age, Annual Income (k$), Spending Score (1-100).
- Optimal Clusters: 2 (determined via Silhouette Score: 0.571).

**Segment Profiles:**

| Segment | Average Age | Avg. Annual Income (k$) | Avg. Spending Score | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Cluster 0** | 32.1 | 41.5 | 53.1 | **Young, Moderate Spenders.** Younger demographic with lower income but reasonable spending habits. |
| **Cluster 1** | 55.0 | 94.2 | 18.1 | **Older, High Income, Low Spenders.** Older demographic with high purchasing power but very conservative spending. |

> [!TIP]
> **Business Action:** The "Older, High Income" segment (Cluster 1) represents a significant untapped opportunity. They have the funds but aren't spending. Tailored marketing for premium, age-appropriate products or luxury services could convert their high income into higher spending scores.

![Store Customers Characteristics](file:///c:/Users/prabh/OneDrive/study/Internships/thiranex/proj-2/results/store_customers_characteristics.png)

---

## 2. Behavioral Segmentation (Detailed Metrics)

**Methodology:**
- Dataset: 50 sample customers (`sample_customer_data.csv`).
- Features Used: Purchase Frequency, Customer Lifetime Value (CLV), Return Rate, Customer Satisfaction Score.
- Optimal Clusters: 4 (determined via Silhouette Score: 0.589).

**Segment Profiles:**

| Segment | Purchase Frequency | Avg. CLV | Satisfaction Score | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Cluster 0** | 14.9 | ~7,500 | 3.57 | **Average Customers.** Steady, moderate buyers with decent satisfaction. |
| **Cluster 1** | 35.5 | ~20,000+ | 4.69 | **Champions.** Very frequent buyers, highest CLV, and exceptionally high satisfaction. |
| **Cluster 2** | 6.5 | ~2,500 | 2.55 | **At-Risk / Low Value.** Infrequent buyers, low value, and very poor satisfaction scores. |
| **Cluster 3** | 25.5 | ~13,000 | 4.27 | **Loyal Spenders.** High frequency and good satisfaction, trailing just behind the Champions. |

> [!WARNING]
> **Business Action (Cluster 2):** Investigate the low satisfaction scores for Cluster 2. High return rates or poor customer service experiences might be driving them away. Intervention is required to prevent churn.

> [!TIP]
> **Business Action (Cluster 1 & 3):** Implement VIP loyalty programs for these segments to retain them, as they drive the vast majority of the Customer Lifetime Value.

![Behavioral Clusters](file:///c:/Users/prabh/OneDrive/study/Internships/thiranex/proj-2/results/behavioral_clusters.png)

---

## Conclusion

By leveraging K-Means clustering, we successfully identified distinct customer groups based on both demographics and behavior. This dual approach allows for highly targeted marketing strategies:
1. **Demographic Targeting:** Focus on unlocking the spending potential of older, high-income customers.
2. **Behavioral Targeting:** Protect the "Champions" while urgently addressing the pain points of the "At-Risk" group.
