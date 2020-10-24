from api.models import Branch

def get_branch(branch_id):
    if branch_id:
        branches = Branch.objects.filter(id=branch_id)
        if len(branches) == 0:
            return None
        return branches[0]