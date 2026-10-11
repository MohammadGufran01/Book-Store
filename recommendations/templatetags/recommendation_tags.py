from django import template
from django.utils.safestring import mark_safe
from recommendations.services.engine import RecommendationEngine

register = template.Library()


@register.simple_tag
def get_user_recommendations(user, limit=8):
    return RecommendationEngine.get_for_user(user, limit=int(limit))


@register.simple_tag
def get_similar_books(book, limit=6):
    return RecommendationEngine.get_similar_books(book, limit=int(limit))


@register.simple_tag
def get_frequently_bought_together(book, limit=3):
    return RecommendationEngine.get_frequently_bought_together(book, limit=int(limit))


@register.simple_tag
def get_trending_books(limit=8):
    return RecommendationEngine.get_trending_bestsellers(limit=int(limit))


@register.simple_tag
def get_genre_spotlight(genre, limit=6):
    return RecommendationEngine.get_genre_highlights(genre, limit=int(limit))


@register.filter
def render_stars(rating):
    try:
        r = float(rating or 0)
    except (ValueError, TypeError):
        r = 0.0

    full_stars = int(r)
    has_half = (r - full_stars) >= 0.4
    empty_stars = 5 - full_stars - (1 if has_half else 0)

    html = []
    for _ in range(full_stars):
        html.append('<i data-lucide="star" class="w-4 h-4 fill-amber-400 text-amber-400"></i>')
    if has_half:
        html.append('<i data-lucide="star-half" class="w-4 h-4 fill-amber-400 text-amber-400"></i>')
    for _ in range(empty_stars):
        html.append('<i data-lucide="star" class="w-4 h-4 text-slate-300"></i>')

    return mark_safe("".join(html))


@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def sub(value, arg):
    try:
        return round(float(value) - float(arg), 2)
    except (ValueError, TypeError):
        return 0.0


@register.filter
def is_in_set(item_id, target_set):
    if not target_set:
        return False
    return item_id in target_set
