import matplotlib.pyplot as plt
import pandas as pd
spotify_clean = pd.read_csv("spotify_clean.csv")
# spotify_clean.head()

plt.figure(figsize=(8,5))
plt.hist(spotify_clean["Popularity"], bins=10, color="lightgreen", edgecolor="black")
plt.title("Track Popularity Distribution")
plt.xlabel("Popularity")
plt.ylabel("Number of Tracks")
plt.show()
