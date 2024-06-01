import pandas as pd
from sklearn.datasets import make_blobs

# Generate 100 data points with 2 features and 3 centers
X, y = make_blobs(n_samples=250, n_features=2, centers=3, random_state=42)

# Convert the data points into a DataFrame
df = pd.DataFrame(X, columns=['Feature1', 'Feature2'])

# Save the DataFrame to an Excel file
df.to_excel("kmeans_data.xlsx", index=False)

