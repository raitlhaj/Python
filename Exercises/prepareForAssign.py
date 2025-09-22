
class PrepareForAssign:
    def __init__(self, value):
        self.value = value

    def prepare(self):
        # Example preparation logic
        return str(self.value).strip().lower()
    
    def is_polyndrome(self):
        prepared_value = self.prepare()
        return prepared_value == prepared_value[::-1]

    def avreage(slef, numbers):
        return sum(numbers) / len(numbers) if numbers else 0
    
    
 