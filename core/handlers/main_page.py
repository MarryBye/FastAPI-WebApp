from fastapi import Request
from core.classes.webapp import GamersWeb

app = GamersWeb()

@app.new_handler
async def main_page(request: Request):
    return await app.render_template("main.html", request, a=5)