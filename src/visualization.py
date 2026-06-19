import matplotlib.pyplot as plt
import seaborn as sns


def plot_clusters_2d(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x='Annual Income (k$)',
        y='Spending Score (1-100)',
        hue='label',
        data=df,
        palette='Set1'
    )
    plt.title("Customer Segments")
    plt.show()
