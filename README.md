# Hierarchical_Clustering
#  Hierarchical Clustering on RFM Data — Flask Web App
```
This project demonstrates unsupervised learning using **Hierarchical Clustering** on customer **RFM data** (Recency, Frequency, Monetary). The web app, built using Flask, visualizes the **dendrogram** of customer segments and optionally assigns clusters.
```
---

##  Project Structure
```
hierarchical_rfm/
├── app.py # Main Flask app
├── rfm_data.csv # Sample dataset (30 customers)
├── templates/
│ └── index.html # Web UI with dendrogram
├── static/
│ └── style.css # Optional styling
├── requirements.txt # Python dependencies
```
---

##  Dataset Description (`rfm_data.csv`)
```
| Feature     | Description                                |
|-------------|--------------------------------------------|
| Recency     | Days since last purchase                   |
| Frequency   | Number of purchases                        |
| Monetary    | Total amount spent                         |
```
```
This format is ideal for identifying **customer segments** such as:
- Loyal Customers
- New or Infrequent Buyers
- High Spenders
```
---

##  How to Run the App

# 1. Clone or Download the Repository

```
git clone https://github.com/yourusername/hierarchical_rfm.git
cd hierarchical_rfm
```
# 2. Install Dependencies
```
Make sure Python 3.8+ is installed.
```
```
pip install -r requirements.txt
```
# 3. Run the Flask App
```
python app.py
```
# In app.py:
```
python
Copy code
from scipy.cluster.hierarchy import fcluster
df['Cluster'] = fcluster(Z, t=3, criterion='maxclust')
You can then modify index.html to show statistics or cluster-specific insights.
```
# Why Hierarchical Clustering?
```
Reveals natural customer groupings

Visual and interpretable (via dendrograms)

Doesn’t require pre-specifying k like K-Means
```

# Requirements
```
Flask
pandas
matplotlib
scipy
```
# ScreenShot
![alt text](<Screenshot 2025-08-03 161003.png>)