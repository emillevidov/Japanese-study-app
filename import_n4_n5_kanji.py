import csv
import json
import os

DATA_FILE = "data.json"
CSV_FILE = "JLPT_kanji_ALL.csv"

try:
    # 1. טעינת הנתונים הקיימים מ-data.json
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"kanji": [], "vocab": [], "grammar": []}

    existing_kanji = {item.get("kanji") for item in data.get("kanji", [])}

    # 2. קריאת קובץ ה-CSV וסינון רמות 4 ו-5 (N4, N5)
    n4_n5_kanji = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # דילוג על כותרת אם קיימת
        for row in reader:
            if len(row) >= 2:
                kanji_char = row[0].strip()
                level = row[1].strip()
                if level in ["4", "5"]:
                    n4_n5_kanji.append((kanji_char, level))

    # 3. הוספת קאנג'י חדשים בלבד למאגר
    start_id = len(data.get("kanji", [])) + 1
    added_count = 0
    skipped_count = 0

    for kanji_char, level in n4_n5_kanji:
        if kanji_char in existing_kanji:
            skipped_count += 1
            continue

        data["kanji"].append({
            "id": f"n_kanji_{start_id + added_count}",
            "chapter": f"JLPT N{level}",
            "kanji": kanji_char,
            "onyomi": "-",
            "kunyomi": "-",
            "meaning": f"JLPT N{level} Kanji"
        })
        added_count += 1

    # 4. שמירת הקובץ המעודכן
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם בהצלחה!")
    print(f"נוספו {added_count} קאנג'י חדשים מרמות N4 ו-N5.")
    print(f"סוננו {skipped_count} קאנג'י שכבר היו קיימים במאגר.")

except Exception as e:
    print(f"שגיאה בתהליך הייבוא: {e}")