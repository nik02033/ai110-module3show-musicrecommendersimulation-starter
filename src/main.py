"""
CLI runner for the Music Recommender Simulation.

Run from the project root:
 python -m src.main
"""

from pathlib import Path

from src.recommender import load_songs, recommend_songs


def _print_recommendations(user_prefs: dict, songs: list, k: int = 5) -> None:
    """Pretty-print ranked picks with scores and per-feature reasons."""
    genre = user_prefs["genre"]
    mood = user_prefs["mood"]
    energy = user_prefs["energy"]
    valence = user_prefs.get("valence", 0.5)

    print(f"\n  Profile: {genre} / {mood}  |  energy {energy}  |  valence {valence}")
    print("  " + "-" * 52)

    rows = recommend_songs(user_prefs, songs, k=k)
    for i, (song, score, reasons) in enumerate(rows, start=1):
        print(f"\n  {i}. {song['title']}")
        print(f"     {song['artist']}  ·  {song['genre']}  ·  {song['mood']}")
        print(f"     Final score: {score:.2f}")
        print("     Reasons:")
        for line in reasons:
            print(f"       • {line}")


def main() -> None:
    """Load the catalog, score against the default pop/happy profile, print top picks."""
    root = Path(__file__).resolve().parent.parent
    csv_path = root / "data" / "songs.csv"

    songs = load_songs(str(csv_path))
    print(f"Loaded songs: {len(songs)}")

    # Default profile from the starter (pop / happy) — verify top pick is on-genre + on-mood
    default_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "valence": 0.85,
        "likes_acoustic": False,
    }

    print("\n" + "=" * 58)
    print("  Music Recommender — CLI (default profile)")
    print("=" * 58)
    _print_recommendations(default_prefs, songs, k=5)

    print("\n" + "=" * 58)


if __name__ == "__main__":
    main()
