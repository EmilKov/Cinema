from django import forms
from .models import Profile
# class ImageUploadForm(forms.Form):
#     """Image upload form."""
    # image = forms.ImageField()

# class ProfilePicForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields=['image']
# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image')
#     class Meta:
#         model = Images
#         fields = ('image', )
# class ImageForm(forms.ModelForm):
#     class Meta:
#         model= Profile
#         fields= [ "image"]


# class PostForm(forms.ModelForm):
#     photo = forms.ImageField(label='')
#
#     class Meta:
#         model = Profile
#         fields = ('photo',)

from .models import Comment_movie


class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment_movie
        fields=('text',)
