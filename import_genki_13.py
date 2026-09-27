import json
import os

DATA_FILE = "data.json"

# רשימת כל אוצר המילים מפרק 13 - כולל המילים מעמודי הקאנג'י
genki_13_vocab = [
    # אוצר מילים רגיל
    {"word": "大人", "reading": "おとな", "meaning": "adult"},
    {"word": "弁護士", "reading": "べんごし", "meaning": "lawyer"},
    {"word": "私", "reading": "わたくし", "meaning": "I (formal)"},
    {"word": "カレー", "reading": "カレー", "meaning": "curry"},
    {"word": "紅茶", "reading": "こうちゃ", "meaning": "black tea"},
    {"word": "着物", "reading": "きもの", "meaning": "kimono; Japanese traditional dress"},
    {"word": "セーター", "reading": "セーター", "meaning": "sweater"},
    {"word": "楽器", "reading": "がっき", "meaning": "musical instrument"},
    {"word": "空手", "reading": "からて", "meaning": "karate"},
    {"word": "ゴルフ", "reading": "ゴルフ", "meaning": "golf"},
    {"word": "バイク", "reading": "バイク", "meaning": "motorcycle"},
    {"word": "象", "reading": "ぞう", "meaning": "elephant"},
    {"word": "体", "reading": "からだ", "meaning": "body"},
    {"word": "外国語", "reading": "がいこくご", "meaning": "foreign language"},
    {"word": "言葉", "reading": "ことば", "meaning": "language"},
    {"word": "文法", "reading": "ぶんぽう", "meaning": "grammar"},
    {"word": "アプリ", "reading": "アプリ", "meaning": "application"},
    {"word": "アパート", "reading": "アパート", "meaning": "apartment"},
    {"word": "マンション", "reading": "マンション", "meaning": "larger apartment building; condominium"},
    {"word": "空港", "reading": "くうこう", "meaning": "airport"},
    {"word": "店", "reading": "みせ", "meaning": "shop; store"},
    {"word": "物価", "reading": "ぶっか", "meaning": "consumer prices"},
    {"word": "広告", "reading": "こうこく", "meaning": "advertisement"},
    {"word": "募集", "reading": "ぼしゅう", "meaning": "recruitment"},
    {"word": "約束", "reading": "やくそく", "meaning": "promise; appointment"},
    {"word": "嬉しい", "reading": "うれしい", "meaning": "glad"},
    {"word": "悲しい", "reading": "かなしい", "meaning": "sad"},
    {"word": "厳しい", "reading": "きびしい", "meaning": "strict"},
    {"word": "気分が悪い", "reading": "きぶんがわるい", "meaning": "to feel sick"},
    {"word": "辛い", "reading": "からい", "meaning": "hot and spicy; salty"},
    {"word": "すごい", "reading": "すごい", "meaning": "incredible; awesome"},
    {"word": "近い", "reading": "ちかい", "meaning": "close; near"},
    {"word": "色々な", "reading": "いろいろな", "meaning": "various; different kinds of"},
    {"word": "幸せな", "reading": "しあわせな", "meaning": "happy (lasting happiness)"},
    {"word": "だめな", "reading": "だめな", "meaning": "no good"},
    {"word": "編む", "reading": "あむ", "meaning": "to knit"},
    {"word": "頑張る", "reading": "がんばる", "meaning": "to do one's best; to try hard"},
    {"word": "泣く", "reading": "なく", "meaning": "to cry"},
    {"word": "磨く", "reading": "みがく", "meaning": "to brush (teeth); to polish"},
    {"word": "約束を守る", "reading": "やくそくをまもる", "meaning": "to keep a promise"},
    {"word": "感動する", "reading": "かんどうする", "meaning": "to be moved/touched (by...)"},
    {"word": "全部", "reading": "ぜんぶ", "meaning": "all"},
    {"word": "申します", "reading": "もうします", "meaning": "my name is..."},
    {"word": "特に", "reading": "とくに", "meaning": "especially"},
    # מספרים ובנק
    {"word": "一日", "reading": "いちにち", "meaning": "one day"},
    {"word": "二日", "reading": "ふつか", "meaning": "two days"},
    {"word": "三日", "reading": "みっか", "meaning": "three days"},
    {"word": "四日", "reading": "よっか", "meaning": "four days"},
    {"word": "五日", "reading": "いつか", "meaning": "five days"},
    {"word": "六日", "reading": "むいか", "meaning": "six days"},
    {"word": "七日", "reading": "なのか", "meaning": "seven days"},
    {"word": "八日", "reading": "ようか", "meaning": "eight days"},
    {"word": "九日", "reading": "ここのか", "meaning": "nine days"},
    {"word": "十日", "reading": "とおか", "meaning": "ten days"},
    {"word": "口座", "reading": "こうざ", "meaning": "account"},
    {"word": "手数料", "reading": "てすうりょう", "meaning": "commission"},
    {"word": "キャッシュカード", "reading": "キャッシュカード", "meaning": "bank card"},
    {"word": "通帳", "reading": "つうちょう", "meaning": "passbook"},
    {"word": "預金", "reading": "よきん", "meaning": "savings"},
    {"word": "金額", "reading": "きんがく", "meaning": "amount"},
    {"word": "暗証番号", "reading": "あんしょうばんごう", "meaning": "personal identification number"},
    {"word": "現金", "reading": "げんきん", "meaning": "cash"},
    # מילים מעמודי הקאנג'י
    {"word": "食べ物", "reading": "たべもの", "meaning": "food"},
    {"word": "飲み物", "reading": "のみもの", "meaning": "drink"},
    {"word": "物", "reading": "もの", "meaning": "things"},
    {"word": "買い物", "reading": "かいもの", "meaning": "shopping"},
    {"word": "動物", "reading": "どうぶつ", "meaning": "animal"},
    {"word": "鳥", "reading": "とり", "meaning": "bird; poultry"},
    {"word": "焼き鳥", "reading": "やきとり", "meaning": "grilled chicken"},
    {"word": "白鳥", "reading": "はくちょう", "meaning": "swan"},
    {"word": "料理", "reading": "りょうり", "meaning": "cooking"},
    {"word": "料金", "reading": "りょうきん", "meaning": "charge"},
    {"word": "授業料", "reading": "じゅぎょうりょう", "meaning": "tuition"},
    {"word": "給料", "reading": "きゅうりょう", "meaning": "salary"},
    {"word": "理由", "reading": "りゆう", "meaning": "reason"},
    {"word": "地理", "reading": "ちり", "meaning": "geography"},
    {"word": "無理な", "reading": "むりな", "meaning": "impossible"},
    {"word": "特別な", "reading": "とくべつな", "meaning": "special"},
    {"word": "特徴", "reading": "とくちょう", "meaning": "characteristic"},
    {"word": "特急", "reading": "とっきゅう", "meaning": "super express"},
    {"word": "安い", "reading": "やすい", "meaning": "cheap"},
    {"word": "安全な", "reading": "あんぜんな", "meaning": "safe"},
    {"word": "安心", "reading": "あんしん", "meaning": "relief"},
    {"word": "不安な", "reading": "ふあんな", "meaning": "anxious; worried"},
    {"word": "ご飯", "reading": "ごはん", "meaning": "rice; meal"},
    {"word": "朝ご飯", "reading": "あさごはん", "meaning": "breakfast"},
    {"word": "昼ご飯", "reading": "ひるごはん", "meaning": "lunch"},
    {"word": "晩ご飯", "reading": "ばんごはん", "meaning": "dinner"},
    {"word": "肉", "reading": "にく", "meaning": "meat"},
    {"word": "牛肉", "reading": "ぎゅうにく", "meaning": "beef"},
    {"word": "豚肉", "reading": "ぶたにく", "meaning": "pork"},
    {"word": "肉屋", "reading": "にくや", "meaning": "meat shop"},
    {"word": "筋肉", "reading": "きんにく", "meaning": "muscle"},
    {"word": "悪い", "reading": "わるい", "meaning": "bad"},
    {"word": "最悪", "reading": "さいあく", "meaning": "the worst"},
    {"word": "悪魔", "reading": "あくま", "meaning": "devil"},
    {"word": "体重", "reading": "たいじゅう", "meaning": "body weight"},
    {"word": "体操", "reading": "たいそう", "meaning": "gymnastics; physical exercises"},
    {"word": "同じ", "reading": "おなじ", "meaning": "same"},
    {"word": "同僚", "reading": "どうりょう", "meaning": "coworker"},
    {"word": "同級生", "reading": "どうきゅうせい", "meaning": "classmate"},
    {"word": "同時", "reading": "どうじ", "meaning": "same time"},
    {"word": "着く", "reading": "つく", "meaning": "to arrive"},
    {"word": "着る", "reading": "きる", "meaning": "to wear"},
    {"word": "水着", "reading": "みずぎ", "meaning": "swimwear"},
    {"word": "大阪着", "reading": "おおさかちゃく", "meaning": "arriving at Osaka"},
    {"word": "空気", "reading": "くうき", "meaning": "air"},
    {"word": "空", "reading": "そら", "meaning": "sky"},
    {"word": "空く", "reading": "あく", "meaning": "to be vacant"},
    {"word": "神戸港", "reading": "こうべこう", "meaning": "Kobe Port"},
    {"word": "港", "reading": "みなと", "meaning": "port"},
    {"word": "香港", "reading": "ホンコン", "meaning": "Hong Kong"},
    {"word": "昼", "reading": "ひる", "meaning": "noon; daytime"},
    {"word": "昼寝", "reading": "ひるね", "meaning": "nap"},
    {"word": "昼休み", "reading": "ひるやすみ", "meaning": "lunch break"},
    {"word": "昼食", "reading": "ちゅうしょく", "meaning": "lunch"},
    {"word": "海", "reading": "うみ", "meaning": "sea"},
    {"word": "日本海", "reading": "にほんかい", "meaning": "the Japan Sea"},
    {"word": "海外", "reading": "かいがい", "meaning": "overseas"},
    {"word": "海岸", "reading": "かいがん", "meaning": "coast"},
    {"word": "北海道", "reading": "ほっかいどう", "meaning": "Hokkaido"}
]

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_vocab = data.get("vocab", [])
    # יצירת רשימה של מילים וקריאות שכבר קיימות כדי למנוע כפילויות
    existing_words = {item.get("word") for item in existing_vocab}
    existing_readings = {item.get("reading") for item in existing_vocab}

    start_id = len(existing_vocab) + 1
    added_count = 0
    skipped_count = 0

    for item in genki_13_vocab:
        # אם המילה או הקריאה קיימות במאגר (למשל מגיטהאב), דלג עליה
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v13_{start_id + added_count}",
            "chapter": 13,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים חדשות מפרק 13.")
    print(f"סוננו {skipped_count} מילים שכבר הופיעו במאגרי N4/N5.")

except Exception as e:
    print(f"שגיאה: {e}")
