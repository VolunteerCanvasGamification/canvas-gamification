from django.urls import path
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api.views import (
    QuestionViewSet,
    SampleMultipleChoiceQuestionViewSet,
    UserConsentViewSet,
    ContactUsViewSet,
    QuestionCategoryViewSet,
    UserStatsViewSet,
    UQJViewSet,
    ActionsViewSet,
    FAQViewSet,
    TokenValueViewSet,
    CourseViewSet,
    CanvasCourseRegistrationViewSet,
    ResetPasswordViewSet,
    UserRegistrationViewSet,
    UpdateProfileViewSet,
    SubmissionViewSet,
    ObtainAuthTokenView,
    MultipleChoiceQuestionViewSet,
    JavaQuestionViewSet,
    ParsonsQuestionViewSet,
    EventViewSet,
    TokenUseViewSet,
    DifficultyViewSet,
    ChangePasswordViewSet,
    UpdateUQJViewSet,
    QuestionReportViewSet,
)
from api.views.action import ExportActionViewSet

from api.views.admin import AdminViewSet
from api.views.analytics import AnalyticsViewSet
from api.views.course_admin import CourseAdminViewSet
from api.views.eventSet import EventSetViewSet
from api.views.goal import GoalViewSet, GoalItemViewSet
from api.views.page_view import PageViewViewSet, ExportPageViewViewSet
from api.views.survey import SurveyViewSet, ExportSurveyViewSet
from api.views.team import TeamViewSet
from api.views.user import ExportUserViewSet
from api.views.user_consent import ExportUserConsentViewSet

router = DefaultRouter()
router.register(r"questions", QuestionViewSet, basename="question")
router.register(
    r"sample-multiple-choice-question",
    SampleMultipleChoiceQuestionViewSet,
    basename="sample-multiple-choice-question",
)
router.register(
    r"multiple-choice-question",
    MultipleChoiceQuestionViewSet,
    basename="multiple-choice-question",
)
router.register(r"java-question", JavaQuestionViewSet, basename="java-question")
router.register(r"parsons-question", ParsonsQuestionViewSet, basename="parsons-question")
router.register(r"user-consent", UserConsentViewSet, basename="user-consent")
router.register(r"contact-us", ContactUsViewSet, basename="contact-us")
router.register(
    r"question-category",
    QuestionCategoryViewSet,
    basename="question-category",
)
router.register(r"token-values", TokenValueViewSet, basename="token-values")
router.register(r"user-stats", UserStatsViewSet, basename="user-stats")
router.register(r"user-actions", ActionsViewSet, basename="user-actions")
router.register(r"uqj", UQJViewSet, basename="uqj")
router.register(r"faq", FAQViewSet, basename="faq")
router.register(r"course", CourseViewSet, basename="course")
router.register(
    r"course-registration",
    CanvasCourseRegistrationViewSet,
    basename="course-registration",
)
router.register(r"change-password", ChangePasswordViewSet, basename="change-password")
router.register(r"reset-password", ResetPasswordViewSet, basename="reset-password")
router.register(r"register", UserRegistrationViewSet, basename="register")
router.register(r"update-profile", UpdateProfileViewSet, basename="update-profile")
router.register(r"submission", SubmissionViewSet, basename="submission")
router.register(r"event", EventViewSet, basename="event")
router.register(r"token-use", TokenUseViewSet, basename="token-use")
router.register(r"difficulty", DifficultyViewSet, basename="difficulty")
router.register(r"admin", AdminViewSet, basename="admin")
router.register(r"course-admin", CourseAdminViewSet, basename="admin-course")
router.register(r"uqj-update", UpdateUQJViewSet, basename="uqj-update")
router.register(r"question-report", QuestionReportViewSet, basename="question-report")
# router.register(r"analytics", AnalyticsViewSet, basename="analytics")
router.register(r"team", TeamViewSet, basename="team")
router.register(r"goal", GoalViewSet, basename="goal")
router.register(r"goal-item", GoalItemViewSet, basename="goal-item")
router.register(r"page-view", PageViewViewSet, basename="page-view")
router.register(r"survey", SurveyViewSet, basename="survey")
router.register(r"export/page-view", ExportPageViewViewSet, basename="export-page-view")
router.register(r"export/action", ExportActionViewSet, basename="export-action")
router.register(r"event-set", EventSetViewSet, basename="event-set-view")
router.register(r"export/consent", ExportUserConsentViewSet, basename="export-consent")
router.register(r"export/user", ExportUserViewSet, basename="export-user")
router.register(r"export/survey", ExportSurveyViewSet, basename="export-survey")

app_name = "api"
urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Canvas Gamification API",
            description="All the available APIs",
            version="1.0.0",
            public=True,
            permission_classes=(permissions.AllowAny,),
        ),
        name="openapi-schema",
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="api/docs.html",
            extra_context={"schema_url": "api:openapi-schema"},
        ),
        name="docs",
    ),
    path("api-token-auth/", ObtainAuthTokenView.as_view(), name="token-auth"),
] + router.urls
