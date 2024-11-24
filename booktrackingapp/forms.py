from django import forms
from .models import JournalEntry

class EntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['journal_entry']
        widgets = {
            'journal_entry': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }