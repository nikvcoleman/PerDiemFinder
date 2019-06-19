#!/usr/bin/env python3
# Per Diem Finder written by Nikolas Coleman
# For Indyne inc. overseas and CONUS Per Diem rates

import requests
import bs4
import sys


def main():
    print("Welcome to Per Diem Finder\nThis program was written by: Nikolas Coleman\n")
    here_or_there = input("Please select the option that applies to you.\n1. I am looking at rates INSIDE the CONUS\n\
2. I am looking at rates OUTSIDE of the CONUS\n(1|2): ")
    if here_or_there == str(1):
        conus_hotel_zipcode = input("What is the zip code of the hotel you are staying at?: ")
        # automate this to get the files from gsa.gov and save them later once we find out how
        conus_url = ("https://www.gsa.gov/travel/plan-book/per-diem-rates/per-diem-rates-lookup/?action=perdiems_report\
&fiscal_year=2019&city=&state=&zip=" + conus_hotel_zipcode)

        if len(conus_hotel_zipcode) > 5:
            print("Zip code entered is too long. Please limit the zip code to 4 digits please.")
        elif len(conus_hotel_zipcode) == 5:
            try:
                webpage = requests.get(conus_url)
                soup = bs4.BeautifulSoup(webpage.content, "html.parser")
                rate_find = soup.find("td", headers="MIE").get_text()
                first_last = soup.find("td", headers="firstLast").get_text()
                print("Per diem rate for first and last day of travel is: " + first_last)
                print("The rate according to the zip code is: " + rate_find + " per day. ")
                print("PLEASE DOUBLE CHECK THIS LINK TO CONFIRM THIS INFORMATION IS CORRECT:\n" + conus_url)
            except AttributeError as f_up1:
                print("Attribute Error. That's all I know.")
                attribute_er = input("Would you like more technical information as to why this happened?(y|n): ")
                if attribute_er.lower() == "y":
                    print(f_up1)
                else:
                    print("Goodbye.")
                sys.exit()
            except requests.exceptions.ConnectionError as f_up2:
                print("Unable to connect due to connection error. Please check network connection.")
                connect_er = input("Would you like more technical information as to why this happened?(y|n): ")
                if connect_er.lower() == "y":
                    print(f_up2)
                else:
                    print("Goodbye.")
                sys.exit()
            except requests.exceptions.HTTPError as f_up3:
                print("Invalid http response.")
                http_er = input("Would you like more technical information as to why this happened?(y|n): ")
                if http_er.lower() == "y":
                    print(f_up3)
                else:
                    print("Goodbye.")
                sys.exit()
            except requests.exceptions.Timeout as f_up4:
                print("Request timed out. Goodbye!")
                time_er = input("Would you like more technical information as to why this happened?(y|n): ")
                if time_er.lower() == "y":
                    print(f_up4)
                else:
                    print("Goodbye.")
                sys.exit()
    elif here_or_there == str(2):
        print("OPTION NOT HERE YET")
    else:
        print("Please type either '1' or '2'")
# OVERSEAS DATA https://aoprals.state.gov/web920/per_diem_action.asp?MenuHide=1&CountryCode=0000


if __name__ == '__main__':
    main()
