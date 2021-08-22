class CorsMiddleware:
    def __init__(self, *args, **kwargs):
        pass

    def process_response(self, req, resp):
        resp["Access-Control-Allow-Origin"] = "*"
        return resp
