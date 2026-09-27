import json
import os

DATA_FILE = "data.json"

# מילות הקאנג'י מפרק 14
genki_14_vocab = [
    {"word": "彼", "reading": "かれ", "meaning": "he; boyfriend"},
    {"word": "彼女", "reading": "かのじょ", "meaning": "she; girlfriend"},
    {"word": "彼ら", "reading": "かれら", "meaning": "they"},
    {"word": "彼氏", "reading": "かれし", "meaning": "boyfriend"},
    {"word": "時代", "reading": "じだい", "meaning": "age; era"},
    {"word": "電気代", "reading": "でんきだい", "meaning": "electricity fee"},
    {"word": "九十年代", "reading": "きゅうじゅうねんだい", "meaning": "90's"},
    {"word": "十代", "reading": "じゅうだい", "meaning": "in one's teens"},
    {"word": "代わりに", "reading": "かわりに", "meaning": "instead"},
    {"word": "留学生", "reading": "りゅうがくせい", "meaning": "international students"},
    {"word": "留学する", "reading": "りゅうがくする", "meaning": "to study abroad"},
    {"word": "留守", "reading": "るす", "meaning": "absence; not at home"},
    {"word": "家族", "reading": "かぞく", "meaning": "family"},
    {"word": "民族", "reading": "みんぞく", "meaning": "ethnic group"},
    {"word": "水族館", "reading": "すいぞくかん", "meaning": "aquarium"},
    {"word": "王族", "reading": "おうぞく", "meaning": "member of royalty"},
    {"word": "父親", "reading": "ちちおや", "meaning": "father"},
    {"word": "親切な", "reading": "しんせつな", "meaning": "kind"},
    {"word": "親友", "reading": "しんゆう", "meaning": "best friend"},
    {"word": "両親", "reading": "りょうしん", "meaning": "parents"},
    {"word": "親しい", "reading": "したしい", "meaning": "intimate"},
    {"word": "母親", "reading": "ははおや", "meaning": "mother"},
    {"word": "切る", "reading": "きる", "meaning": "to cut"},
    {"word": "切符", "reading": "きっぷ", "meaning": "ticket"},
    {"word": "切手", "reading": "きって", "meaning": "postage stamp"},
    {"word": "大切な", "reading": "たいせつな", "meaning": "precious"},
    {"word": "英語", "reading": "えいご", "meaning": "English language"},
    {"word": "英国", "reading": "えいこく", "meaning": "United Kingdom"},
    {"word": "英会話", "reading": "えいかいわ", "meaning": "English conversation"},
    {"word": "英雄", "reading": "えいゆう", "meaning": "hero"},
    {"word": "店", "reading": "みせ", "meaning": "shop"},
    {"word": "店員", "reading": "てんいん", "meaning": "store clerk"},
    {"word": "売店", "reading": "ばいてん", "meaning": "stall; kiosk"},
    {"word": "書店", "reading": "しょてん", "meaning": "bookstore"},
    {"word": "店長", "reading": "てんちょう", "meaning": "store manager"},
    {"word": "去年", "reading": "きょねん", "meaning": "last year"},
    {"word": "過去", "reading": "かこ", "meaning": "the past"},
    {"word": "去る", "reading": "さる", "meaning": "to leave"},
    {"word": "消去する", "reading": "しょうきょする", "meaning": "to erase"},
    {"word": "急に", "reading": "きゅうに", "meaning": "suddenly"},
    {"word": "急ぐ", "reading": "いそぐ", "meaning": "to hurry"},
    {"word": "急行", "reading": "きゅうこう", "meaning": "express train"},
    {"word": "特急", "reading": "とっきゅう", "meaning": "super express"},
    {"word": "乗る", "reading": "のる", "meaning": "to ride"},
    {"word": "乗り物", "reading": "のりもの", "meaning": "vehicle"},
    {"word": "乗車", "reading": "じょうしゃ", "meaning": "riding a car"},
    {"word": "乗馬", "reading": "じょうば", "meaning": "horseback riding"},
    {"word": "本当に", "reading": "ほんとうに", "meaning": "really"},
    {"word": "お弁当", "reading": "おべんとう", "meaning": "boxed lunch"},
    {"word": "当時", "reading": "とうじ", "meaning": "at that time"},
    {"word": "当たる", "reading": "あたる", "meaning": "to hit"},
    {"word": "音楽", "reading": "おんがく", "meaning": "music"},
    {"word": "発音", "reading": "はつおん", "meaning": "pronunciation"},
    {"word": "音", "reading": "おと", "meaning": "sound"},
    {"word": "本音", "reading": "ほんね", "meaning": "real intention"},
    {"word": "楽しい", "reading": "たのしい", "meaning": "fun"},
    {"word": "楽器", "reading": "がっき", "meaning": "musical instrument"},
    {"word": "楽な", "reading": "らくな", "meaning": "easy; comfortable"},
    {"word": "医者", "reading": "いしゃ", "meaning": "doctor"},
    {"word": "歯医者", "reading": "はいしゃ", "meaning": "dentist"},
    {"word": "医学", "reading": "いがく", "meaning": "medical science"},
    {"word": "医院", "reading": "いいん", "meaning": "clinic"},
    {"word": "学者", "reading": "がくしゃ", "meaning": "scholar"},
    {"word": "読者", "reading": "どくしゃ", "meaning": "reader"},
    {"word": "若者", "reading": "わかもの", "meaning": "young people"},
    {"word": "忍者", "reading": "にんじゃ", "meaning": "ninja"}
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

    for item in genki_14_vocab:
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v14_{start_id + added_count}",
            "chapter": 14,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים חדשות מפרק 14.")
    print(f"סוננו {skipped_count} מילים שכבר הופיעו במאגרי N4/N5.")

except Exception as e:
    print(f"שגיאה: {e}")