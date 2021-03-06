from django import forms
from .models import Question,Choice,Image

class VoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question')
        super(VoteForm, self).__init__(*args, **kwargs)
        CHOICES = [(ch.id, ch.choice_text) for ch in self.question.choice_set.all()]
        self.fields['面白さ'] = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect())

    def save(self):
        choice_id = self.cleaned_data.get('面白さ')
        selected_choice = Choice.objects.get(pk=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture', 'title']

   
