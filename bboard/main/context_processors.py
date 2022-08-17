from .models import SubRubric


def categories_for_all_pages(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context