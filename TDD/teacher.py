
class Teacher:
    def __init__(self,name,years_exp,master_degree= False,topics=[]):
        self.name = name
        self.years_exp = years_exp
        self.master_degree = master_degree
        self.topics = topics

    @property
    def has_master_degree(self):
        return self.master_degree
    @property
    def amount_topics(self):
        return len(self.topics)