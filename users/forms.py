from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


# Create your forms here.

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','last_name','first_name','email', 'password1', 'password2']


class UserForms(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ['username','last_name','first_name','email']  


	

	