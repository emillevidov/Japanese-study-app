import json
import os

DATA_FILE = "data.json"

genki_17_vocab = [
    # Nouns
    {"word": "赤ちゃん", "reading": "あかちゃん", "meaning": "baby"},
    {"word": "お客さん", "reading": "おきゃくさん", "meaning": "guest; visitor; client; customer"},
    {"word": "首相", "reading": "しゅしょう", "meaning": "prime minister"},
    {"word": "サラリーマン", "reading": "サラリーマン", "meaning": "salaryman; office worker"},
    {"word": "給料", "reading": "きゅうりょう", "meaning": "salary"},
    {"word": "残業", "reading": "ざんぎょう", "meaning": "overtime work"},
    {"word": "パンダ", "reading": "パンダ", "meaning": "panda"},
    {"word": "コンタクトレンズ", "reading": "コンタクトレンズ", "meaning": "contact lenses"},
    {"word": "ひげ", "reading": "ひげ", "meaning": "beard"},
    {"word": "ブーツ", "reading": "ブーツ", "meaning": "boots"},
    {"word": "鍵", "reading": "かぎ", "meaning": "lock; key"},
    {"word": "宝くじ", "reading": "たからくじ", "meaning": "lottery"},
    {"word": "紙", "reading": "かみ", "meaning": "paper"},
    {"word": "スプーン", "reading": "スプーン", "meaning": "spoon"},
    {"word": "お湯", "reading": "おゆ", "meaning": "hot water"},
    {"word": "電子レンジ", "reading": "でんしレンジ", "meaning": "microwave oven"},
    {"word": "ヒーター", "reading": "ヒーター", "meaning": "heater"},
    {"word": "ニュース", "reading": "ニュース", "meaning": "news"},
    {"word": "火事", "reading": "かじ", "meaning": "fire"},
    {"word": "旅行会社", "reading": "りょこうがいしゃ", "meaning": "travel agency"},
    {"word": "ショッピングモール", "reading": "ショッピングモール", "meaning": "shopping mall"},
    {"word": "寮", "reading": "りょう", "meaning": "dormitory"},
    {"word": "違い", "reading": "ちがい", "meaning": "difference"},
    {"word": "秘密", "reading": "ひみつ", "meaning": "secret"},
    {"word": "準備", "reading": "じゅんび", "meaning": "preparation"},
    {"word": "自分", "reading": "じぶん", "meaning": "oneself"},

    # i-adjectives
    {"word": "危ない", "reading": "あぶない", "meaning": "dangerous"},
    {"word": "うらやましくない", "reading": "うらましい", "meaning": "envious"},  # נשמור את הבסיס
    {"word": "少ない", "reading": "すくない", "meaning": "a little; a few"},
    {"word": "都合が悪い", "reading": "つごうがわるい", "meaning": "inconvenient; to have a scheduling conflict"},
    {"word": "強い", "reading": "つよい", "meaning": "strong"},

    # na-adjectives
    {"word": "最悪な", "reading": "さいあくな", "meaning": "the worst"},

    # U-verbs
    {"word": "選ぶ", "reading": "えらぶ", "meaning": "to choose; to select (〜を)"},
    {"word": "お湯を沸かす", "reading": "おゆをわかす", "meaning": "to boil water"},
    {"word": "髪をとかす", "reading": "かみをとかす", "meaning": "to comb one's hair"},
    {"word": "ひげをそる", "reading": "ひげをそる", "meaning": "to shave one's beard"},
    {"word": "脱ぐ", "reading": "ぬぐ", "meaning": "to take off (clothes) (〜を)"},
    {"word": "混む", "reading": "こむ", "meaning": "to get crowded (〜が)"},
    {"word": "宝くじに当たる", "reading": "たからくじにあたる", "meaning": "to win a lottery"},

    # Ru-verbs
    {"word": "入れる", "reading": "いれる", "meaning": "to make tea, coffee, etc. (〜を)"},
    {"word": "生まれる", "reading": "うまれる", "meaning": "to be born (〜が)"},
    {"word": "鍵をかける", "reading": "かぎをかける", "meaning": "to lock (〜に)"},
    {"word": "足りる", "reading": "たりる", "meaning": "to be sufficient; to be enough (〜が)"},
    {"word": "慣れる", "reading": "なれる", "meaning": "to get used to... (〜に)"},

    # Irregular Verbs
    {"word": "お祈りする", "reading": "おいのりする", "meaning": "to pray (〜に)"},
    {"word": "化粧する", "reading": "けしょうする", "meaning": "to put makeup on"},
    {"word": "就職する", "reading": "しゅうしょくする", "meaning": "to get a full-time job (at...) (company に)"},
    {"word": "離婚する", "reading": "りこんする", "meaning": "to get a divorce (person と)"},
    {"word": "する", "reading": "する", "meaning": "to wear small items (necktie, watch, etc.) (〜を)"},

    # Adverbs and Other Expressions
    {"word": "ずいぶん", "reading": "ずいぶん", "meaning": "very"},
    {"word": "例えば", "reading": "たとえば", "meaning": "for example"},
    {"word": "〜に比べて", "reading": "〜にくらべて", "meaning": "compared with..."},
    {"word": "〜によると", "reading": "〜によると", "meaning": "according to..."},
    {"word": "前", "reading": "まえ", "meaning": "before..."},
    {"word": "やっぱり", "reading": "やっぱり", "meaning": "after all"},
    {"word": "〜かな", "reading": "〜かな", "meaning": "I wonder... (casual)"},
    {"word": "そうか", "reading": "そうか", "meaning": "I see. (casual)"},
    {"word": "おめでとうございます", "reading": "おめでとうございます", "meaning": "Congratulations!"}
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

    for item in genki_17_vocab:
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v17_main_{start_id + added_count}",
            "chapter": 17,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים חדשות מפרק 17.")
    print(f"סוננו {skipped_count} כפילויות.")

except Exception as e:
    print(f"שגיאה: {e}")