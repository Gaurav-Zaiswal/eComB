from django.conf import settings
class LoginMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.response = self.get_response(request)
        return self.response