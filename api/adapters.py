from allauth.account.adapter import DefaultAccountAdapter
from api.models import Branch
from api.db_utils import get_branch


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """

        user = super().save_user(request, user, form, False)

        user.full_name = request.data.get('full_name', '')
        user.username = request.data.get('username', '')
        
        branch = get_branch(request.data.get('branch', '')) 
        if branch is None:
            return None
        user.branch = branch
            
        user.save()
        return user
    

    def respond_email_verification_sent(self, request, user):
        pass