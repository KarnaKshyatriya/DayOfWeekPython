def dayOfTheWeek(argument):
    switcher={
        0:"The day is Sunday",
        1:"The day is Monday",
        2:"The day is Tuesday",
        3:"The day is Wednesday",
        4:"The day is Thursday",
        5:"The day is Friday",
        6:"The day is  Suturday"
    }
    return switcher.get(argument,"Please enter a value from 0 to 6")

if __name__=="__main__":
    userVal=int(input("Please enter your week day choice \n in number :: "))
    print(dayOfTheWeek(userVal))

input('Please press enter to exit from console')

