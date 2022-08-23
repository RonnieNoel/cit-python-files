#A simple grading calculator that uses if statement and comparision operators 

number=int(input("enter a number"))
if number>100:
     print("enter a correct percentage to get the grade")
elif number>=90:
      print("Excellent:A")
elif number>=80:
      print("Very Good:B")
elif number>=70:
      print("Good:D")
elif number>=60:
      print("Fair:E")
elif number>=0:
      print("You Failed:F")
elif number<0:
       print("enter a correct percentage to get the grade")