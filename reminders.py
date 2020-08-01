from tkinter import *


 
objectList = []
#will create an reminder object
class reminder:
    def __init__(self, title, day,  month, year, time, importance):
        self.title = title
        self.day = day
        self.month = month
        self.year = year
        self.time = time
        self.importance = importance
    
    def __str__(self):
        return self.title + ": " + self.day + " - " + self.month + " - " + self.year + " - " + self.time
    
#will sort the reminders based on importance
def bubbleSort(): 
    n = len(objectList) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if objectList[j].importance < objectList[j+1].importance: 
                objectList[j], objectList[j+1] = objectList[j+1], objectList[j]

#will create an object and then add it to an list
def addobject():
    object1 = reminder(title_entry.get(), day_entry.get(), month_entry.get(), year_entry.get(), time_entry.get(), importance_entry.get())
    objectList.append(object1)
    displayReminders()

#displays the reminders once they are added
def displayReminders():
    all_reminders.delete(0, END)
    bubbleSort()
    for x in objectList:
        #add objects to the Listbox
        all_reminders.insert(END, x.title)
    


#root object
root = Tk()

#creating listbox in order to display the reminders once you add them

#creating a frame in order to add the widgets on top of it
frame = Frame(root)
frame.place(relx= 0.3, rely= 0.1, relwidth=10, relheight=10)

#ADDING THE WIDGETS

#title
title_label = Label(frame, text= "title")
title_entry = Entry(frame)
title_label.grid(row= 0, column= 0)
title_entry.grid(row= 0, column= 1)

#day
day_label = Label(frame, text= 'Day(M, T, W, Th, F, Sat, Sun)')
day_entry = Entry(frame)
day_label.grid(row= 1, column= 0)
day_entry.grid(row= 1, column= 1)

#month
month_label = Label(frame, text= 'Month(Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sept, Oct, Nov, Dec)')
month_entry = Entry(frame)
month_label.grid(row= 2, column= 0)
month_entry.grid(row= 2, column= 1)

#year
year_label = Label(frame, text= 'Year(must be 4 digit number)')
year_entry = Entry(frame)
year_label.grid(row = 3, column= 0)
year_entry.grid(row= 3, column= 1)

#time
time_label = Label(frame, text= 'Time(Hour:Minute)')
time_entry = Entry(frame)
time_label.grid(row= 4, column= 0)
time_entry.grid(row= 4, column= 1)

#importance
importance_label = Label(frame, text= 'Importance(rate 1, 2, or 3')
importance_entry = Entry(frame)
importance_label.grid(row= 5, column= 0)
importance_entry.grid(row= 5, column= 1)

#enter button
enter_button = Button(frame, text= "enter information", command= lambda: addobject())
enter_button.grid(row= 6, column= 1)

#lisbox to display all the reminders
all_reminders = Listbox(frame)
all_reminders.grid(row= 7, column= 1)



root.mainloop()