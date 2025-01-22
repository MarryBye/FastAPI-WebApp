import asyncio

from core.classes.webapp import GamersWeb
from core.handlers.main_page import main_page

app = GamersWeb()
app.register_routes()

# def convert_string_to_tuples(string: str, separator: str=",") -> tuple[tuple]:
#     return tuple(tuple(el.split("|")) for el in string.split(separator))

# a = "1|Aboba,2|Aboba2"

# a = convert_string_to_tuples(a)
# print(a)