from django.db import IntegrityError
from rest_framework.exceptions import ValidationError


class UpdateIntegrityCheck:
    def perform_update(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise ValidationError
