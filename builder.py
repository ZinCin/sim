import os

SITE_URL = "https://zincin.github.io/sim/"

HTML_TEMPLATE = """<!DOCTYPE html>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{site_url}/static/thumbnails/{video_id}.jpg">
    <meta property="og:type" content="video.other">
    <meta property="og:url" content="{site_url}/video/{video_id}/">
    <meta name="twitter:card" content="summary_large_image">

    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500&display=swap" rel="stylesheet">
    <link href="https://vjs.zencdn.net/8.10.0/video-js.css" rel="stylesheet" />
    <style>
        :root {{ --bg: #0a0b10; --card: #161922; --accent: #4aa9c2; --text: #e0e0e0; }}
        body {{ 
            background: var(--bg); color: var(--text); font-family: 'Rubik', sans-serif; 
            margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; 
        }}
        .player-wrap {{ width: 100%; max-width: 1000px; border-radius: 12px; overflow: hidden; border: 1px solid #222; background: #000; }}
        .info {{ width: 100%; max-width: 1000px; margin-top: 25px; background: var(--card); padding: 25px; border-radius: 12px; box-sizing: border-box; }}
        h1 {{ margin: 0 0 10px 0; color: var(--accent); font-size: 1.5em; }}
        p {{ line-height: 1.6; opacity: 0.8; margin: 0; }}
    </style>
</head>
<body>
    <div class="player-wrap">
        <video id="vid" class="video-js vjs-default-skin vjs-big-play-centered" controls preload="auto" width="1000" height="560">
            <source src="../../videos/{video_id}/video.mp4" type="video/mp4">
            Ваш браузер не поддерживает элемент <code>video</code>.
        </video>
    </div>
    <div class="info">
        <h1>{title}</h1>
        <p>{description}</p>
    </div>

    <script src="https://vjs.zencdn.net/8.10.0/video.min.js"></script>
    <script>
        // Упрощённая инициализация: теперь используем обычный MP4-файл вместо HLS-плейлиста.
        const player = videojs('vid');
        // Если нужен автоплей в современных браузерах — можно включить player.muted(true); player.play();
    </script>
</body>
</html>
"""


def build():
    base_path = "C:/Users/user/Documents/GitHub/sim"

    video_id = input("ID видео: ").strip()
    title = input("Заголовок: ").strip()
    description = input("Описание: ").strip()

    page_dir = os.path.join(base_path, "video", video_id)
    os.makedirs(page_dir, exist_ok=True)

    # Важно: В <source src="..."> путь должен начинаться с /название_репозитория/
    html = HTML_TEMPLATE.format(
        title=title,
        description=description,
        video_id=video_id,
        site_url=SITE_URL
    )

    with open(os.path.join(page_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # Создаем .nojekyll если его нет
    with open(os.path.join(base_path, ".nojekyll"), "a") as f:
        pass

    print(f"\nГотово. Проверь, что в папке 'sim/videos/{video_id}' лежат файлы .m3u8 и .ts")


if __name__ == "__main__":
    build()
