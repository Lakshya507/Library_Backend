from django import template

register = template.Library()

@register.filter
def duration_seconds(seconds):
    try:
        seconds = int(seconds)
        hours, remainder = divmod(seconds, 3600)
        minutes, secs = divmod(remainder, 60)
        return f"{hours}h {minutes}m {secs}s"
    except Exception:
        return "0h 0m 0s"
