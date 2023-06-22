from .models import SubRubric

#Рубрики на всех страницах сайта
def categories_for_all_pages(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context