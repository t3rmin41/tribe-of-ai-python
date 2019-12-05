class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def find_printed_name(self):
        return self.first_name+" "+self.last_name
    def find_sortable_name(self):
        return self.last_name + ", " + self.first_name[0]

from datetime import datetime
class Meeting:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
