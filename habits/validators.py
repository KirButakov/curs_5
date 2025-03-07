from rest_framework import serializers


def validate_habit_fields(data):
    if data.get("related_habit") and data.get("reward"):
        raise serializers.ValidationError(
            "You can't set both related habit and reward."
        )
    if data.get("is_pleasant") and (data.get("reward") or data.get("related_habit")):
        raise serializers.ValidationError(
            "Pleasant habits can't have rewards or related habits."
        )
    if data.get("duration") > 120:
        raise serializers.ValidationError("Duration should not exceed 120 seconds.")
    return data
