import json
import os

DATA_FILE = "data.json"

genki_17_salon_vocab = [
    # Hair Salon Vocabulary & Verbs
    {"word": "髪形", "reading": "かみがた", "meaning": "hairstyle"},
    {"word": "切る", "reading": "きる", "meaning": "to cut"},
    {"word": "そる", "reading": "そる", "meaning": "to shave"},
    {"word": "刈る", "reading": "かる", "meaning": "to crop"},
    {"word": "そめる", "reading": "そめる", "meaning": "to dye"},
    {"word": "そろえる", "reading": "そろえる", "meaning": "to make hair even; to trim"},
    {"word": "パーマをかける", "reading": "パーマをかける", "meaning": "to have one's hair permed"},
    {"word": "すく", "reading": "すく", "meaning": "to thin out (hair)"},
    {"word": "分け目", "reading": "わけめ", "meaning": "part (in hair)"},
    {"word": "前髪", "reading": "まえがみ", "meaning": "bangs; fringe"},
    {"word": "横", "reading": "よこ", "meaning": "side"},
    {"word": "後ろ", "reading": "うしろ", "meaning": "back"},

    # Salon Menu / Pricing
    {"word": "シャンプー", "reading": "シャンプー", "meaning": "shampoo"},
    {"word": "カット", "reading": "カット", "meaning": "cut"},
    {"word": "ブロー", "reading": "ブロー", "meaning": "blow-dry"},
    {"word": "パーマ", "reading": "パーマ", "meaning": "perm"},
    {"word": "カラー", "reading": "カラー", "meaning": "hair coloring"},
    {"word": "セット", "reading": "セット", "meaning": "set"},

    # Useful Expressions at the Hair Salon
    {"word": "カットをお願いします。", "reading": "カットをおねがいします。",
     "meaning": "I would like to have my hair cut."},
    {"word": "あまり短くしないでください。", "reading": "あまりみじかくしないでください。",
     "meaning": "Please don't make it too short."},
    {"word": "そわないでください。", "reading": "そわないでください。", "meaning": "Please don't shave me."},
    {"word": "３センチぐらい切ってください。", "reading": "３センチぐらいきってください。",
     "meaning": "Please cut off about 3 centimeters."},
    {"word": "後ろをそろえてください。", "reading": "うしろをそろえてください。",
     "meaning": "Please cut the back all the same length."},
    {"word": "赤にそめてください。", "reading": "あかにそめてください。", "meaning": "Please dye my hair red."},
    {"word": "ボブ・マーリーみたいな髪形にしたいんですが。",
     "reading": "ボブ・マーリーみたいなかみがたにしたいんですが。", "meaning": "I want my hair to be like Bob Marley's."}
]

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_vocab = data.get("vocab", [])
    existing_words = {item.get("word") for item in existing_vocab}
    existing_readings = {item.get("reading") for item in existing_vocab}

    start_id = len(existing_vocab) + 1
    added_count = 0
    skipped_count = 0

    for item in genki_17_salon_vocab:
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v17_salon_{start_id + added_count}",
            "chapter": 17,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים וביטויים חדשים מספרת פרק 17.")
    print(f"סוננו {skipped_count} כפילויות.")

except Exception as e:
    print(f"שגיאה: {e}")