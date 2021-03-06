from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import generics
from .utils import GetStackExchange
from api.models import Questions, Answers
from api.serializers import QuestionSerializer


class All_questions_View(APIView):

	def get(self,request,*args,**kwargs):
		page=self.request.query_params.get("page")
		all_ques = GetStackExchange()
		all_ques = all_ques.get_all_questions(page)
		return Response(all_ques,status=status.HTTP_200_OK)

class Search_questions_View(APIView):

	def get(self,request,*args,**kwargs):
		page=self.request.query_params.get("page")
		all_ques = GetStackExchange()
		all_ques = all_ques.get_all_questions(page)
		return Response(all_ques,status=status.HTTP_200_OK)

class Query_ques_View(APIView):

	def get(self,request,*args,**kwargs):
		page = self.request.query_params.get("page")
		query = self.request.query_params.get("query")
		sort = self.request.query_params.get("sort")
		order = self.request.query_params.get("order")
		if(sort=="0"):
			sort="desc"
		if(order=="0"):
			order="activity"
		ques_qs = Questions.objects.filter(query=query)
		if ques_qs.exists():
			ques_object = ques_qs.first()
			serialized_data = QuestionSerializer(ques_object)
			data = serialized_data.data['data']
			return Response(data,status=status.HTTP_200_OK)
		query_ques_res = GetStackExchange()
		query_ques_res = query_ques_res.search(page,query,order,sort)
		return Response(query_ques_res,status=status.HTTP_200_OK)

class Advance_search_View(APIView):

	def get(self,request,*args,**kwargs):
		page=self.request.query_params.get("page")
		query=self.request.query_params.get("query")
		ques_qs = Questions.objects.filter(query=query)
		if ques_qs.exists():
			ques_object = ques_qs.first()
			serialized_data = QuestionSerializer(ques_object)
			data = serialized_data.data['data']
			return Response(data,status=status.HTTP_200_OK)
		adv_res = GetStackExchange()
		adv_res = adv_res.advance_search(query,page)
		return Response(adv_res,status=status.HTTP_200_OK)

class Detail_View(APIView):
	def get(self,request,*args,**kwargs):
		ques_id = self.request.query_params.get("quesid",None)
		
		if ques_id is None:
			return Response({"error":"Question Id is required"},status=400)

		ans_qs = Answers.objects.filter(question_id=ques_id)
		if ans_qs.exists():
			ans_object = ans_qs.first()
			serialized_data = AnswerSerializer(ques_object)
			data = serialized_data.data['data']
			return Response(data,status=status.HTTP_200_OK)

		ans_res = GetStackExchange()
		ans_res = ans_res.answer_search(ques_id)
		return Response(ans_res,status=status.HTTP_200_OK)

