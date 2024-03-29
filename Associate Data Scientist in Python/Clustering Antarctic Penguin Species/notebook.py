# Import Required Packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Loading and examining the dataset
penguins_df = pd.read_csv("data/penguins.csv")
print(penguins_df.head())
print(penguins_df.info())
print(penguins_df.isna().sum())

# Data Cleaning
penguins_clean = penguins_df.dropna()
#penguins_clean.boxplot()
#plt.show()
#print(penguins_clean[(penguins_clean["flipper_length_mm"]>4000) | (penguins_clean["flipper_length_mm"]<0)])
penguins_clean = penguins_clean.drop([9, 14])
#penguins_clean.boxplot()
#plt.show()

# Pre-processing (turn catigorical data(sex) into binary)
penguins_dummies = pd.get_dummies(penguins_clean).drop('sex_.', axis=1)
#print (penguins_dummies)

# standardized scaling
scaler = StandardScaler()
penguins_scaled = scaler.fit_transform(penguins_dummies)
penguins_preprocessed = pd.DataFrame(penguins_scaled, columns=penguins_dummies.columns)
#print(penguins_preprocessed)

#PCA
pca = PCA()
pca.fit(penguins_preprocessed)
print(pca.explained_variance_ratio_)
n_components = sum(pca.explained_variance_ratio_ > 0.1)
pca=PCA(n_components=n_components)
penguins_PCA = pca.fit_transform(penguins_preprocessed)

# Clustering
inertia=[]

for k in range(1, 10):
    kmeans= KMeans(n_clusters=k, random_state=42).fit(penguins_PCA)
    inertia.append(kmeans.inertia_)
#plt.plot(range(1,10), inertia, marker="o")
#plt.xlabel("Number of cluster")
#plt.ylabel("Inertia")
#plt.title("Elbow Method")
#plt.show()
n_clusters=4

kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(penguins_PCA)
xs=penguins_PCA[:,0]
ys=penguins_PCA[:,1]
plt.scatter(xs, ys, c=kmeans.labels_, cmap='viridis')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title(f'K-means Clustering (K={n_clusters})')
plt.legend()
plt.show()

# Create a statistical table
penguins_clean["label"] = kmeans.labels_
stat_penguins = penguins_clean[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm','label']].groupby('label').mean()
#print(stat_penguins)

