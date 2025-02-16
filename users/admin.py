from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "velog_uuid",
        "email",
        "group_id",
        "is_active",
        "created_at",
    ]

    empty_value_display = "-"
    ordering = ["-created_at"]

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        list_display_labels = {  # noqa
            "velog_uuid": "Velog UUID",
            "email": "이메일",
            "group_id": "그룹 ID",
            "is_active": "활성화 여부",
            "created_at": "생성일",
        }
        return list_display
