from aiohttp import web

async def handle(request):
    return web.Response(
        text="""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Raffle App</title>
            <script src="https://telegram.org/js/telegram-web-app.js"></script>
            <style>
                body { padding: 20px; font-family: Arial; }
                input { margin: 10px 0; display: block; }
            </style>
        </head>
        <body>
            <h1>Настройки розыгрыша</h1>
            <input type="text" id="post_url" placeholder="Ссылка на пост">
            <button onclick="submitForm()">Создать</button>
            
            <script>
                function submitForm() {
                    const data = {
                        post_url: document.getElementById('post_url').value
                    };
                    Telegram.WebApp.sendData(JSON.stringify(data));
                }
            </script>
        </body>
        </html>
        """,
        content_type="text/html"
    )

app = web.Application()
app.router.add_get("/", handle)

if __name__ == "__main__":
    web.run_app(app, port=8080)