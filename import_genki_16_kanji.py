import json
import os

DATA_FILE = "data.json"

genki_16_kanji_vocab = [
    {"word": "子供", "reading": "こども", "meaning": "child"},
    {"word": "供える", "reading": "そなえる", "meaning": "to offer something to a spirit"},
    {"word": "提供", "reading": "ていきょう", "meaning": "offer"},
    {"word": "世界", "reading": "せかい", "meaning": "the world"},
    {"word": "世話", "reading": "せわ", "meaning": "care"},
    {"word": "世代", "reading": "せだい", "meaning": "generation"},
    {"word": "三世", "reading": "さんせい", "meaning": "the third generation"},
    {"word": "世の中", "reading": "よのなか", "meaning": "society"},
    {"word": "視界", "reading": "しかい", "meaning": "visibility"},
    {"word": "政界", "reading": "せいかい", "meaning": "political world"},
    {"word": "限界", "reading": "げんかい", "meaning": "limit"},
    {"word": "全部", "reading": "ぜんぶ", "meaning": "all"},
    {"word": "安全", "reading": "あんぜん", "meaning": "safety"},
    {"word": "全国", "reading": "ぜんこく", "meaning": "whole country"},
    {"word": "全く", "reading": "まったく", "meaning": "entirely"},
    {"word": "全て", "reading": "すべて", "meaning": "all"},
    {"word": "部屋", "reading": "へや", "meaning": "room"},
    {"word": "テニス部", "reading": "テニスぶ", "meaning": "tennis club"},
    {"word": "部長", "reading": "ぶちょう", "meaning": "department manager"},
    {"word": "始まる", "reading": "はじまる", "meaning": "something begins"},
    {"word": "始まる", "reading": "はじめる", "meaning": "to begin something"},
    {"word": "始発", "reading": "しはつ", "meaning": "first train of the day"},
    {"word": "開始", "reading": "かいし", "meaning": "start"},
    {"word": "毎週", "reading": "まいしゅう", "meaning": "every week"},
    {"word": "先週", "reading": "せんしゅう", "meaning": "last week"},
    {"word": "一週間", "reading": "いっしゅうかん", "meaning": "one week"},
    {"word": "週末", "reading": "しゅうまつ", "meaning": "weekend"},
    {"word": "二週目", "reading": "にしゅうめ", "meaning": "second week"},
    {"word": "考える", "reading": "かんがえる", "meaning": "to think"},
    {"word": "考え", "reading": "かんがえ", "meaning": "idea"},
    {"word": "考古学", "reading": "こうこがく", "meaning": "archaeology"},
    {"word": "参考", "reading": "さんこう", "meaning": "reference"},
    {"word": "開ける", "reading": "あける", "meaning": "to open something"},
    {"word": "開く", "reading": "あく", "meaning": "something opens"},
    {"word": "開く", "reading": "ひらく", "meaning": "to open"},
    {"word": "開店", "reading": "かいてん", "meaning": "opening of a store"},
    {"word": "本屋", "reading": "ほんや", "meaning": "bookstore"},
    {"word": "魚屋", "reading": "さかなや", "meaning": "fish shop"},
    {"word": "屋上", "reading": "おくじょう", "meaning": "rooftop"},
    {"word": "屋内", "reading": "おくない", "meaning": "indoor"},
    {"word": "味方", "reading": "みかた", "meaning": "ally; person on one's side"},
    {"word": "読み方", "reading": "よみかた", "meaning": "way of reading"},
    {"word": "夕方", "reading": "ゆうがた", "meaning": "evening"},
    {"word": "両方", "reading": "りょうほう", "meaning": "both"},
    {"word": "方法", "reading": "ほうほう", "meaning": "method"},
    {"word": "運動", "reading": "うんどう", "meaning": "exercise"},
    {"word": "運転", "reading": "うんてん", "meaning": "driving"},
    {"word": "運がいい", "reading": "うんがいい", "meaning": "lucky"},
    {"word": "運命", "reading": "うんめい", "meaning": "fate"},
    {"word": "運ぶ", "reading": "はこぶ", "meaning": "to carry"},
    {"word": "動く", "reading": "うごく", "meaning": "to move"},
    {"word": "自動車", "reading": "じどうしゃ", "meaning": "automobile"},
    {"word": "動物", "reading": "どうぶつ", "meaning": "animal"},
    {"word": "動詞", "reading": "どうし", "meaning": "verb"},
    {"word": "教える", "reading": "おしえる", "meaning": "to teach"},
    {"word": "教室", "reading": "きょうしつ", "meaning": "classroom"},
    {"word": "教会", "reading": "きょうかい", "meaning": "church"},
    {"word": "キリスト教", "reading": "キリストきょう", "meaning": "Christianity"},
    {"word": "教科書", "reading": "きょうかしょ", "meaning": "textbook"},
    {"word": "研究室", "reading": "けんきゅうしつ", "meaning": "professor's office"},
    {"word": "地下室", "reading": "ちかしつ", "meaning": "basement"},
    {"word": "待合室", "reading": "まちあいしつ", "meaning": "waiting room"},
    {"word": "以外", "reading": "いがい", "meaning": "other than"},
    {"word": "以上", "reading": "いじょう", "meaning": "or more"},
    {"word": "以下", "reading": "いか", "meaning": "or less"},
    {"word": "以内", "reading": "いない", "meaning": "within"},
    {"word": "以前", "reading": "いぜん", "meaning": "before; formerly"}
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

    for item in genki_16_kanji_vocab:
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v16_kanji_{start_id + added_count}",
            "chapter": 16,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים חדשות מקאנג'י פרק 16.")
    print(f"סוננו {skipped_count} כפילויות.")

except Exception as e:
    print(f"שגיאה: {e}")