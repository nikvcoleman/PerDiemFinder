import tkinter as tk
import requests
import sys
import bs4


def get_info():
    conus_url = ("https://www.gsa.gov/travel/plan-book/per-diem-rates/per-diem-rates-lookup/?action=perdiems_report&fis\
cal_year=2019&city=&state=&zip=" + user_input1.get())
    webpage = requests.get(conus_url)
    soup = bs4.BeautifulSoup(webpage.content, "html.parser")
    rate_find = soup.find("td", headers="MIE").get_text()
    first_last = soup.find("td", headers="firstLast").get_text()
    print("\nPer diem rate for first and last day of travel is: " + first_last)
    print("The rate according to the zip code is: " + rate_find + " per day. ")
    print("PLEASE DOUBLE CHECK THIS LINK TO CONFIRM THIS INFORMATION IS CORRECT:\n" + conus_url)
    print("Total reimbursement should be:" + rate_find.replace("$","" )*int(user_input2.get()))


def exit():
    sys.exit()


root = tk.Tk()

root.title('Perdy GUI')
root.geometry('500x500')
hotel_zip = tk.Label(root, text="Hotel zipcode")
hotel_zip.grid(column=0, row=0)
user_input1 = tk.Entry()
user_input1.grid(column=1, row=0)
len_of_stay = tk.Label(root, text="How many days will you be staying?")
len_of_stay.grid(column=0, row=2)
user_input2 = tk.Entry()
user_input2.grid(column=1, row=2)
button1 = tk.Button(root, text="Enter", command=get_info)
button1.grid(column=2, row=4)
exit_butt = tk.Button(root, text="EXIT", command=exit)
exit_butt.grid(column=0, row=4)
root.mainloop()
