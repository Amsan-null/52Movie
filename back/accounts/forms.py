from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        User = get_user_model()
        # https://docs.djangoproject.com/ko/4.2/ref/contrib/auth/#user-model
        fields = ('first_name', 'last_name', 'email')
        # 패스워드 창이 정상적으로 뜬다면 UserChangeForm이 아니라 UserCreationForm을 상속 받은 것

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()