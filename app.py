from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram
import os

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('rfm_data.csv')

    X = df[['Recency', 'Frequency', 'Monetary']]

    Z = linkage(X, method='ward')

    plt.figure(figsize=(12, 6))
    dendrogram(Z, labels=df['CustomerID'].values, leaf_rotation=90)
    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Customer ID")
    plt.ylabel("Distance")
    plt.tight_layout()
    plt.savefig('static/dendrogram.png')
    plt.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
