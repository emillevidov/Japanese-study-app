import json
import os

DATA_FILE = "data.json"

genki_17_kanji_vocab = [
    {"word": "分野", "reading": "ぶんや", "meaning": "realm; field"},
    {"word": "長野", "reading": "ながの", "meaning": "Nagano"},
    {"word": "野球", "reading": "やきゅう", "meaning": "baseball"},
    {"word": "小野さん", "reading": "おのさん", "meaning": "Mr./Ms. Ono"},
    {"word": "野菜", "reading": "やさい", "meaning": "vegetable"},
    {"word": "習う", "reading": "ならう", "meaning": "to learn"},
    {"word": "習字", "reading": "しゅうじ", "meaning": "calligraphy"},
    {"word": "練習", "reading": "れんしゅう", "meaning": "practice"},
    {"word": "習慣", "reading": "しゅうかん", "meaning": "habit; custom"},
    {"word": "主に", "reading": "おもに", "meaning": "mainly"},
    {"word": "主婦", "reading": "しゅふ", "meaning": "housewife"},
    {"word": "主語", "reading": "しゅご", "meaning": "subject of a sentence"},
    {"word": "持ち主", "reading": "もちぬし", "meaning": "owner"},
    {"word": "二十五歳", "reading": "にじゅうごさい", "meaning": "twenty-five years old"},
    {"word": "お歳暮", "reading": "おせいぼ", "meaning": "year-end gift"},
    {"word": "二十歳", "reading": "はたち", "meaning": "twenty years old"},
    {"word": "集める", "reading": "あつめる", "meaning": "to collect"},
    {"word": "特集", "reading": "とくしゅう", "meaning": "magazine feature"},
    {"word": "集中する", "reading": "しゅうちゅうする", "meaning": "to concentrate"},
    {"word": "発表する", "reading": "はっぴょうする", "meaning": "to make public; to give a presentation"},
    {"word": "発音", "reading": "はつおん", "meaning": "pronunciation"},
    {"word": "出発", "reading": "しゅっぱつ", "meaning": "departure"},
    {"word": "発明", "reading": "はつめい", "meaning": "invention"},
    {"word": "表紙", "reading": "ひょうし", "meaning": "cover page"},
    {"word": "表現", "reading": "ひょうげん", "meaning": "expression"},
    {"word": "表す", "reading": "あらわす", "meaning": "to express"},
    {"word": "表", "reading": "おもて", "meaning": "the front"},
    {"word": "作品", "reading": "さくひん", "meaning": "work (of art, etc.)"},
    {"word": "上品な", "reading": "じょうひんな", "meaning": "elegant"},
    {"word": "手品", "reading": "てじな", "meaning": "magic"},
    {"word": "品物", "reading": "しなもの", "meaning": "article of merchandise"},
    {"word": "写真", "reading": "しゃしん", "meaning": "photograph"},
    {"word": "写す", "reading": "うつす", "meaning": "to copy"},
    {"word": "写生", "reading": "しゃせい", "meaning": "sketch"},
    {"word": "描写する", "reading": "びょうしゃする", "meaning": "to describe"},
    {"word": "真ん中", "reading": "まんなか", "meaning": "center"},
    {"word": "の真上", "reading": "のまうえ", "meaning": "right above"},
    {"word": "真夜中", "reading": "まよなか", "meaning": "midnight"},
    {"word": "文字", "reading": "もじ", "meaning": "letter; character"},
    {"word": "名字", "reading": "みょうじ", "meaning": "family name"},
    {"word": "大文字", "reading": "おおもじ", "meaning": "uppercase letters"},
    {"word": "赤字", "reading": "あかじ", "meaning": "deficit"},
    {"word": "漢字", "reading": "かんじ", "meaning": "Chinese character"},
    {"word": "活動", "reading": "かつどう", "meaning": "activity"},
    {"word": "生活", "reading": "せいかつ", "meaning": "life; living"},
    {"word": "活発な", "reading": "かっぱつな", "meaning": "active"},
    {"word": "活用", "reading": "かつよう", "meaning": "conjugation"},
    {"word": "活気", "reading": "かっき", "meaning": "liveliness"},
    {"word": "結婚する", "reading": "けっこんする", "meaning": "to get married"},
    {"word": "結果", "reading": "けっか", "meaning": "result"},
    {"word": "結論", "reading": "けつろん", "meaning": "conclusion"},
    {"word": "結ぶ", "reading": "むすぶ", "meaning": "to tie a knot"},
    {"word": "離婚する", "reading": "りこんする", "meaning": "divorce"},
    {"word": "婚約者", "reading": "こんやくしゃ", "meaning": "fiancé(e)"},
    {"word": "新婚", "reading": "しんこん", "meaning": "1newlywed"},
    {"word": "未婚", "reading": "みこん", "meaning": "unmarried"},
    {"word": "歩く", "reading": "あるく", "meaning": "to walk"},
    {"word": "歩道", "reading": "ほどう", "meaning": "sidewalk"},
    {"word": "散歩する", "reading": "さんぽする", "meaning": "to stroll"},
    {"word": "一歩", "reading": "いっぽ", "meaning": "one step"},
    {"word": "進歩", "reading": "しんぽ", "meaning": "progress"}
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

    for item in genki_17_kanji_vocab:
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v17_kanji_{start_id + added_count}",
            "chapter": 17,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים חדשות מקאנג'י פרק 17.")
    print(f"סוננו {skipped_count} כפילויות.")

except Exception as e:
    print(f"שגיאה: {e}")