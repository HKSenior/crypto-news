from datetime import datetime

from django.template import Library
from django.utils import timezone

register = Library()


@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)


def pretty_time_delta(seconds):
    seconds = abs(int(seconds))
    weeks, seconds = divmod(seconds, 604800)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if weeks > 0:
        return "{w} weeks {d} days".format(w=weeks, d=days)
    if days > 0:
        return "{d} days {h} hours".format(d=days, h=hours)
    elif hours > 0:
        return "{h} hours {m} minutes".format(h=hours, m=minutes)
    elif minutes > 0:
        return "{m} minutes {s} seconds".format(m=minutes, s=seconds)
    else:
        return "{s} seconds".foramt(s=seconds)


@register.filter(name='howlong')
def filter_howlong(value):
    now = timezone.localtime(timezone.now())
    past = timezone.make_aware(
        datetime.strptime(str(value).split('.')[0], "%Y-%m-%d %H:%M:%S"))
    diff = now - past
    return pretty_time_delta(diff.total_seconds())
