from django.test import TestCase, Client
from .models import Question, Choice
from django.test import TestCase, Client
from django.urls import reverse
from .models import Question, Choice

# Create your tests here.


# testando GET /questions
class QuestionViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        # Create some dummy questions
        for i in range(10):
            Question.objects.create(id = i, text=f"Sample Question {i+1}", focos = [])

    #test response
    def test_response_format(self):
        response = self.client.get(reverse('get_questions'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')


    #test randomness with two calls        
    def test_randomness_of_questions(self):
        first_call = self.client.get(reverse('get_questions')).json()
        second_call = self.client.get(reverse('get_questions')).json()

        self.assertNotEqual(first_call, second_call, "Two calls returned the same set of questions")

    #test what happens with an empty database   
    def test_empty_database(self):
        
        Question.objects.all().delete()
        response = self.client.get(reverse('get_questions'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
 
        self.assertEqual(len(data), len('[]'), "Response should be empty when no questions are available")






# testando POST /answer

class AnswerViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        
        # Create a test question and choices
        question = Question.objects.create(id = 1, text=f"Sample Question 1", focos = [])
        Choice.objects.create(question=question, text="Choice 1", is_correct=False)
        Choice.objects.create(question=question, text="Choice 2", is_correct=False)
        Choice.objects.create(question=question, text="Choice 3", is_correct=False)
        Choice.objects.create(question=question, text="Choice 4", is_correct=False)
        self.correct_choice = Choice.objects.create(question=question, text="Choice 5", is_correct=True)

    # check feedback when answer is correct
    def test_submit_answer_correct(self):

        # Simulate a correct answer submission
        data = {
            'question_id': self.correct_choice.question.id,
            'submitted_answer': self.correct_choice.text
        }
        response = self.client.post(reverse('submit_answer'), data, content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data['is_correct'])
        self.assertEqual(response_data['resposta'], self.correct_choice.text)

    #check feedback if answer is wrong
    def test_submit_answer_incorrect(self):

        # Simulate an incorrect answer submission
        data = {
            'question_id': self.correct_choice.question.id,
            'submitted_answer': "Incorrect Answer"
        }
        response = self.client.post(reverse('submit_answer'), data, content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertFalse(response_data['is_correct'])
        self.assertEqual(response_data['resposta'], self.correct_choice.text)
