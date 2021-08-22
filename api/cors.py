class CorsMiddleware:
    def process_response(self, req, resp):
        resp["Access-Control-Allow-Origin"] = "*"
        return resp
