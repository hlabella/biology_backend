from django.shortcuts import render
from django.http import JsonResponse
from .models import Question
from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import Question, Choice
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

#get questions view:

@csrf_exempt
@require_http_methods(["GET"])
def get_questions(request):
    NUMBER_OF_QUESTIONS = 5

    # Fetch random questions
    random_questions = Question.objects.order_by('?')[:NUMBER_OF_QUESTIONS]

    # Serialize the random questions
    serialized_questions = serializers.serialize('json', random_questions)

    return JsonResponse(serialized_questions, safe=False, content_type='application/json')

#post answer view:

@csrf_exempt
@require_http_methods(["POST"])
def submit_answer(request):
    try:
        data = json.loads(request.body)
        question_id = data['question_id']
        submitted_answer = data['submitted_answer']

        # Validate and process the answer
        question = Question.objects.get(id=question_id)
        correct_choice = question.choices.get(is_correct=True)

        is_correct = correct_choice.text == submitted_answer
        response_data = {
            'is_correct': is_correct,
            'resposta': correct_choice.text,
            'video_resolucao': question.video_resolution
        }
        return JsonResponse(response_data)
    except Question.DoesNotExist:
        return JsonResponse({'error': 'Question not found'}, status=404)
    except Choice.DoesNotExist:
        return JsonResponse({'error': 'Correct choice not found'}, status=404)
    except KeyError:
        return JsonResponse({'error': 'Invalid data'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

