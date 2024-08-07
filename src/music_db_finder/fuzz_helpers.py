# Import statements
import discogs_client as DiscogsClient
from rapidfuzz import fuzz as r_fuzz


def get_discogs_name(object):
    if type(object) is DiscogsClient.models.Artist:
        name = object.name
    elif type(object) in [DiscogsClient.models.Master, DiscogsClient.models.Release]:
        name = object.title
        if object.data["artist"] + " - " in name:
            name = name.split(" - ")[1]
    else:
        raise TypeError('Object not Discogs type')
    return name


def get_name_as_str(object):
    if type(object) is str:
        return object.lower()
    elif type(object) is dict:
        return object.get('name', object.get('artist', object.get('title'))).lower()
    elif getattr(object, '__module__') == 'discogs_client.models':
        return get_discogs_name(object).lower()
    else:
        raise TypeError('Unknown object type.')


def obj_ratio(a, b, scorer=r_fuzz.token_sort_ratio, *args, **kwargs):
    a = get_name_as_str(a)
    b = get_name_as_str(b)
    return scorer(a, b, *args, **kwargs)
