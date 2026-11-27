class student :
    def accept(self,roll_no,name,mark):
        self.roll_no = roll_no
        self.name = name 
        self.mark = mark
        

    def display(self):
        print("roll no:",self.roll_no)
        print("name:",self.name)
        print("mark:",self.mark)

s1 = student()
s1.accept(101,"anu",85)

s2 = student()
s2.accept(102,"bala",92)

s3 = student()
s3.accept(103,"charan",78)

if s1.mark >= s2.mark and s1.mark >= s3.mark:
        s1.display()
elif s2.mark >= s1.mark and s2.mark >= s3.mark:
        s2.display()
else:
        s3.display()
    
    
