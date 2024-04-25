import datetime
import requests


def fetch_age_from_agify(name: str) -> tuple:
    """
    Fetch age information from Agify API based on the provided name.

    :param name: The name of the person.
    :return: Tuple containing age and date of birth. If age is not available or not an integer, return None.
    """

    # Make request to Agify API
    url = "https://api.agify.io"
    params = {"name": name}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            response_data = response.json()
            age = response_data.get("age")
            if age is not None and isinstance(age, int):
                current_year = datetime.datetime.now().year
                date_of_birth = current_year - age
                return age, date_of_birth
            else:
                # Age not available or not an integer
                return None, None
        else:
            # Agify API failed
            return None, None
    except Exception:
        # Issue with request
        return None, None
