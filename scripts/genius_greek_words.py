"""
Genius API — Greek word-to-song mapper
=======================================
Usage:
  1. pip install requests
  2. Set your Genius Client Access Token below (or as env var GENIUS_TOKEN)
  3. Run: python scripts/genius_greek_words.py
  4. Output is printed as JS-ready objects — paste into sing-the-song.html

Get a free token at: https://genius.com/api-clients
"""

import os
import json
import time
import requests

GENIUS_TOKEN = os.getenv("GENIUS_TOKEN", "PASTE_YOUR_TOKEN_HERE")
BASE_URL = "https://api.genius.com"
HEADERS = {"Authorization": f"Bearer {GENIUS_TOKEN}"}

# ── Words to look up ────────────────────────────────────────────────────────
# Add/remove words here. Each word will be searched on Genius.
WORDS = {
    "easy": [
        # ── months ──
        "Ιανουάριος", "Φεβρουάριος", "Μάρτιος", "Απρίλιος",
        "Μάιος", "Ιούνιος", "Ιούλιος", "Αύγουστος",
        "Σεπτέμβριος", "Οκτώβριος", "Νοέμβριος", "Δεκέμβριος",
        # ── seasons ──
        "άνοιξη", "καλοκαίρι", "φθινόπωρο", "χειμώνας",
        # ── colors ──
        "κόκκινος", "μπλε", "πράσινος", "κίτρινος",
        "μαύρος", "άσπρος", "μωβ", "πορτοκαλί", "ροζ", "ασημένιος",
        # ── days ──
        "Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη",
        "Παρασκευή", "Σάββατο", "Κυριακή",
        # ── nouns ──
        "αγάπη", "νύχτα", "βροχή", "καρδιά", "ήλιος",
        "θάλασσα", "χαρά", "λύπη", "ουρανός", "φεγγάρι",
        "αστέρι", "δρόμος", "μάτια", "ζωή", "μουσική",
        "τραγούδι", "ψυχή", "φτερά", "πόλη", "σπίτι",
        "χορός", "φωτιά", "κόσμος", "φως", "ελπίδα",
        "όνειρο", "πόνος", "φιλί", "αγκαλιά", "σιωπή",
        "νερό", "φίλος", "χέρι", "στιγμή", "παιδί",
        "χαμόγελο", "δάκρυ", "λόγια", "χρόνος", "μέρα",
        "καλοκαίρι", "χειμώνας", "βουνό", "γη", "φύση",
        "φωνή", "κύμα", "πόρτα", "ανάσα", "σκιά",
        # ── adjectives ──
        "όμορφος", "μόνος", "τρελός", "ζεστός", "κρύος",
        "γλυκός", "σκοτεινός", "φωτεινός", "αληθινός", "ελεύθερος",
        "χαρούμενος", "λυπημένος", "δυνατός", "ωραίος", "καλός",
        # ── verbs ──
        "αγαπώ", "χορεύω", "τραγουδώ", "κλαίω", "γελώ",
        "τρέχω", "φεύγω", "μένω", "κοιτώ", "ακούω",
        "θυμάμαι", "ονειρεύομαι", "περιμένω", "ζω", "αγκαλιάζω",
    ],
    "normal": [
        # ── nouns ──
        "μοναξιά", "αλήθεια", "ελευθερία", "δύναμη", "ανάμνηση",
        "παρελθόν", "ευκαιρία", "ταξίδι", "επιστροφή", "χωρισμός",
        "συνάντηση", "νοσταλγία", "αγωνία", "λαχτάρα", "απελπισία",
        "μυστικό", "ευτυχία", "μαγεία", "απόσταση", "εκδίκηση",
        "ζήλεια", "προδοσία", "αντρεία", "αδυναμία", "μελαγχολία",
        "εξουσία", "μνήμη", "παράδεισος", "κόλαση", "αντίσταση",
        # ── adjectives ──
        "μοναχικός", "θλιμμένος", "ξεχασμένος", "αγαπημένος", "χαμένος",
        "ζωντανός", "αδικημένος", "ατέλειωτος", "γλυκόπικρος", "ανίκητος",
        "κρυμμένος", "σπασμένος", "τρελαμένος", "αδύναμος", "ανυπόμονος",
        # ── verbs ──
        "παλεύω", "συγχωρώ", "αλλάζω", "αντέχω", "ελπίζω",
        "φοβάμαι", "προχωρώ", "αφήνω", "χάνομαι", "αναπνέω",
        "αποφασίζω", "σκέφτομαι", "ξεχνώ", "πονάω", "λατρεύω",
    ],
    "hard": [
        # ── adjectives ──
        "παντοτινός", "αναπόφευκτος", "αναντικατάστατος",
        "παραμυθένιος", "αξεπέραστος", "υπερφυσικός",
        "ανεξέλεγκτος", "επαναστατικός", "συγκλονιστικός",
        "διαχρονικός", "αθάνατος", "ξεχωριστός",
        "αδιαχώριστος", "αναπάντεχος", "αμετάκλητος",
        "ανεκπλήρωτος", "αξέχαστος", "απαράμιλλος",
        "ανεξίτηλος", "αδιανόητος", "αξιοθαύμαστος",
        # ── nouns ──
        "αυτοκαταστροφή", "συμφιλίωση", "αναστάτωση",
        "ψευδαίσθηση", "απελευθέρωση", "αντιπαράθεση",
        "αυτοσυγκράτηση", "αναζωπύρωση", "κατακτητής",
        # ── verbs ──
        "αυτοκαταστρέφομαι", "εξουθενώνομαι", "αναστατώνομαι",
        "παραλογίζομαι", "εξιδανικεύω", "αντιπαρατίθεμαι",
    ],
}

MAX_RESULTS = 3          # how many song examples to keep per word
DELAY_SECS  = 0.4        # be polite — don't hammer the API


def search_genius(query: str) -> list[dict]:
    """Return up to MAX_RESULTS hits for a query, filtered to Greek songs."""
    try:
        resp = requests.get(
            f"{BASE_URL}/search",
            headers=HEADERS,
            params={"q": query},
            timeout=8,
        )
        resp.raise_for_status()
        hits = resp.json()["response"]["hits"]
    except Exception as e:
        print(f"  [error] {query}: {e}")
        return []

    results = []
    for hit in hits:
        song   = hit["result"]
        title  = song.get("title", "").strip()
        artist = song.get("primary_artist", {}).get("name", "").strip()
        lang   = song.get("language", "")

        # Keep only Greek-language results (Genius tags them as "el")
        # Fall back to checking if title/artist has Greek characters
        is_greek = (lang == "el") or any(
            "\u0370" <= ch <= "\u03ff" or "\u1f00" <= ch <= "\u1fff"
            for ch in title + artist
        )

        if is_greek and title and artist:
            results.append(f"{title} — {artist}")
            if len(results) >= MAX_RESULTS:
                break

    return results


def main():
    if GENIUS_TOKEN == "PASTE_YOUR_TOKEN_HERE":
        print("ERROR: Set your Genius token in the script or GENIUS_TOKEN env var.")
        return

    all_output = {}

    for difficulty, words in WORDS.items():
        print(f"\n── {difficulty.upper()} ──")
        entries = []

        for word in words:
            songs = search_genius(word)
            if songs:
                entry = {"w": word, "s": songs}
                entries.append(entry)
                print(f"  {word:20s} → {songs[0]}")
            else:
                # Keep word but flag it — fill manually
                entries.append({"w": word, "s": ["TODO — no results found"]})
                print(f"  {word:20s} → [no results]")

            time.sleep(DELAY_SECS)

        all_output[difficulty] = entries

    # ── Print JS-ready output ────────────────────────────────────────────────
    print("\n\n" + "=" * 60)
    print("// ── Paste this into sing-the-song.html (gr section) ──")
    print("=" * 60)
    print("gr: {")
    for difficulty, entries in all_output.items():
        print(f"  {difficulty}: [")
        for e in entries:
            songs_js = json.dumps(e["s"], ensure_ascii=False)
            print(f"    {{ w:{json.dumps(e['w'], ensure_ascii=False):<22s} s:{songs_js} }},")
        print("  ],")
    print("}")


if __name__ == "__main__":
    main()
