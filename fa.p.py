class student:
    def _init__(self,): #default  constructor
        self.marks=marks
        self._marks=marks #private
    def getter(self):
        return self.marks
    def setter(self,marks):
        self.marks=marks
    s1=student(79)
     #set the data:
    s1.setter(79)
     #get the data
    ans=s1.getter()
    print(ans)
