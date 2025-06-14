class JWTAuthCookieMiddleware:
    """
    Middleware que detecta tokens JWT en cookies y los asigna al encabezado HTTP_AUTHORIZATION
    para que DRF los reconozca automáticamente.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si la solicitud es para el admin, no interferimos con el sistema de autenticación
        if request.path.startswith('/admin/'):
            return self.get_response(request)
            
        # Intentamos obtener el token de las cookies
        token = request.COOKIES.get('access_token')
        if token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
            
        # Seguir con el flujo normal de la petición
        return self.get_response(request)