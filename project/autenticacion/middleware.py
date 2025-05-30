# autenticacion/middleware.py
class JWTAuthCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        print("Middleware JWTAuthCookieMiddleware: Iniciando...")
        token = request.COOKIES.get('access_token')
        print(f"Middleware: access_token encontrado en cookies: {bool(token)}")

        if token:
            request.META['HTTP_AUTHORIZATION'] = f"Bearer {token}"
            print(f"Middleware: Cabecera HTTP_AUTHORIZATION establecida: {request.META.get('HTTP_AUTHORIZATION')}")
        else:
            print("Middleware: No se encontró access_token en cookies.")

        response = self.get_response(request)
        print("Middleware JWTAuthCookieMiddleware: Respuesta generada, retornando.")
        return response