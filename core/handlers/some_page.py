from fastapi import Request
from core.classes.webapp import GamersWeb

app = GamersWeb()

@app.new_handler
async def some_page(request: Request, id: int):
    return await app.render_template("some_page.html", request, id=id)