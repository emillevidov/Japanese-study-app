import json
import os

DATA_FILE = "data.json"

genki_16_vocab = [
    # Nouns
    {"word": "駅員さん", "reading": "えきいんさん", "meaning": "station attendant"},
    {"word": "親", "reading": "おや", "meaning": "parent"},
    {"word": "親せき", "reading": "しんせき", "meaning": "relatives"},
    {"word": "ごみ", "reading": "ごみ", "meaning": "garbage"},
    {"word": "砂糖", "reading": "さとう", "meaning": "sugar"},
    {"word": "ファイル", "reading": "ファイル", "meaning": "(file) folder; portfolio; file"},
    {"word": "大きさ", "reading": "おおきさ", "meaning": "size"},
    {"word": "道", "reading": "みち", "meaning": "way; road; directions"},
    {"word": "期末試験", "reading": "きまつしけん", "meaning": "final examination"},
    {"word": "研究", "reading": "けんきゅう", "meaning": "research"},
    {"word": "大学院", "reading": "だいがくいん", "meaning": "graduate school"},
    {"word": "奨学金", "reading": "しょうがくきん", "meaning": "scholarship"},
    {"word": "推薦状", "reading": "すいせんじょう", "meaning": "letter of recommendation"},
    {"word": "台風", "reading": "たいふう", "meaning": "typhoon"},
    {"word": "文化", "reading": "ぶんか", "meaning": "culture"},
    {"word": "返事", "reading": "へんじ", "meaning": "reply"},
    {"word": "日", "reading": "ひ", "meaning": "day"},

    # i-adjectives
    {"word": "汚い", "reading": "きたない", "meaning": "dirty"},

    # U-verbs
    {"word": "起こす", "reading": "おこす", "meaning": "to wake (someone) up (〜を)"},
    {"word": "おごる", "reading": "おごる", "meaning": "to treat (someone) to a meal (person に meal を)"},
    {"word": "笑う", "reading": "わらう", "meaning": "to laugh"},
    {"word": "落ち込む", "reading": "おちこむ", "meaning": "to get depressed"},
    {"word": "困る", "reading": "こまる", "meaning": "to have difficulty"},
    {"word": "出す", "reading": "だす", "meaning": "to take (something) out; to hand in (something) (〜を)"},
    {"word": "直す", "reading": "なおす", "meaning": "to correct; to fix (〜を)"},
    {"word": "見つかる", "reading": "みつかる", "meaning": "to be found (〜が)"},
    {"word": "訳す", "reading": "やくす", "meaning": "to translate (source を target に)"},
    {"word": "貸す", "reading": "かす", "meaning": "to lend (person に thing を)"},
    {"word": "連れていく", "reading": "つれていく", "meaning": "to take (someone) to (a place) (person を place に)"},
    {"word": "道に迷う", "reading": "みちにまよう", "meaning": "to become lost; to lose one's way"},
    {"word": "迎えに行く", "reading": "むかえにいく", "meaning": "to go to pick up (place まで/に person を)"},

    # Ru-verbs
    {"word": "集める", "reading": "あつめる", "meaning": "to collect (〜を)"},
    {"word": "入れる", "reading": "いれる", "meaning": "to put (something) in (thing を place に)"},
    {"word": "見せる", "reading": "みせる", "meaning": "to show (person に thing を)"},
    {"word": "乗り遅れる", "reading": "のりおくれる", "meaning": "to miss (a train, bus, etc.) (〜に)"},
    {"word": "アイロンをかける", "reading": "アイロンをかける", "meaning": "to iron (clothes) (〜に)"},

    # Irregular Verbs
    {"word": "朝寝坊する", "reading": "あさねぼうする", "meaning": "to oversleep"},
    {"word": "案内する", "reading": "あんないする", "meaning": "to show (someone) around (place を)"},
    {"word": "説明する", "reading": "せつめいする", "meaning": "to explain"},
    {"word": "迎えに来る", "reading": "むかえにくる", "meaning": "to come to pick up (place まで/に person を)"},

    # Adverbs and Other Expressions
    {"word": "今日中に", "reading": "きょうじゅうに", "meaning": "by the end of today"},
    {"word": "授業中に", "reading": "じゅぎょうちゅうに", "meaning": "in class; during the class"},
    {"word": "この間", "reading": "このあいだ", "meaning": "the other day"},
    {"word": "これから", "reading": "これから", "meaning": "from now on"},
    {"word": "このぐらい", "reading": "このぐらい",
     "meaning": "about this much (= これぐらい / このくらい / これくらい)"},
    {"word": "自分で", "reading": "じぶんで", "meaning": "do something by oneself"},
    {"word": "他の", "reading": "ほかの", "meaning": "other"},
    {"word": "ええと", "reading": "ええと", "meaning": "well...; let me see..."},
    {"word": "実は", "reading": "じつは", "meaning": "actually; in fact"},
    {"word": "〜以外", "reading": "〜いがい", "meaning": "other than..."},
    {"word": "ごめん", "reading": "ごめん", "meaning": "I'm sorry. (casual)"},
    {"word": "失礼します", "reading": "しつれいします", "meaning": "Excuse me.; Sorry to interrupt you."}
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

    for item in genki_16_vocab:
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v16_main_{start_id + added_count}",
            "chapter": 16,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים חדשות מפרק 16.")
    print(f"סוננו {skipped_count} כפילויות.")

except Exception as e:
    print(f"שגיאה: {e}")