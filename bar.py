import matplotlib.pyplot as plt
import pandas as pd
spotify_clean = pd.read_csv("spotify_clean.csv")
spotify_clean.head()

top_artists = spotify_clean["Artist"].value_counts().head(10)

plt.figure(figsize=(8,5))
top_artists.plot(kind="bar", color="skyblue")
plt.title("Top 10 Artists in My Spotify")
plt.ylabel("Number of Tracks")
plt.xlabel("Artist")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()