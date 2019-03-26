from django.template import Library
from django.utils import timezone

register = Library()


@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)


def pretty_time_delta(seconds):
    sign_string = '-' if seconds < 0 else ''
    seconds = abs(int(seconds))
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days > 0:
        return "{sign}{d} days {h} hours".format(
            sign=sign_string, d=days, h=hours)
    elif hours > 0:
        return "{sign}{h} hours {m} minutes".format(
            sign=sign_string, h=hours, m=minutes)
    elif minutes > 0:
        return "{sign}{m} minutes {s} seconds".format(
            sign=sign_string, m=minutes, s=seconds)
    else:
        return "{sign}{s} seconds".foramt(s=seconds)


@register.filter(name='howlong', expects_localtime=True)
def filter_howlong(value):
    diff = timezone.localtime(timezone.now()) - value
    return pretty_time_delta(diff.total_seconds())
