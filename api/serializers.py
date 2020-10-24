from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists
from rest_framework import serializers
from api.models import User, Branch
from api.db_utils import get_branch

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'full_name', 'status',
            'branch'
        ]
        extra_kwargs = {
            'status': {'read_only': True},
            'username': {'read_only': True},
        }
    
    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        branch = validated_data.get('branch', instance.branch)
        if branch:
            instance.branch = branch
        instance.save()
        return instance

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    full_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    branch = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Branch.objects.all(), 
    )

    class Meta:
        model = User
        fields = ['username', 'full_name',
        'password1', 'password2', 'branch']
        extra_kwargs = {
            'password1': {
                'write_only':True
            }
        }

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'full_name': self.validated_data.get('full_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'username': self.validated_data.get('username', ''),
            'branch': self.validated_data.get('branch', ''),
        }

    def save(self, request):
        # if request.user.is_authenticated and request.user.is_librarian:
        # else:
        #     raise serializers.ValidationError("You don't have permissions")
        if request.user.is_authenticated:
            if not request.user.is_librarian:
                raise serializers.ValidationError({"error":"You don't have permissions"})
            adapter = get_adapter()
            user = adapter.new_user(request)
            self.cleaned_data = self.get_cleaned_data()
            if adapter.save_user(request, user, self) is None:
                raise serializers.ValidationError({"error":"Branch does not exisit"})
            user.save()
            return user
        