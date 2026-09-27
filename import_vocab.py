import urllib.request
import csv
import json
import os
import ssl

# פקודה שפותרת את חסימת תעודות האבטחה במחשבי מק
ssl._create_default_https_context = ssl._create_unverified_context

URLS = {
    "N4": "https://raw.githubusercontent.com/elzup/jlpt-word-list/refs/heads/master/src/n4.csv",
    "N5": "https://raw.githubusercontent.com/elzup/jlpt-word-list/refs/heads/master/src/n5.csv"
}
DATA_FILE = "data.json"


def import_github_vocab():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"grammar": [], "vocab": [], "kanji": []}

    vocab_list = data.get("vocab", [])
    existing_words = {item.get("word") for item in vocab_list}
    total_added = 0

    for level, url in URLS.items():
        print(f"מוריד נתונים של {level} מהקישור...")
        try:
            response = urllib.request.urlopen(url)
            lines = [l.decode('utf-8') for l in response.readlines()]
            reader = csv.reader(lines)

            count = 0
            start_id = len(vocab_list) + 1

            for i, row in enumerate(reader):
                if not row:
                    continue

                word = row[0].strip() if len(row) > 0 else ""
                reading = row[1].strip() if len(row) > 1 else ""
                meaning = row[2].strip() if len(row) > 2 else ""

                if not word and not reading:
                    continue
                if not word:
                    word = reading

                # מניעת כפילויות
                if word in existing_words:
                    continue

                vocab_list.append({
                    "id": f"{level.lower()}_import_{start_id + count}",
                    "chapter": f"{level}_GitHub",
                    "word": word,
                    "reading": reading,
                    "meaning": meaning
                })
                existing_words.add(word)
                count += 1

            total_added += count
            print(f"נוספו {count} מילים של {level}.")

        except Exception as e:
            print(f"שגיאה במהלך ייבוא {level}: {e}")

    data["vocab"] = vocab_list

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא מגיטהאב הושלם! סך הכל נוספו {total_added} מילים ל-data.json.")


if __name__ == "__main__":
    import_github_vocab()