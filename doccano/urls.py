from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from .views.server import IndexView
from .views.server import (
    ProjectView,
    DatasetView,
    DataUpload,
    LabelView,
    StatsView,
    GuidelineView,
    UsersView,
)
from .views.server import ProjectsView, DataDownload
from .views.server import (
    DemoTextClassification,
    DemoNamedEntityRecognition,
    DemoTranslation,
)

from .views.api import Me, Features, Users
from .views.api import ProjectList, ProjectDetail
from .views.api import LabelList, LabelDetail, ApproveLabelsAPI, LabelUploadAPI
from .views.api import DocumentList, DocumentDetail
from .views.api import AnnotationList, AnnotationDetail
from .views.api import TextUploadAPI, TextDownloadAPI
from .views.api import StatisticsAPI
from .views.api import RoleMappingList, RoleMappingDetail, Roles


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path(
        "projects/<int:project_id>/docs/download",
        DataDownload.as_view(),
        name="download",
    ),
    path("projects/<int:project_id>/", ProjectView.as_view(), name="annotation"),
    path("projects/<int:project_id>/docs/", DatasetView.as_view(), name="dataset"),
    path("projects/<int:project_id>/docs/create", DataUpload.as_view(), name="upload"),
    path(
        "projects/<int:project_id>/labels/",
        LabelView.as_view(),
        name="label-management",
    ),
    path("projects/<int:project_id>/stats/", StatsView.as_view(), name="stats"),
    path(
        "projects/<int:project_id>/guideline/",
        GuidelineView.as_view(),
        name="guideline",
    ),
    path("projects/<int:project_id>/users/", UsersView.as_view(), name="users"),
    path(
        "demo/text-classification/",
        DemoTextClassification.as_view(),
        name="demo-text-classification",
    ),
    path(
        "demo/named-entity-recognition/",
        DemoNamedEntityRecognition.as_view(),
        name="demo-named-entity-recognition",
    ),
    path("demo/translation/", DemoTranslation.as_view(), name="demo-translation"),
    # API paths
    path("v1/auth-token", obtain_auth_token),
    path("v1/me", Me.as_view(), name="me"),
    path("v1/features", Features.as_view(), name="features"),
    path("v1/projects", ProjectList.as_view(), name="project_list"),
    path("v1/users", Users.as_view(), name="user_list"),
    path("v1/roles", Roles.as_view(), name="roles"),
    path(
        "v1/projects/<int:project_id>", ProjectDetail.as_view(), name="project_detail"
    ),
    path(
        "v1/projects/<int:project_id>/statistics",
        StatisticsAPI.as_view(),
        name="statistics",
    ),
    path("v1/projects/<int:project_id>/labels", LabelList.as_view(), name="label_list"),
    path(
        "v1/projects/<int:project_id>/label-upload",
        LabelUploadAPI.as_view(),
        name="label_upload",
    ),
    path(
        "v1/projects/<int:project_id>/labels/<int:label_id>",
        LabelDetail.as_view(),
        name="label_detail",
    ),
    path("v1/projects/<int:project_id>/docs", DocumentList.as_view(), name="doc_list"),
    path(
        "v1/projects/<int:project_id>/docs/<int:doc_id>",
        DocumentDetail.as_view(),
        name="doc_detail",
    ),
    path(
        "v1/projects/<int:project_id>/docs/<int:doc_id>/approve-labels",
        ApproveLabelsAPI.as_view(),
        name="approve_labels",
    ),
    path(
        "v1/projects/<int:project_id>/docs/<int:doc_id>/annotations",
        AnnotationList.as_view(),
        name="annotation_list",
    ),
    path(
        "v1/projects/<int:project_id>/docs/<int:doc_id>/annotations/<int:annotation_id>",
        AnnotationDetail.as_view(),
        name="annotation_detail",
    ),
    path(
        "v1/projects/<int:project_id>/docs/upload",
        TextUploadAPI.as_view(),
        name="doc_uploader",
    ),
    path(
        "v1/projects/<int:project_id>/docs/download",
        TextDownloadAPI.as_view(),
        name="doc_downloader",
    ),
    path(
        "v1/projects/<int:project_id>/roles",
        RoleMappingList.as_view(),
        name="rolemapping_list",
    ),
    path(
        "v1/projects/<int:project_id>/roles/<int:rolemapping_id>",
        RoleMappingDetail.as_view(),
        name="rolemapping_detail",
    ),
]
