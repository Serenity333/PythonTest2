from tkinter import *

root = Tk()

pic = Text(root, height = 30, width = 30)
photo = PhotoImage(file='./photos/img425.jpg')
pic.insert(END,'\n')
pic.image_create(END, image=photo)

pic.pack(side=LEFT)

cat1 = Text(root, height=30, width = 30)
scroll = Scrollbar(root, command=cat1.yview)
cat1.configure(yscrollcommand=scroll.set)
cat1.tag_configure(font=('Courier', 14, 'bold'))
cat1.tag_configure('big', font=('Verdana', 15, 'bold'))
cat1.tag_configure('color', foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))

cat1.tag_bind('follow', '<1>', lambda e, t=cat1: t.insert(END, "Not now, maybe later!"))
cat1.insert(END, '\nHerbs\n', 'big')
quote = """
Name:
Alternate Names:
Native Regions:
Planetary Influences:
Deity Associations:
Tool Uses:
Health Attributes:
Energy Uses:
"""
cat1.insert(END, quote, 'color')
cat1.insert(END, 'follow-up\n', 'follow')
cat1.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
