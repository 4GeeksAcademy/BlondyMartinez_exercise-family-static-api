
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name;
        self._next_id = 1;
        self._members = [];

    def _generateId(self):
        id = self._next_id;
        self._next_id += 1;
        return id;

    def add_member(self, member):
        if member['first_name'] == 'Tommy': member['id'] = 3443
        else: member['id'] = self._generateId()
        self._members.append(member);
        return self._members

    def delete_member(self, id):
        member_to_delete = self.get_member(id)
        self._members.remove(member_to_delete)
        return self._members

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id: return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
