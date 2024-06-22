# Import statements
import discogs_client as DiscogsClient
from rapidfuzz import fuzz as r_fuzz


def get_discogs_name(object):
    if type(object) == DiscogsClient.models.Artist:
        object = object.name
    elif type(object) in [DiscogsClient.models.Master, DiscogsClient.models.Release]:
        object = object.title
    return object.lower()


def obj_ratio(a, b, scorer=r_fuzz.token_sort_ratio, *args, **kwargs):
    # print(type(a))
    # print(type(b))
    a = get_discogs_name(a)
    b = get_discogs_name(b)
    return scorer(a, b, *args, **kwargs)