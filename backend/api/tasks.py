from celery.decorators import task
from celery.utils.log import get_task_logger
from django.contrib.gis.geos import Point
from django.db.models import *
from api.models import Questions, Answers
logger = get_task_logger(__name__)


@task(name="populatedb")
def populatedb(query, apidata):
	if Questions.objects.filter(query=query).exists()==False:
		ques_db=Questions.objects.create(query=query, data=apidata)
		ques_db.save()
	logger.info("created")

@task(name="populateanswers")
def populateanswers(question_id, apidata):
	if Answers.objects.filter(question_id=question_id).exists()==False:
		ans_db=Answers.objects.create(question_id=question_id, data=apidata)
		ans_db.save()
	logger.info("created")
