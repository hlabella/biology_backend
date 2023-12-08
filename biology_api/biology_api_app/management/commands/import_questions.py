from django.core.management.base import BaseCommand
from biology_api_app.models import Question, Choice 
import json

class Command(BaseCommand):
    help = 'Import questions from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to JSON file with questions')

    def handle(self, *args, **kwargs):

        # Clear existing questions
        Question.objects.all().delete()
    
        json_file_path = kwargs['json_file']
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for entry in data:
                
                # Sometimes 'resposta' can be null, so we don't insert
                if not entry.get('resposta'):
                    continue

                # Extract the correct answer label
                correct_answer_label = entry['resposta'].split(': ')[1].strip()

                # Create question instance
                question = Question.objects.create(
                    id=entry['_id']['$oid'],
                    text=entry['texto'],
                    focos=entry['focos'],
                    image=entry['imagem'],
                    video_resolution=entry['video_resolucao'],
                    discipline=entry['disciplina'],
                    thematic=entry['tematica']
                )

                 # Create choices
                for index, choice_text in enumerate(entry['alternativas']):
                    is_correct = chr(65 + index) == correct_answer_label

                    Choice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=is_correct
                    )

            self.stdout.write(self.style.SUCCESS('Successfully imported questions'))
