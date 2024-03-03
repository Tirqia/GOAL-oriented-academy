#1  
#პარამეტრი             #პარამეტრი
# def sides_of_a_tringle(a,b,c):  
#     if a + b > c and a + c > b and b + c > a:
#         print("ასეთი სამკუთედი იარსებებს")
#     else:
#         print("ასეთი სამკუთხედი ვერ იარსებებს")

# sides_of_a_tringle(60, 60, 60,)
# sides_of_a_tringle(3, 7, 11,)
# #1-2ვარიანტი

# side_1 = float(input("enter side one"))
# side_2 = float(input("enter side two"))
# side_3 = float(input("enter side three"))
# #ფუნქც
# sides_of_a_tringle(side_1, side_2, side_3)

def names(aleko, beqa, saba): #პარამეტრი
    names_list = [aleko, beqa, saba]
    names_str = ", ".join(names_list)
    print("names: " + names_str)

names("aleko", "beqa", "saba")