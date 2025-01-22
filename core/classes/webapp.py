from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from core.classes.singleton import SingletonMeta

from configuration import PAGE_ROUTES

class GamersWeb(FastAPI, metaclass=SingletonMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.handlers = {}
        
        self.templates = Jinja2Templates(directory="./templates")
        self.statics = StaticFiles(directory="./static")
        
        self.mount(path="/static", app=self.statics, name="static")
        self.mount(path="/templates", app=self.templates, name="templates")
        
    async def render_template(self, name: str, request: Request, **context):
        return self.templates.TemplateResponse(
            name, context={"request": request, **context}
        )

    def register_routes(self):
        for route in PAGE_ROUTES:
            self.add_route(path=route["path"], route=self.handlers[route["endpoint"]], methods=route["methods"])
    
    def new_handler(self, f):
        print("New handler registering:", f.__name__)
        self.handlers[f.__name__] = f