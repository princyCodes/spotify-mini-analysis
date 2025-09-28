import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
spotify_clean = pd.read_csv("spotify_clean.csv")

# Keep only tracks with known genres
known_genres_df = spotify_clean[spotify_clean["Genres"] != "Unknown"]

known_genres_df = known_genres_df["Genres"].value_counts().head(10)  # top 10 genres

plt.figure(figsize=(6,6))
known_genres_df.plot(kind="pie", autopct="%1.1f%%", startangle=140, cmap="tab20")
plt.title("Genre Distribution")
plt.ylabel("")  # hide y-label
plt.show()
