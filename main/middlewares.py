
class TimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #print('Обработка запроса')
        response = self.get_response(request)
        #print('Обработка ответа')
        return response

    # def process_exception(self, request, exception):
    #     print(f'Exception {exception}')
    #     return HttpResponse(f'Ошибка {exception}')
