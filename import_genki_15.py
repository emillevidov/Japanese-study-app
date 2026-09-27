import json
import os

DATA_FILE = "data.json"

genki_15_vocab = [
    # Nouns
    {"word": "外国人", "reading": "がいこくじん", "meaning": "foreigner"},
    {"word": "そば", "reading": "そば", "meaning": "soba; Japanese buckwheat noodles"},
    {"word": "絵", "reading": "え", "meaning": "painting; picture; drawing"},
    {"word": "地図", "reading": "ちず", "meaning": "map"},
    {"word": "辞書", "reading": "じしょ", "meaning": "dictionary"},
    {"word": "家具", "reading": "かぐ", "meaning": "furniture"},
    {"word": "電池", "reading": "でんち", "meaning": "battery"},
    {"word": "ジャケット", "reading": "ジャケット", "meaning": "jacket"},
    {"word": "ペット", "reading": "ペット", "meaning": "pet"},
    {"word": "割引券", "reading": "わりびきけん", "meaning": "discount coupon"},
    {"word": "インターネット", "reading": "インターネット", "meaning": "internet (more colloquially, ネット)"},
    {"word": "地震", "reading": "じしん", "meaning": "earthquake"},
    {"word": "保険", "reading": "ほけん", "meaning": "insurance"},
    {"word": "税金", "reading": "ぜいきん", "meaning": "tax"},
    {"word": "教室", "reading": "きょうしつ", "meaning": "classroom"},
    {"word": "建物", "reading": "たてもの", "meaning": "building"},
    {"word": "プール", "reading": "プール", "meaning": "swimming pool"},
    {"word": "映画館", "reading": "えいがかん", "meaning": "movie theater"},
    {"word": "旅館", "reading": "りょかん", "meaning": "Japanese inn"},
    {"word": "庭", "reading": "にわ", "meaning": "garden"},
    {"word": "ボランティア", "reading": "ボランティア", "meaning": "volunteer"},
    {"word": "活動", "reading": "かつどう", "meaning": "activity"},
    {"word": "経験", "reading": "けいけん", "meaning": "experience"},
    {"word": "習慣", "reading": "しゅうかん", "meaning": "custom"},
    {"word": "締め切り", "reading": "しめきり", "meaning": "deadline"},
    {"word": "予定", "reading": "よてい", "meaning": "schedule; plan"},
    {"word": "卒業式", "reading": "そつぎょうしき", "meaning": "graduation ceremony"},
    {"word": "結婚式", "reading": "けっこんしき", "meaning": "wedding"},

    # U-verbs
    {"word": "売る", "reading": "うる", "meaning": "to sell (〜を)"},
    {"word": "下ろす", "reading": "おろす", "meaning": "to withdraw (money) (〜を)"},
    {"word": "描く", "reading": "かく", "meaning": "to draw; to paint (〜を)"},
    {"word": "探す", "reading": "さがす", "meaning": "to look for (〜を)"},
    {"word": "誘う", "reading": "さそう", "meaning": "to invite (〜を)"},
    {"word": "しゃべる", "reading": "しゃべる", "meaning": "to chat"},
    {"word": "付き合う", "reading": "つきあう",
     "meaning": "(1) to date (someone) (person と) (2) to keep company (purpose に)"},
    {"word": "着く", "reading": "つく", "meaning": "to arrive (place に)"},
    {"word": "保険に入る", "reading": "ほけんにはいる", "meaning": "to buy insurance"},

    # Ru-verbs
    {"word": "気をつける", "reading": "きをつける", "meaning": "to be cautious/careful (〜に)"},
    {"word": "調べる", "reading": "しらべる", "meaning": "to look into (a matter) (matter を)"},
    {"word": "見える", "reading": "みえる", "meaning": "to be visible (〜が)"},

    # Irregular Verbs
    {"word": "する", "reading": "する", "meaning": "to decide on (an item) (item に)"},
    {"word": "観光する", "reading": "かんこうする", "meaning": "to do sightseeing"},
    {"word": "予約する", "reading": "よやくする", "meaning": "to reserve (〜を)"},
    {"word": "参加する", "reading": "さんかする", "meaning": "to participate (〜に)"},
    {"word": "卒業する", "reading": "そつぎょうする", "meaning": "to graduate (from...) (school を)"},
    {"word": "発表する", "reading": "はっぴょうする", "meaning": "to make a presentation; to make public"},

    # Adverbs and Other Expressions
    {"word": "〜けど", "reading": "〜けど", "meaning": "..., but; ..., so"},
    {"word": "〜目", "reading": "〜め", "meaning": "-th"},
    {"word": "一日目", "reading": "いちにちめ", "meaning": "first day"},
    {"word": "一日中", "reading": "いちにちじゅう", "meaning": "all day long"},
    {"word": "最近", "reading": "さいきん", "meaning": "recently"},
    {"word": "もう一度", "reading": "もういちど", "meaning": "one more time"},
    {"word": "楽しみです", "reading": "たのしみです", "meaning": "cannot wait; to look forward to it"},

    # Useful Expressions - At the Hotel
    {"word": "〜泊", "reading": "〜はく", "meaning": "... nights"},
    {"word": "朝食付き", "reading": "ちょうしょくつき", "meaning": "with breakfast"},
    {"word": "一泊二食付き", "reading": "いっぱくにしょくつき", "meaning": "one night with two meals"},
    {"word": "チェックイン（する）", "reading": "チェックイン（する）", "meaning": "checking in"},
    {"word": "チェックアウト（する）", "reading": "チェックアウト（する）", "meaning": "checking out"},
    {"word": "シングル", "reading": "シングル", "meaning": "single room"},
    {"word": "ダブル", "reading": "ダブル", "meaning": "double room"},
    {"word": "ツイン", "reading": "ツイン", "meaning": "twin room"},
    {"word": "〜名", "reading": "〜めい", "meaning": "... person(s)"},
    {"word": "フロント", "reading": "フロント", "meaning": "receptionist; front desk"},
    {"word": "禁煙", "reading": "きんえん", "meaning": "non-smoking"},
    {"word": "喫煙", "reading": "きつえん", "meaning": "smoking"},
    {"word": "大浴場", "reading": "だいよくじょう", "meaning": "large spa"},

    # Hotel Sentences
    {"word": "予約した〇〇です。チェックインお願いします。", "reading": "よやくした〇〇です。チェックインおねがいします。",
     "meaning": "I have a reservation under the name of XX. Could you check me in, please?"},
    {"word": "〇〇で払えますか。", "reading": "〇〇ではらえますか。", "meaning": "Can I pay by XX?"},
    {"word": "アメリカドルを日本円に両替できますか。", "reading": "アメリカドルをにほんえんにりょうがえできますか。",
     "meaning": "Can you change US dollars to Japanese yen?"},
    {"word": "タクシーを呼んでもらえますか。", "reading": "タクシーをよんでもらえますか。",
     "meaning": "Would you call a taxi for us?"},
    {"word": "近くにおすすめのレストランがありますか。", "reading": "ちかくにおすすめのレストランがありますか。",
     "meaning": "Are there any restaurants you recommend near here?"},
    {"word": "二時まで荷物を預かってもらえますか。", "reading": "にじまでにモつをあずかってもらえますか。",
     "meaning": "Could you keep my luggage until 2 o'clock?"}
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

    for item in genki_15_vocab:
        if item["word"] in existing_words or item["reading"] in existing_readings:
            skipped_count += 1
            continue

        existing_vocab.append({
            "id": f"v15_{start_id + added_count}",
            "chapter": 15,
            "word": item["word"],
            "reading": item["reading"],
            "meaning": item["meaning"]
        })
        added_count += 1

    data["vocab"] = existing_vocab

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"הייבוא הושלם! נוספו {added_count} מילים חדשות מפרק 15.")
    print(f"סוננו {skipped_count} מילים שכבר הופיעו במאגר.")

except Exception as e:
    print(f"שגיאה: {e}")