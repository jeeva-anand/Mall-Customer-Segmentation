# Mall Customer Segmentation

##  Unsupervised Machine Learning for Customer Behavior Analysis

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![Clustering](https://img.shields.io/badge/Unsupervised%20Learning-Clustering-red?style=for-the-badge)
![KMeans](https://img.shields.io/badge/Algorithm-KMeans-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/App-Streamlit-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

 

##  Project Overview

This project applies **Unsupervised Machine Learning (K-Means Clustering)** to segment mall customers based on their:

* Annual Income
* Spending Score
* Age

The goal is to identify **distinct customer groups** to help businesses design **targeted marketing strategies**, improve customer engagement, and maximize revenue.

This project follows a **production-style ML pipeline**, including:

* Modular code structure
* Training pipeline (`train.py`)
* Model persistence
* Streamlit deployment-ready app

 

##  Problem Statement

Retail businesses generate large volumes of customer data but often fail to convert it into actionable insights.

Without segmentation:

* Marketing campaigns are generic
* Customer targeting is inefficient
* Revenue opportunities are missed

This project solves this by applying **clustering techniques to group similar customers** based on behavior patterns.

 

##  Objectives

* Perform Exploratory Data Analysis (EDA)
* Understand customer distribution patterns
* Apply K-Means clustering algorithm
* Identify optimal clusters using Elbow Method
* Build a reproducible ML training pipeline
* Deploy an interactive Streamlit dashboard
* Extract actionable business insights

 

##  Project Architecture

```text id="project-structure"
Mall-Customer-Segmentation/
│
├── data/
│   ├── Mall_Customers.csv
│   └── clustered_customers.csv
│
├── notebooks/
│   ├── 01_eda_analysis.ipynb
│   └── 02_kmeans_clustering.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── visualization.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── app/
│   └── streamlit_app.py
│
├── models/
│   └── kmeans_model.pkl
│
├── reports/
│   └── figures/
│
├── requirements.txt
└── README.md
```

 

##  Machine Learning Pipeline

###  Step 1: Data Loading

Load and inspect customer dataset.

###  Step 2: Exploratory Data Analysis (EDA)

* Age distribution
* Income distribution
* Spending score analysis
* Correlation heatmaps

###  Step 3: Feature Selection

Key features used:

* Annual Income (k$)
* Spending Score (1–100)

###  Step 4: Optimal Cluster Selection

* Elbow Method used to determine best K value
* WCSS (Within-Cluster Sum of Squares) analysis

###  Step 5: Model Training

* KMeans clustering algorithm
* Final model trained with optimal clusters (K=5)

###  Step 6: Model Persistence

* Trained model saved using `joblib`
* Reusable for inference and deployment

 

##  Training Pipeline

The project includes a production-style training script:

```bash id="train-command"
python -m src.train
```

This script:

* Loads data
* Performs feature selection
* Finds optimal clusters
* Trains KMeans model
* Saves model (`kmeans_model.pkl`)
* Stores clustered dataset

 

##  Customer Segments Identified

The model identifies meaningful customer groups:

*  **High Income – High Spending (VIP Customers)**
*  **High Income – Low Spending (Careful Spenders)**
*  **Low Income – High Spending (Impulse Buyers)**
*  **Low Income – Low Spending (Budget Customers)**
*  **Average Customers (Balanced Behavior)**

 

##  Key Business Insights

* High income does not always imply high spending
* Spending behavior is independent of income levels
* Customer segmentation enables personalized marketing
* VIP customers are key revenue drivers
* Budget customers respond better to discounts

 

##  Streamlit Application

An interactive web application allows users to:

* Upload customer dataset
* View clustered results
* Explore customer segments visually
* Analyze group distributions

```bash id="streamlit-run"
streamlit run app/streamlit_app.py
```

 

##  Visualizations

* Elbow Method Curve
* 2D Cluster Visualization
* 3D Cluster Plot (Age, Income, Spending Score)
* Distribution plots for all features
* Correlation heatmap

 

##  Tech Stack

**Programming Language:** Python 
**Data Processing:** Pandas, NumPy
**Visualization:** Matplotlib, Seaborn
**Machine Learning:** Scikit-learn (KMeans)
**Deployment:** Streamlit
**Model Persistence:** Joblib

 

##  How to Run This Project

```bash id="run-steps"
# Clone repository
git https://github.com/jeeva-anand/Mall-Customer-Segmentation

# Navigate to project
cd Mall-Customer-Segmentation

# Install dependencies
pip install -r requirements.txt

# Run training pipeline
python -m src.train

# Launch Streamlit app
streamlit run app.py
```

 

##  Real-World Applications

* Customer segmentation in retail stores
* Personalized marketing campaigns
* Product recommendation systems
* Customer behavior analytics
* Business decision-making support

 

##  Skills Demonstrated

* Unsupervised Machine Learning
* K-Means Clustering
* Feature Engineering
* Data Cleaning & Preprocessing
* Data Visualization & Storytelling
* Model Pipeline Design
* Deployment using Streamlit

 

##  Future Improvements

* Add PCA-based dimensionality reduction
* Compare multiple clustering algorithms (DBSCAN, Hierarchical)
* Build advanced interactive dashboards
* Integrate real-time customer analytics system
* Deploy on cloud (AWS / Streamlit Cloud)

 



# If You Like This Project

Feel free to star ⭐ the repository and contribute improvements!
