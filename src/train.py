from data_loader import load_data
from preprocessing import select_features
from clustering import find_optimal_clusters, train_kmeans
from utils import save_model
import matplotlib.pyplot as plt



# Load data
data = load_data("../data/raw/Mall_Customers.csv")

# Feature selection
X = select_features(data)

# Step 1: Elbow Method
wss = find_optimal_clusters(X)

plt.plot(range(1, 11), wss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WSS")
plt.savefig("../reports/figures/elbow_curve.png")
plt.show()

# Step 2: Train final model
model, labels = train_kmeans(X, k=5)

data['Cluster'] = labels

# Step 3: Save model
save_model(model, "../models/kmeans_model.pkl")

# Save clustered dataset (VERY IMPORTANT for portfolio)
data.to_csv("../data/processed/clustered_customers.csv", index=False)

print("Training completed and model saved!")
