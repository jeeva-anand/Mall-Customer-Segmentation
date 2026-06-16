
# Customer Segmentation – Mall Customers

##  Project Overview

This project focuses on **customer segmentation** using unsupervised machine learning.
The goal is to group mall customers based on their purchasing behavior so that marketing strategies can be better targeted.

We use the **K-Means Clustering algorithm** to identify meaningful customer groups from behavioral and demographic data.

---

##  Dataset Information

The dataset is created purely for learning purposes and represents customers of a supermarket mall.

It includes the following features:

* **CustomerID** → Unique identifier for each customer
* **Gender** → Male / Female
* **Age** → Age of the customer
* **Annual Income (k$)** → Yearly income in thousands
* **Spending Score (1–100)** → Score assigned based on customer spending behavior and purchasing patterns

---

##  Problem Statement

As a mall owner, the goal is to understand your customers and identify:

* Which customers are most valuable
* Which customers are frequent spenders
* Which customers can be targeted easily by marketing campaigns

This helps in designing **effective marketing strategies** and improving customer engagement.

---

##  Machine Learning Approach

We use **Unsupervised Learning** since we do not have labeled outputs.

### Algorithm Used:

* K-Means Clustering

### Why K-Means?

* Simple and efficient for segmentation
* Works well with numerical customer data
* Helps identify hidden patterns in spending behavior

---

##  Workflow

1. Import and explore dataset
2. Perform exploratory data analysis (EDA)
3. Select important features (e.g., Income, Spending Score)
4. Determine optimal number of clusters using **Elbow Method**
5. Apply K-Means clustering
6. Visualize customer segments
7. Interpret and analyze clusters

---

##  Expected Outcome

After clustering, customers are grouped into segments such as:

* High income – high spending 
* High income – low spending
* Low income – high spending
* Low income – low spending

These insights help the marketing team:

* Personalize offers
* Improve customer retention
* Increase sales conversion

---

##  Technologies Used

* Python 
* Pandas
* NumPy
* Matplotlib / Seaborn
* Scikit-learn

---

## How to Run the Project

```bash
# Clone the repository
git clone https://github.com/your-username/customer-segmentation.git

# Move into directory
cd customer-segmentation

# Install dependencies
pip install -r requirements.txt

# Run the notebook or script
jupyter notebook
```

---

