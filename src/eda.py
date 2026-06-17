import seaborn as sns
import matplotlib.pyplot as plt



def plot_distributions(df):
    plt.figure(figsize=(15, 8))

    plt.subplot(2, 2, 1)
    sns.histplot(df['Annual Income (k$)'], kde=True)
    plt.title("Annual Income Distribution")

    plt.subplot(2, 2, 2)
    sns.histplot(df['Age'], kde=True)
    plt.title("Age Distribution")

    plt.subplot(2, 2, 3)
    sns.histplot(df['Spending Score (1-100)'], kde=True)
    plt.title("Spending Score Distribution")

    plt.subplot(2, 2, 4)
    sns.countplot(x=df['Gender'])

    plt.tight_layout()
    plt.show()
