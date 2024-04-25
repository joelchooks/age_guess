from django.core.cache import cache

from .utils import fetch_age_from_agify


def get_cached_request_response(name: str) -> dict:
    """
    Retrieve cached response for the given name, if available or get new response.

    :param name: The name of the person.
    :return: Cached response if available, None otherwise.
    """

    cache_key = name
    response = cache.get(cache_key, None)
    if response is None:
        age, date_of_birth = fetch_age_from_agify(name=name)
        if date_of_birth:
            response = {
                "name": name,
                "age": age,
                "date_of_birth": date_of_birth,
            }
            # Cache the result with the cache key
            cache.set(cache_key, response)
        else:
            return {}

    return response
