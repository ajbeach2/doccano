from django.conf import settings

def get_projet_admin_role():
    return getattr(settings, 'ROLE_PROJECT_ADMIN', 'project_admin')

def get_annotator_role():
    return getattr(settings, 'ROLE_ANNOTATOR', 'annotator')

def get_annotation_approver_role():
    return getattr(settings, 'ROLE_ANNOTATION_APPROVER', 'annotation_approver')