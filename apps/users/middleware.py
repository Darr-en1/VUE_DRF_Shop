import requests
from django.utils.deprecation import MiddlewareMixin

__author__ = 'Darr_en1'

class StackOverflowMiddleware(MiddlewareMixin):

    def process_exception(self,request,exception):

        intitle = f'{exception.__class__.__name__}: {exception.args[0]}'

        url = 'https://api.stackexchange.com/2.2/search'
        headers = {'User-Agent': 'github.com/vitorfs/seot'}
        params = {
            'order': 'desc',
            'sort': 'votes',
            'site': 'stackoverflow',
            'pagesize': 3,
            'tagged': 'python;django',
            'intitle': intitle
        }

        r = requests.get(url, params=params, headers=headers)
        questions = r.json()

        print('')

        for question in questions['items']:
            print(question['title'])
            print(question['link'])

            print('')



