class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    if user not in group.users and group.groups==[]:
        return False
    if user not in group.users and group.groups!=[]:
        for group_ in group.groups:
            result=is_user_in_group(user, group_)
            if result==True:
                return True
        return False

#Test
#1 Udacity provided test
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print('Test1')
print('Is user {} in group {}? {}'.format('sub_child_user',parent.name, is_user_in_group('sub_child_user', parent)))    # Should return True
print('Is user {} in group {}? {}'.format('sub_child_user',child.name, is_user_in_group('sub_child_user', child)))    # Should return True
print('Is user {} in group {}? {}'.format('sub_child_user',sub_child.name, is_user_in_group('sub_child_user', sub_child)))    # Should return True
print('Test1 done.')
print('--------------------------------------------------------------------------------------------------------------')

#2. Empty or not found in the froup
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

parent.add_group(child)
print('Test2')
print('Is user {} in group {}? {}'.format('sub_child_user',parent.name, is_user_in_group('sub_child_user', parent)))    # Should return False
print('Is user {} in group {}? {}'.format('sub_child_user',child.name, is_user_in_group('sub_child_user', child)))    # Should return False
print('Is user {} in group {}? {}'.format('sub_child_user',sub_child.name, is_user_in_group('sub_child_user', sub_child)))    # Should return True
print('Test2 done.')
print('--------------------------------------------------------------------------------------------------------------')

#3
Empty = Group("empty")
User = "user"
print('Test3')
print('Is user {} in group {}? {}'.format('user',Empty.name, is_user_in_group('user', Empty)))    # Should return False
print('Test3 done.')
print('--------------------------------------------------------------------------------------------------------------')
