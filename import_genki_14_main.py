import json
import os

DATA_FILE = "data.json"

genki_14_main_vocab = [
    # Nouns
    {"word": "奥さん", "reading": "おくさん", "meaning": "(your/someone's) wife"},
    {"word": "ご主人", "reading": "ごしゅじん", "meaning": "(your/someone's) husband"},
    {"word": "パートナー", "reading": "パートナー", "meaning": "partner"},
    {"word": "おじさん", "reading": "おじさん", "meaning": "uncle; middle-aged man"},
    {"word": "おばさん", "reading": "おばさん", "meaning": "aunt; middle-aged woman"},
    {"word": "両親", "reading": "りょうしん", "meaning": "parents"},
    {"word": "大家さん", "reading": "おおやさん", "meaning": "landlord; landlady"},
    {"word": "皆さん", "reading": "みなさん", "meaning": "everyone; all of you"},
    {"word": "チョコレート", "reading": "チョコレート", "meaning": "chocolate"},
    {"word": "みかん", "reading": "みかん", "meaning": "mandarin orange"},
    {"word": "トレーナー", "reading": "トレーナー", "meaning": "sweatshirt"},
    {"word": "シャツ", "reading": "シャツ", "meaning": "shirt"},
    {"word": "ネクタイ", "reading": "ネクタイ", "meaning": "necktie"},
    {"word": "マフラー", "reading": "マフラー", "meaning": "winter scarf"},
    {"word": "指輪", "reading": "ゆびわ", "meaning": "ring"},
    {"word": "鉛筆", "reading": "えんぴつ", "meaning": "pencil"},
    {"word": "ぬいぐるみ", "reading": "ぬいぐるみ", "meaning": "stuffed animal (e.g., teddy bear)"},
    {"word": "漫画", "reading": "まんが", "meaning": "comic book"},
    {"word": "化粧品", "reading": "けしょうひん", "meaning": "cosmetics"},
    {"word": "ラジオ", "reading": "ラジオ", "meaning": "radio"},
    {"word": "お皿", "reading": "おさら", "meaning": "plate; dish"},
    {"word": "お返し", "reading": "おかえし", "meaning": "return (as a token of gratitude)"},
    {"word": "履歴書", "reading": "りれきしょ", "meaning": "resume"},
    {"word": "クリスマス", "reading": "クリスマス", "meaning": "Christmas"},
    {"word": "バレンタインデー", "reading": "バレンタインデー", "meaning": "Valentine's Day"},
    {"word": "ホワイトデー", "reading": "ホワイトデー", "meaning": "White Day (yet another gift-giving day)"},

    # Adjectives
    {"word": "欲しい", "reading": "ほしい", "meaning": "to want"},
    {"word": "おしゃれな", "reading": "おしゃれな", "meaning": "fashionable; stylish"},
    {"word": "けちな", "reading": "けちな", "meaning": "stingy; cheap"},

    # Verbs
    {"word": "送る", "reading": "おくる", "meaning": "to send"},
    {"word": "似合う", "reading": "にあう", "meaning": "to look good (on somebody)"},
    {"word": "あきらめる", "reading": "あきらめる", "meaning": "to give up"},
    {"word": "あげる", "reading": "あげる", "meaning": "to give (to others)"},
    {"word": "くれる", "reading": "くれる", "meaning": "to give (me)"},
    {"word": "できる", "reading": "できる", "meaning": "to come into existence; to be made"},
    {"word": "相談する", "reading": "そうだんする", "meaning": "to consult"},
    {"word": "注意する", "reading": "ちゅういする", "meaning": "to give warning; to watch out"},
    {"word": "プロポーズする", "reading": "プロポーズする", "meaning": "to propose marriage"},

    # Adverbs, Expressions, and Counters
    {"word": "〜君", "reading": "〜くん", "meaning": "Mr./Ms... (casual)"},
    {"word": "〜たち", "reading": "〜たち", "meaning": "[makes a noun plural]"},
    {"word": "私たち", "reading": "わたしたち", "meaning": "we"},
    {"word": "こんな〜", "reading": "こんな〜", "meaning": "... like this; this kind of..."},
    {"word": "急に", "reading": "きゅうに", "meaning": "suddenly"},
    {"word": "ちょうど", "reading": "ちょうど", "meaning": "exactly"},
    {"word": "よく", "reading": "よく", "meaning": "well"},
    {"word": "さあ", "reading": "さあ", "meaning": "I am not sure..."},
    {"word": "どうしたらいい", "reading": "どうしたらいい", "meaning": "what should one do"},
    {"word": "〜個", "reading": "〜こ", "meaning": "[generic counter for smaller items]"},
    {"word": "〜冊", "reading": "〜さつ", "meaning": "[counter for bound volumes]"},
    {"word": "〜台", "reading": "〜だい", "meaning": "[counter for equipment]"},
    {"word": "〜匹", "reading": "〜ひき", "meaning": "[counter for smaller animals]"},
    {"word": "〜本", "reading": "〜ほん", "meaning": "[counter for long objects]"}
]

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_vocab = data.get("vocab", [])
    # יצירת רשימות למניעת כפילויות
    existing_words = {item.get("word") for item in existing_vocab}
    existing_readings = {item.get("reading") for item in existing_vocab}

    start_id = len(existing_vocab) + 1
    added_count = 0
    skipped_count = 0

    for item in genki_14_main_vocab:
        # דילוג על מילים שכבר קיימות ב-N4/N5 או בקאנג'י של פרק 14
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v14_main_{start_id + added_count}",
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
    print(f"סוננו {skipped_count} מילים שכבר הופיעו במאגר (מגיטהאב או מרשימת הקאנג'י).")

except Exception as e:
    print(f"שגיאה: {e}")