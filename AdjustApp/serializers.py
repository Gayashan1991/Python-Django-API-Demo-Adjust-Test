from django.db.models import fields
from rest_framework import serializers
from AdjustApp.models import Metric

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue')