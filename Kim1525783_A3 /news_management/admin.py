from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Category, News
from .forms import NewsForm

# admin for categories - simple list and search
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# admin for news with validation on save
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsForm  # custom form for validation

    list_display = ('title', 'published_date', 'source', 'category')
    list_filter = ('category', 'published_date')
    search_fields = ('title', 'source')
    ordering = ('-published_date',)

    # check title isn't blank before saving
    def save_model(self, request, obj, form, change):
        try:
            if not obj.title.strip():
                raise ValidationError("title cannot be blank")
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            # show validation error message in admin
            self.message_user(request, f"error: {e}", level='error')
        except Exception:
            # catch other unknown errors
            self.message_user(request, "something went wrong when saving", level='error')
