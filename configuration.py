PAGE_ROUTES = [
    {
        "path": "/",
        "endpoint": "main_page",
        "methods": ["GET"]
    },
    {
        "path": "/some_page/{id}",
        "endpoint": "some_page",
        "methods": ["GET"]
    }
]

GLOBAL_CONTEXT = {
    "SITE_NAME": "GMRS | Website"
}
