import json
import os

DATA_FILE = "data.json"

genki_15_kanji_vocab = [
    {"word": "死ぬ", "reading": "しぬ", "meaning": "to die"},
    {"word": "死", "reading": "し", "meaning": "death"},
    {"word": "必死", "reading": "ひっし", "meaning": "desperate"},
    {"word": "死者", "reading": "ししゃ", "meaning": "the dead"},
    {"word": "意味", "reading": "いみ", "meaning": "meaning"},
    {"word": "注意する", "reading": "ちゅういする", "meaning": "to watch out"},
    {"word": "意見", "reading": "いけん", "meaning": "opinion"},
    {"word": "用意する", "reading": "よういする", "meaning": "to prepare"},
    {"word": "趣味", "reading": "しゅみ", "meaning": "hobby"},
    {"word": "興味", "reading": "きょうみ", "meaning": "interest"},
    {"word": "味噌", "reading": "みそ", "meaning": "soybean paste"},
    {"word": "味", "reading": "あじ", "meaning": "taste"},
    {"word": "注文する", "reading": "ちゅうもんする", "meaning": "to order"},
    {"word": "注ぐ", "reading": "そそぐ", "meaning": "to pour"},
    {"word": "夏", "reading": "なつ", "meaning": "summer"},
    {"word": "夏休み", "reading": "なつやすみ", "meaning": "summer vacation"},
    {"word": "初夏", "reading": "しょか", "meaning": "early summer"},
    {"word": "魚", "reading": "さかな", "meaning": "fish"},
    {"word": "魚屋", "reading": "さかなや", "meaning": "fish shop"},
    {"word": "金魚", "reading": "きんぎょ", "meaning": "goldfish"},
    {"word": "人魚", "reading": "にんぎょ", "meaning": "mermaid"},
    {"word": "魚市場", "reading": "うおいちば", "meaning": "fish market"},
    {"word": "お寺", "reading": "おてら", "meaning": "temple"},
    {"word": "東寺", "reading": "とうじ", "meaning": "Toji (the name of a temple)"},
    {"word": "寺院", "reading": "じいん", "meaning": "sacred building"},
    {"word": "禅寺", "reading": "ぜんでら", "meaning": "Zen temple"},
    {"word": "広い", "reading": "ひろい", "meaning": "wide; spacious"},
    {"word": "広場", "reading": "ひろば", "meaning": "square; open space"},
    {"word": "広島", "reading": "ひろしま", "meaning": "Hiroshima"},
    {"word": "広告", "reading": "こうこく", "meaning": "advertisement"},
    {"word": "足", "reading": "あし", "meaning": "foot; leg"},
    {"word": "足りる", "reading": "たりる", "meaning": "to be sufficient"},
    {"word": "一足", "reading": "いっそく", "meaning": "one pair of shoes"},
    {"word": "水不足", "reading": "みずぶそく", "meaning": "lack of water"},
    {"word": "自転車", "reading": "じてんしゃ", "meaning": "bicycle"},
    {"word": "運転する", "reading": "うんてんする", "meaning": "to drive"},
    {"word": "回転ずし", "reading": "かいてんずし", "meaning": "conveyor belt sushi"},
    {"word": "転ぶ", "reading": "ころぶ", "meaning": "to tumble; to fall down"},
    {"word": "借りる", "reading": "かりる", "meaning": "to borrow"},
    {"word": "借地", "reading": "しゃくち", "meaning": "rented land"},
    {"word": "借金", "reading": "しゃっきん", "meaning": "debt"},
    {"word": "借家", "reading": "しゃくや", "meaning": "rented house"},
    {"word": "走る", "reading": "はしる", "meaning": "to run"},
    {"word": "走り書き", "reading": "はしりがき", "meaning": "hasty writing"},
    {"word": "脱走", "reading": "だっそう", "meaning": "escape from a prison"},
    {"word": "場所", "reading": "ばしょ", "meaning": "place"},
    {"word": "工場", "reading": "こうじょう", "meaning": "factory"},
    {"word": "市場", "reading": "いちば", "meaning": "market"},
    {"word": "場合", "rief": "ばあい", "meaning": "case"},
    {"word": "駐車場", "reading": "ちゅうしゃじょう", "meaning": "parking lot"},
    {"word": "建物", "reading": "たてもの", "meaning": "building"},
    {"word": "建てる", "reading": "たてる", "meaning": "to build"},
    {"word": "建つ", "reading": "たつ", "meaning": "to be built"},
    {"word": "建国", "reading": "けんこく", "meaning": "founding a nation"},
    {"word": "地下", "reading": "ちか", "meaning": "underground"},
    {"word": "地下鉄", "reading": "ちかてつ", "meaning": "subway"},
    {"word": "地図", "reading": "ちず", "meaning": "map"},
    {"word": "地球", "reading": "ちきゅう", "meaning": "the earth"},
    {"word": "地震", "reading": "じしん", "meaning": "earthquake"},
    {"word": "通る", "reading": "とおる", "meaning": "to go through; to pass"},
    {"word": "通う", "reading": "かよう", "meaning": "to commute"},
    {"word": "通学", "reading": "つうがく", "meaning": "going to school"},
    {"word": "通勤", "reading": "つうきん", "meaning": "going to work"}
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

    for item in genki_15_kanji_vocab:
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v15_kanji_{start_id + added_count}",
            "chapter": 15,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים חדשות מקאנג'י פרק 15.")
    print(f"סוננו {skipped_count} כפילויות.")

except Exception as e:
    print(f"שגיאה: {e}")