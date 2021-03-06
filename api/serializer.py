from rest_framework import serializers

from tracker.models import RawTracker, BeatTracker


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawTracker
        fields = (
            'url',
            'referrer',
            'dnt',
            'account_id',
            'screen_width',
            'screen_height'
        )


class BeatSerializer(serializers.Serializer):
    secret_id = serializers.UUIDField(required=True)