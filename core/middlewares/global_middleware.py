from fastapi import Request
from core.classes.webapp import GamersWeb
from starlette.middleware.base import BaseHTTPMiddleware

from configuration import GLOBAL_CONTEXT

class GlobalMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        request.state.global_context = GLOBAL_CONTEXT
        
        response = await call_next(request) 
        return response
    
GamersWeb().add_middleware(GlobalMiddleware)