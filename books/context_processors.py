from .models import Genre

def categories_context(request):
    return {
        'all_genres': Genre.objects.all().order_by('name'),
    }
