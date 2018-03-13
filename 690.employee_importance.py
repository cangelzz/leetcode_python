class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emap = {e.id: e for e in employees}
        employee = emap[id]
        importance = employee.importance
        for sub in employee.subordinates:
            importance += self.getImportance(employees, sub)

        return importance
