from rest_framework import serializers

from api.serializers.event import EventSerializer
from course.models.models import MultipleChoiceQuestion, MultipleChoiceSubmission


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ['id', 'title', 'text', 'answer', 'max_submission_allowed', 'time_created', 'time_modified', 'author',
                  'category', 'difficulty', 'is_verified', 'variables', 'choices', 'visible_distractor_count',
                  'token_value', 'success_rate', 'type_name', 'event', 'is_sample', 'category_name',
                  'parent_category_name', 'course_name', 'event_name', 'author_name', ]

    event = EventSerializer()
    choices = serializers.JSONField()


class MultipleChoiceSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceSubmission
        fields = ['pk', 'submission_time', 'answer', 'grade', 'is_correct', 'is_partially_correct', 'finalized',
                  'status', 'tokens_received', 'token_value']
