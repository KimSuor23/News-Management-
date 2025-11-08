from django import forms
from .models import News


# form for adding or editing news
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'category', 'source', 'published_date', 'content']

    # check if title is not empty
    def clean_title(self):
        try:
            title = self.cleaned_data.get('title')
            if not title or title.strip() == "":
                raise forms.ValidationError("title must not be empty")
            return title
        except Exception:
            # handle any unknown error with simple message
            raise forms.ValidationError("error while checking title")
