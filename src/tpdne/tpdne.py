import base64

import requests

from tpdne import __version__


def _request_person(*r_args, **r_kwargs) -> 'requests.Request':
    """Request a new person that doesn't exist

    Args:
        None

    Returns:
        request object
    """

    return requests.get(
        *r_args,
        url="https://thispersondoesnotexist.com/image",
        stream=True,
        headers={
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'tpdne/{}'.format(__version__)
        },
        **r_kwargs
    )

def tpdne_base64() -> 'str':
    """Get a person that doesn't exist in a base64-encoded image

    Args:
        None
    
    Return:
        base64 string
    """

    r = _request_person()
    return base64.encodebytes(r.content)
