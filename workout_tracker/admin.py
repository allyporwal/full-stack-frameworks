from django.contrib import admin
from .models import WorkoutTracker

# Register your models here.


class WorkoutTrackerAdmin(admin.ModelAdmin):
    list_display = (
        'workout_id',
        'created_at',
        'session_name',
        'workout',
    )

    ordering = ('workout_id',)


admin.site.register(WorkoutTracker, WorkoutTrackerAdmin)
