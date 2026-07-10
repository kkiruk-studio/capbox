#!/usr/bin/env python3
"""Generate index.html for every locale from one template.

Usage: python3 build.py
Output: ./index.html (ko), ./en/index.html, ./ja/index.html
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
BASE_URL = "https://kkiruk-studio.github.io/capbox/"

# After App Store approval, set this to the real App Store URL (e.g. https://apps.apple.com/app/id1234567890)
APP_STORE_URL = ""

LANG_LABELS = [("ko/", "한국어"), ("", "EN"), ("ja/", "日本語")]

# Three sample "flying" screenshots used in the hero demo animation (card -> folder).
DEMO_BARS = ["w80", "w60", "w40"]

LOCALES = {
    "ko": {
        "dir": "ko/", "lang": "ko", "font": None,
        "title": "CapBox — 스크린샷 자동 분류",
        "desc": "단톡방 짤, 영수증, 지도 캡처로 쌓인 스크린샷을 CapBox가 온디바이스 AI로 자동 분류합니다. 사진은 기기 밖으로 나가지 않아요.",
        "og_title": "CapBox — 스크린샷 자동 분류",
        "og_desc": "일단 캡처해두면, CapBox 안에 정리돼 있다.",
        "kicker_num": "스크린샷 정리",
        "h1": "일단 캡처해두면,<br><em>CapBox</em> 안에 정리돼 있다.",
        "sub": "단톡방에서 쏟아지는 짤, 결제하고 찍어둔 영수증, 여행 중 캡처한 지도까지 — 사진 앱에 뒤섞인 스크린샷을 CapBox가 폴더별로 정리합니다. 온디바이스 AI라 사진은 기기 밖으로 절대 나가지 않아요.",
        "badge_small": "다운로드는", "note": "온디바이스 · 가입 없음 · iPhone",
        "badge_aria": "App Store에서 다운로드",
        "chips": [["짤", "짤/밈 폴더"], ["영", "영수증 폴더"], ["지", "지도 폴더"]],
        "hero_alt": "CapBox 폴더 목록 화면 — 짤/밈, 대화, 결제, 지도 등으로 정리된 앨범",
        "marquee": ["짤 정리", "영수증 정리", "대화 캡처", "지도 캡처", "온디바이스 AI", "텍스트 검색", "원터치 분류", "일괄 정리"],
        "how_kicker": "사용 방법",
        "how_h2": "스캔 한 번, <em>탭 한 번</em>으로 정리 끝.",
        "steps": [
            ["스캔", "사진 라이브러리 스캔", "카메라 롤에 쌓인 스크린샷을 한 번에 훑어서 몇 장이 정리 안 됐는지 보여줍니다."],
            ["분류", "AI 제안 확인하고 한 탭", "온디바이스 AI가 폴더를 추천하면 한 장씩, 또는 여러 장을 한 번에 골라 보낼 수 있어요."],
            ["보관", "사진 앱 앨범으로 저장", "정리된 스크린샷은 사진 앱의 진짜 앨범이 되어, CapBox 없이도 그대로 남습니다."],
        ],
        "conv_kicker": "핵심 가치", "conv_num": "온디바이스",
        "conv_h2": "정리는 되는데, <em>사진은 안 나간다</em>.",
        "conv_lede": "OCR도, 이미지 분류도 전부 기기 안에서 Vision 프레임워크로 처리합니다. 서버가 없으니 보낼 곳도 없어요.",
        "conv_rows": [
            ["photo.stack", "사진 보관함 스캔", "1단계"],
            ["sparkles", "온디바이스 AI 분류 제안", "2단계"],
            ["folder.fill", "사진 앱 앨범에 저장", "3단계"],
        ],
        "maps_kicker": "폴더 구성", "maps_num": "예시",
        "maps_h2": "카테고리는 <em>내 마음대로</em>.",
        "maps_lede": "짤/밈, 대화, 결제, 지도, 쇼핑, 문서 — 기본 제안 폴더로 시작하고, 이름·색·아이콘은 자유롭게 바꿀 수 있습니다.",
        "providers": [
            ["😂", "짤/밈", [["웃긴 캡처", "밈 모음"]]],
            ["💬", "대화", [["카톡", "단톡방 캡처"]]],
            ["🧾", "결제", [["영수증", "주문 내역"]]],
            ["🗺️", "지도", [["장소", "가게·주소 캡처"]]],
        ],
        "shots_kicker": "화면", "shots_num": "IOS",
        "shots_h2": "쌓아두기용이 아니라, <em>꺼내 쓰는 도구</em>로.",
        "shots_caps": ["폴더별 정리 화면", "한 장씩 분류하기", "통계로 보는 스크린샷"],
        "feat_kicker": "디테일", "feat_num": "06",
        "feat_h2": "작은 앱, <em>분명한 선택</em>.",
        "feats": [
            ["사진 앱 앨범과 동기화", "CapBox 폴더는 곧 사진 앱의 진짜 앨범입니다. 별도 저장소가 없어 데이터가 갇히지 않아요."],
            ["한 장씩 또는 한 번에", "카드 한 장씩 넘기며 정리할 수도, 여러 장을 골라 한 번에 폴더로 보낼 수도 있습니다."],
            ["온디바이스 AI 제안", "Vision으로 텍스트와 이미지를 분석해 폴더를 추천합니다. 사진은 기기 밖으로 절대 나가지 않아요."],
            ["스크린샷 속 텍스트 검색", "OCR로 읽어둔 텍스트 그대로 검색해서, 어떤 캡처였는지 기억 안 나도 바로 찾습니다."],
            ["필요 없는 캡처는 바로 삭제", "정리하다 필요 없어진 스크린샷은 그 자리에서 바로 지울 수 있어요."],
            ["연도·용량 통계", "스크린샷이 연도별로 몇 장씩 쌓였는지, 어떤 해상도가 많은지 한눈에 봅니다."],
        ],
        "final_h2": "스크린샷 폴더, 더 이상 미루지 마세요.", "final_lede": "iPhone에서 무료.",
        "f_contact": "문의", "f_privacy": "개인정보 처리방침", "f_terms": "이용약관",
    },
    "en": {
        "dir": "", "lang": "en", "font": None,
        "title": "CapBox — Sort screenshots automatically",
        "desc": "Meme stashes, receipt photos, saved maps — CapBox sorts the screenshots piling up in your camera roll with on-device AI. Your photos never leave your phone.",
        "og_title": "CapBox — Sort screenshots automatically",
        "og_desc": "Screenshot now. Find it later.",
        "kicker_num": "SCREENSHOT SORTING",
        "h1": "Screenshot now.<br><em>Find it later.</em>",
        "sub": "Memes from group chats, receipts you photographed at checkout, a map you screenshotted mid-trip — they all pile up in one messy camera roll. CapBox sorts them into folders with on-device AI, so your photos never leave your phone.",
        "badge_small": "Download on the", "note": "ON-DEVICE · NO ACCOUNT · IPHONE",
        "badge_aria": "Download on the App Store",
        "chips": [["M", "Memes folder"], ["R", "Receipts folder"], ["P", "Places folder"]],
        "hero_alt": "CapBox folder grid showing albums like Memes, Chats, Receipts, and Places",
        "marquee": ["SORT MEMES", "SORT RECEIPTS", "CHAT CAPTURES", "SAVED MAPS", "ON-DEVICE AI", "TEXT SEARCH", "ONE-TAP SORT", "BATCH SORT"],
        "how_kicker": "HOW IT WORKS",
        "how_h2": "One scan, <em>one tap</em>, done.",
        "steps": [
            ["SCAN", "Scan your camera roll", "CapBox sweeps your photo library and shows you exactly how many screenshots are still waiting to be sorted."],
            ["SORT", "Confirm the AI suggestion", "On-device AI suggests a folder for each screenshot — sort one at a time, or select a batch and send them all at once."],
            ["KEEP", "Saved as real Photos albums", "Sorted screenshots become real albums in your Photos app — they stay there even without CapBox."],
        ],
        "conv_kicker": "CORE VALUE", "conv_num": "ON-DEVICE",
        "conv_h2": "Sorted, but <em>never uploaded</em>.",
        "conv_lede": "OCR and image classification both run locally with Apple's Vision framework. There's no server to send anything to.",
        "conv_rows": [
            ["photo.stack", "Scan Photos library", "STEP 1"],
            ["sparkles", "On-device AI suggests a folder", "STEP 2"],
            ["folder.fill", "Saved to a real Photos album", "STEP 3"],
        ],
        "maps_kicker": "FOLDERS", "maps_num": "EXAMPLES",
        "maps_h2": "Categories, <em>your way</em>.",
        "maps_lede": "Start from suggested folders like Memes, Chats, Receipts, Places, Shopping, and Docs — then rename, recolor, or re-icon any of them.",
        "providers": [
            ["😂", "Memes", [["Funny caps", "Meme stash"]]],
            ["💬", "Chats", [["Group chat", "Conversation caps"]]],
            ["🧾", "Receipts", [["Checkout", "Order confirmations"]]],
            ["🗺️", "Places", [["Maps", "Store & address caps"]]],
        ],
        "shots_kicker": "SCREENS", "shots_num": "IOS",
        "shots_h2": "Built to be <em>used</em>, not just stored.",
        "shots_caps": ["FOLDER OVERVIEW", "ONE-CARD SORTING", "SCREENSHOT STATS"],
        "feat_kicker": "DETAILS", "feat_num": "06",
        "feat_h2": "Small app. <em>Deliberate</em> choices.",
        "feats": [
            ["Synced with real Photos albums", "CapBox folders are actual Photos albums — no separate storage to get locked into."],
            ["Sort one, or sort a batch", "Flip through screenshots one card at a time, or multi-select a pile and send them all at once."],
            ["On-device AI suggestions", "Vision analyzes text and image content to suggest a folder. Your photos never leave the device."],
            ["Search text inside screenshots", "On-device OCR means you can search for what a screenshot said, even if you forgot what it looked like."],
            ["Delete unwanted captures instantly", "Spot a screenshot you don't need anymore? Delete it right from the sorting flow."],
            ["Year & size stats", "See how many screenshots piled up per year, and which resolutions dominate your library."],
        ],
        "final_h2": "Stop putting off that screenshot folder.", "final_lede": "Free on iPhone.",
        "f_contact": "Contact", "f_privacy": "Privacy", "f_terms": "Terms",
    },
    "ja": {
        "dir": "ja/", "lang": "ja", "font": '"Hiragino Kaku Gothic ProN", "Hiragino Sans", "Yu Gothic"',
        "title": "CapBox — スクショを自動で整理",
        "desc": "グループチャットのネタ画像、レシート撮影、地図のスクショ — CapBoxがオンデバイスAIでカメラロールのスクショを自動整理。写真は端末の外に出ません。",
        "og_title": "CapBox — スクショを自動で整理",
        "og_desc": "撮っておけば、CapBoxが整理してくれる。",
        "kicker_num": "スクショ整理",
        "h1": "撮っておけば、<br><em>CapBox</em>が整理してくれる。",
        "sub": "グループチャットのネタ画像、会計時に撮ったレシート、旅先で撮った地図のスクショ — カメラロールにごちゃ混ぜになったスクショを、CapBoxがフォルダごとに整理します。オンデバイスAIなので、写真は端末の外に出ることはありません。",
        "badge_small": "ダウンロードは", "note": "オンデバイス · 登録不要 · iPhone",
        "badge_aria": "App Store でダウンロード",
        "chips": [["ネ", "ネタ画像フォルダ"], ["レ", "レシートフォルダ"], ["地", "地図フォルダ"]],
        "hero_alt": "CapBoxのフォルダ一覧画面 — ネタ画像、会話、レシート、地図などに整理されたアルバム",
        "marquee": ["ネタ画像整理", "レシート整理", "会話キャプチャ", "地図キャプチャ", "オンデバイスAI", "テキスト検索", "ワンタップ整理", "一括整理"],
        "how_kicker": "使い方",
        "how_h2": "スキャン1回、<em>タップ1回</em>で完了。",
        "steps": [
            ["スキャン", "カメラロールをスキャン", "たまったスクショを一気にチェックして、未整理が何枚あるか見せてくれます。"],
            ["整理", "AIの提案をタップで確認", "オンデバイスAIがフォルダを提案。1枚ずつでも、まとめて選んで一括でも整理できます。"],
            ["保存", "写真アプリの本物のアルバムに", "整理したスクショは写真アプリの実際のアルバムになるので、CapBoxがなくてもそのまま残ります。"],
        ],
        "conv_kicker": "コア価値", "conv_num": "オンデバイス",
        "conv_h2": "整理はできても、<em>写真は外に出ない</em>。",
        "conv_lede": "OCRも画像分類も、AppleのVisionフレームワークで端末内だけで処理。送信先のサーバー自体がありません。",
        "conv_rows": [
            ["photo.stack", "写真ライブラリをスキャン", "STEP 1"],
            ["sparkles", "オンデバイスAIがフォルダを提案", "STEP 2"],
            ["folder.fill", "写真アプリの本物のアルバムへ", "STEP 3"],
        ],
        "maps_kicker": "フォルダ", "maps_num": "例",
        "maps_h2": "カテゴリーは<em>自由自在</em>。",
        "maps_lede": "ネタ画像・会話・レシート・地図・ショッピング・書類などの提案フォルダから始めて、名前・色・アイコンは自由に変更できます。",
        "providers": [
            ["😂", "ネタ画像", [["面白キャプチャ", "ネタ画像まとめ"]]],
            ["💬", "会話", [["グループチャット", "会話のスクショ"]]],
            ["🧾", "レシート", [["会計", "注文確認"]]],
            ["🗺️", "地図", [["マップ", "店舗・住所のスクショ"]]],
        ],
        "shots_kicker": "画面", "shots_num": "IOS",
        "shots_h2": "しまい込むためじゃなく、<em>使うための道具</em>に。",
        "shots_caps": ["フォルダ一覧画面", "1枚ずつ整理", "スクショ統計"],
        "feat_kicker": "こだわり", "feat_num": "06",
        "feat_h2": "小さなアプリ、<em>明確な選択</em>。",
        "feats": [
            ["写真アプリのアルバムと同期", "CapBoxのフォルダは実際の写真アルバム。独自ストレージに閉じ込められることはありません。"],
            ["1枚ずつ、またはまとめて", "カードを1枚ずつめくって整理も、複数選択して一括送信もできます。"],
            ["オンデバイスAIの提案", "Visionがテキストと画像を解析してフォルダを提案。写真は端末の外に出ません。"],
            ["スクショ内のテキスト検索", "オンデバイスOCRで、見た目を忘れても書いてあった文字で検索できます。"],
            ["不要なキャプチャをすぐ削除", "整理中に不要だと気づいたスクショは、その場ですぐ削除できます。"],
            ["年別・容量の統計", "年ごとに何枚たまったか、どの解像度が多いかが一目でわかります。"],
        ],
        "final_h2": "スクショフォルダ、もう後回しにしない。", "final_lede": "iPhoneで無料。",
        "f_contact": "お問い合わせ", "f_privacy": "プライバシーポリシー", "f_terms": "利用規約",
    },
}


def hreflang_block():
    lines = [f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}">']
    for key, loc in LOCALES.items():
        lines.append(f'<link rel="alternate" hreflang="{loc["lang"]}" href="{BASE_URL}{loc["dir"]}">')
    return "\n".join(lines)


def lang_nav(cur_dir, rel):
    out = []
    for d, label in LANG_LABELS:
        cls = ' class="cur"' if d == cur_dir else ""
        href = (rel + d) if d else (rel if rel else "./")
        out.append(f'<a href="{href}"{cls}>{label}</a>')
    return "".join(out)


def badge(loc, el_id):
    return (f'<a class="store-badge" id="{el_id}" href="#" aria-label="{loc["badge_aria"]}">'
            f'<svg viewBox="0 0 384 512" aria-hidden="true"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>'
            f'<span class="txt"><small>{loc["badge_small"]}</small><strong>App Store</strong></span></a>')


def mock_folder_screen():
    return """<div class="mock-screen"><div class="mtitle">CapBox</div><div class="mgrid">
      <div class="mfolder"><div class="micon" style="background:#ff9f43">😂</div><div class="mname">짤/밈</div><div class="mcount">128</div></div>
      <div class="mfolder"><div class="micon" style="background:#5b8def">💬</div><div class="mname">대화</div><div class="mcount">64</div></div>
      <div class="mfolder"><div class="micon" style="background:#e8618c">🧾</div><div class="mname">결제</div><div class="mcount">32</div></div>
      <div class="mfolder"><div class="micon" style="background:#2ecc71">🗺️</div><div class="mname">지도</div><div class="mcount">21</div></div>
      </div></div>"""


def mock_sort_screen():
    return """<div class="mock-screen sort"><div class="shotcard">
      <div class="sbar" style="width:70%"></div><div class="sbar" style="width:45%"></div><div class="sbar" style="width:85%"></div>
      </div><div class="chiprow"><span class="mchip">짤/밈</span><span class="mchip">대화</span><span class="mchip">결제</span></div></div>"""


def mock_stats_screen():
    return """<div class="mock-screen stats"><div class="mstatrow">
      <div class="mstat"><div class="mv">4,821</div><div class="ml">전체 이미지</div></div>
      <div class="mstat"><div class="mv">1,203</div><div class="ml">스크린샷</div></div>
      </div><div class="mbars">
      <div class="mbar" style="height:30%"></div><div class="mbar" style="height:55%"></div><div class="mbar" style="height:40%"></div>
      <div class="mbar" style="height:75%"></div><div class="mbar" style="height:60%"></div><div class="mbar" style="height:90%"></div>
      </div></div>"""


MOCK_SCREENS = [mock_folder_screen, mock_sort_screen, mock_stats_screen]


def render(key):
    loc = LOCALES[key]
    rel = "../" if loc["dir"] else ""
    font_override = f'<style>body{{font-family:-apple-system,BlinkMacSystemFont,{loc["font"]},"Segoe UI",sans-serif}}</style>' if loc["font"] else ""
    chips = "".join(
        f'<div class="chip c{i+1}"><span class="g">{g}</span>{label}</div>'
        for i, (g, label) in enumerate(loc["chips"])
    )
    marquee = "".join(f"<span>{m}</span>" for m in loc["marquee"] * 2)
    steps = "".join(
        f'<div class="step"><span class="n">0{i+1}</span><span class="tag">{tag}</span><h3>{h}</h3><p>{p}</p></div>'
        for i, (tag, h, p) in enumerate(loc["steps"])
    )
    conv = "".join(
        f'<div class="convert-row"><span class="g">{i+1}</span><span class="label">{label}</span><span class="cat">{c}</span></div>'
        for i, (icon, label, c) in enumerate(loc["conv_rows"])
    )
    provs = "".join(
        '<div class="prov"><span class="flag">%s</span><h3>%s</h3><ul>%s</ul></div>'
        % (flag, name, "".join(f'<li><span class="g">{g[0]}</span>{n}</li>' for g, n in items))
        for flag, name, items in loc["providers"]
    )
    shots = "".join(
        f'<figure><div class="phone mock">{fn()}<div class="island"></div></div><figcaption>{cap}</figcaption></figure>'
        for fn, cap in zip(MOCK_SCREENS, loc["shots_caps"])
    )
    feats = "".join(f'<div class="feat"><h3>{h}</h3><p>{p}</p></div>' for h, p in loc["feats"])

    html = f"""<!doctype html>
<html lang="{loc['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{loc['title']}</title>
<meta name="description" content="{loc['desc']}">
<meta property="og:title" content="{loc['og_title']}">
<meta property="og:description" content="{loc['og_desc']}">
<meta property="og:image" content="{BASE_URL}assets/icon-512.png">
<meta property="og:type" content="website">
<link rel="canonical" href="{BASE_URL}{loc['dir']}">
{hreflang_block()}
<link rel="icon" type="image/png" href="{rel}assets/icon-180.png">
<link rel="apple-touch-icon" href="{rel}assets/icon-180.png">
<link rel="stylesheet" href="{rel}assets/style.css">
{font_override}
</head>
<body>

<nav>
  <div class="wrap">
    <a class="wordmark" href="{rel if rel else './'}"><img src="{rel}assets/icon-180.png" alt=""><span>CAPBOX</span></a>
    <div class="lang">{lang_nav(loc['dir'], rel)}</div>
  </div>
</nav>

<header class="hero">
  <div class="ghost">C·B</div>
  <div class="wrap">
    <div>
      <div class="kicker"><span>CAPBOX</span><span class="rule"></span><span class="num">{loc['kicker_num']}</span></div>
      <h1>{loc['h1']}</h1>
      <div class="demo">
        <div class="shot"><div class="bar w80"></div><div class="bar w60"></div><div class="bar w40"></div></div>
        <div class="folder"><span class="g">📁</span><span class="label">{loc['chips'][0][1]}</span></div>
      </div>
      <p class="sub">{loc['sub']}</p>
      <div class="cta">
        {badge(loc, 'storeLink')}
        <span class="note">{loc['note']}</span>
      </div>
    </div>
    <div class="phone-col">
      {chips}
      <div class="phone mock">{mock_folder_screen()}<div class="island"></div></div>
    </div>
  </div>
</header>

<div class="marquee" aria-hidden="true"><div class="track">{marquee}</div></div>

<section>
  <div class="wrap">
    <div class="kicker"><span>{loc['how_kicker']}</span><span class="rule"></span><span class="num">01–03</span></div>
    <h2>{loc['how_h2']}</h2>
    <div class="steps">{steps}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="kicker"><span>{loc['conv_kicker']}</span><span class="rule"></span><span class="num">{loc['conv_num']}</span></div>
    <h2>{loc['conv_h2']}</h2>
    <p class="lede">{loc['conv_lede']}</p>
    <div class="convert-table">{conv}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="kicker"><span>{loc['maps_kicker']}</span><span class="rule"></span><span class="num">{loc['maps_num']}</span></div>
    <h2>{loc['maps_h2']}</h2>
    <p class="lede">{loc['maps_lede']}</p>
    <div class="providers">{provs}</div>
  </div>
</section>

<section class="shots">
  <div class="wrap">
    <div class="kicker"><span>{loc['shots_kicker']}</span><span class="rule"></span><span class="num">{loc['shots_num']}</span></div>
    <h2>{loc['shots_h2']}</h2>
    <div class="row">{shots}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kicker"><span>{loc['feat_kicker']}</span><span class="rule"></span><span class="num">{loc['feat_num']}</span></div>
    <h2>{loc['feat_h2']}</h2>
    <div class="grid6">{feats}</div>
  </div>
</section>

<section class="final">
  <div class="wrap">
    <h2>{loc['final_h2']}</h2>
    <p class="lede">{loc['final_lede']}</p>
    <div class="cta">{badge(loc, 'storeLink2')}</div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="brand"><img src="{rel}assets/icon-180.png" alt=""><strong>kkiruk studio</strong></div>
    <div class="links">
      <a href="mailto:kkirukstudio.help@gmail.com">{loc['f_contact']}</a>
      <a href="https://kkiruk-studio.github.io/privacy-policy-app/">{loc['f_privacy']}</a>
      <a href="https://kkiruk-studio.github.io/terms-of-service-app/">{loc['f_terms']}</a>
    </div>
    <div>© 2026 kkiruk studio</div>
  </div>
</footer>

<script>
  // After App Store approval, set the real URL here (e.g. https://apps.apple.com/app/id1234567890)
  const APP_STORE_URL = "{APP_STORE_URL}";
  if (APP_STORE_URL) {{
    document.getElementById("storeLink").href = APP_STORE_URL;
    document.getElementById("storeLink2").href = APP_STORE_URL;
  }} else {{
    document.getElementById("storeLink").style.display = "none";
    document.getElementById("storeLink2").style.display = "none";
  }}
</script>
</body>
</html>
"""
    out = ROOT / loc["dir"] / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(html)} bytes)")


for key in LOCALES:
    render(key)
