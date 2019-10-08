""" a low memory graphql client """

from urequests import post
from const import url as defaultUrl
from const import token as defaultToken

def execute(query,variables=None,url=defaultUrl,token=defaultToken):
    """ executes a graphql query with optional variables """
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # insert a token
    if token:
        headers['Authorization'] = '{}'.format(token)

    # shrink the query
    query = query.replace(r'\n', ' ')
    query = query.replace(r'\t', ' ')

    while query != query.replace('  ', ' '):
        query = query.replace('  ', ' ')

    try:
        response = post(
            url,
            headers=headers,
            json=dict(query=query, variables=variables)
        )
    except OSError:
        return None
    else:
        return response.content.decode('utf-8')



    
