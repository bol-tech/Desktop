
class student():
    def _init_(self, n=  '', m =0 ):
        self.name = n
        self.marks = m
        def display(self):
            print('Hi', self.name)
            print('your marks', self.marks)
            def calculate(self):
         if(self.marks>=90): 
         print('you are now qualified in first slot selection,congratulations! you did well in the interview:')
        elif(self.marks>=80):
            print('you qualified in second slot selection,congratulations!') 
            elif(self.marks>=70):
print('you are qualified in third slot selection,Better!')  
 else
 print('no more slot for this results,sorry!')         
 n = int(input('how many students?'))
 i=0


 while(i<n):
     name = input('enter name:')     
     marks = int(input('enter the marks:'))  
     s = (name, marks)
     s.display()
     s.calculate()
     i+=1
     print('..........................................................................................................')

