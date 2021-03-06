import requests
from requests.exceptions import HTTPError
from django.conf import settings
from api.tasks import populatedb, populateanswers
from celery.result import AsyncResult
import json

class GetStackExchange:
    EP = 'https://api.stackexchange.com/2.2/{}'  # endpoint for Stackexchange API

    def get_all_questions(self, page, order="desc", sort="activity", site="stackoverflow"):
        param={
            "page": page,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('questions'), params=param)
            json_response = response.json()
            return response.json()
            response.raise_for_status()
        except Exception as err:
            print(f'Other error occurred: {err}')

    def search(self, page, tagged, order="desc", sort="activity", site="stackoverflow"):
        param={
            "tagged" : tagged,
            "page": page,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('search'), params=param)
            json_response = response.json()
            populatedb.delay(tagged,json_response)
            return response.json()
            response.raise_for_status()
        except Exception as err:
            print(f'Other error occurred: {err}')

    def advance_search(self, q, page, order="desc", sort="activity", site="stackoverflow"):
        param={
            "q": q,
            # "accepted" : accepted,
            # "answers" : answers,
            # "user" : user,
            # "tagged" : tagged,
            # "nottagged": nottagged,
            "page": page,
            # "pagesize": pagesize,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('search/advanced'), params=param)
            json_response = response.json()
            populatedb.delay(q,json_response)
            return response.json()
            response.raise_for_status()
        except Exception as err:
            print(f'Other error occurred: {err}')

    def answer_search(self,question_id, order="desc", sort="activity", site="stackoverflow"):
        param={
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('questions/'+str(question_id)+'/answers'), params=param)
            print(response.url)
            json_response = response.json()
            populateanswers.delay(question_id,json_response)
            return response.json()
            response.raise_for_status()
        except Exception as err:
            print(f'Other error occurred: {err}')

