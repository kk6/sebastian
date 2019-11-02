from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm as UserChangeBaseForm
from django.contrib.auth.forms import UserCreationForm as UserCreationBaseForm


class UserCreationForm(UserCreationBaseForm):
    """ユーザー作成フォーム"""

    class Meta:
        model = get_user_model()
        fields = ("name", "username", "email")


class UserChangeForm(UserChangeBaseForm):
    """ユーザー編集フォーム"""

    class Meta:
        model = get_user_model()
        fields = ("name", "username", "email")
