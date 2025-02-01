#Match-case/switch-case Statement -> An alternative to use many elif statement
#                                   execute some code if a value matches a case
#                                   Benefits:cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case "sunday":
            return "It is sunday"
        case "monday":
            return "It is monday"
        case "tuesday":
            return "It is tuesday"
        case "wednesday":
            return "It is wednesday"
        case "thursday":
            return "It is thursday"
        case "friday":
            return "It is friday"
        case "saturday":
            return "It is saturday"
        case _:
            return "The day is not valid" #_ is wildcard.It is like else.If no case match then it works
print(day_of_week("jnd"))

def is_weekend(day):
    match day:
        case "friday" | "saturday":
            return True
        case "sunday" | "sunday" | "monday" | "tuesday" | "wednesday":
            return False
        case _:
            return False
print(is_weekend("monday"))
