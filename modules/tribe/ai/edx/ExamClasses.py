class Name(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def find_printed_name(self):
        return self.first_name+" "+self.last_name
    def find_sortable_name(self):
        return self.last_name + ", " + self.first_name[0]

class FullName(Name):
    def __init__(self, first_name, middle_name, last_name):
        super().__init__(first_name, last_name)
        self.middle_name = middle_name
    def find_printed_name(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name
    def find_sortable_name(self):
        return Name.find_sortable_name(self)

class Meeting(object):
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
