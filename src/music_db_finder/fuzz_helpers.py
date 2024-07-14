# Import statements
import discogs_client as DiscogsClient
from rapidfuzz import fuzz as r_fuzz

def get_discogs_name(object):
    if type(object) == DiscogsClient.models.Artist:
        name = object.name
    elif type(object) in [DiscogsClient.models.Master, DiscogsClient.models.Release]:
        name = object.title
        if object.data['artist'] + ' - ' in name:
            name = name.split(' - ')[1]
    return name
    # return getattr(object, 'name', getattr(getattr(object, 'master', getattr(object, 'main_release', None)), 'title', 'none'))

def get_discogs_name_as_str(object):
    # if type(object) == DiscogsClient.models.Artist:
    #     object = object.name
    # elif type(object) in [DiscogsClient.models.Master, DiscogsClient.models.Release]:
    #     object = object.title
    # return object.lower()
    if type(object) == str:
        return object.lower()
    else:
        return get_discogs_name(object).lower()


def obj_ratio(a, b, scorer=r_fuzz.token_sort_ratio, *args, **kwargs):
    # print(type(a))
    # print(type(b))
    a = get_discogs_name_as_str(a)
    b = get_discogs_name_as_str(b)
    return scorer(a, b, *args, **kwargs)