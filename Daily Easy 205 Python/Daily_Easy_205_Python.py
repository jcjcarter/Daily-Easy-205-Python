import arrow

for line in open().read("input.txt").splitlines():
    date1, date2 = line.split()
    date1, date2 = arrow.get(date1), arrow.get(date2)
    main_ordinals = ["th", "st", "nd", "rd"] + ["th"]*6
    ordinals = main_ordinals + ["th"]*10 + main_ordinals*2
    if date1.year != date2.year and not (date1.year == arrow.now().year and (date2-date1).days < 365):
        str1 = date1.format("MMMM D") + ordinals[date1.day] + ", " + date1.format("YYYY")
        str2 = date2.format("MMMM D") + ordinals[date2.day] + ", " + date2.format("YYYY")
    elif date1.month != date2.month:
        str1 = date1.format("MMMM D") + ordinals[date1.day]
        str2 = date2.format("MMMM D") + ordinals[date2.day]
    elif date1.day != date2.day:
        str1 = date1.format("MMMM D") + ordinals[date1.day]
        str2 = date2.format("D") + ordinals[date2.day]
    else:
        str1 = ""
        str2 = date2.format("MMMM D") + ordinals[date2.day]

    if date1.year == date2.year and date1.year != arrow.now().year:
        str2 += ", " + date1.format("YYYY")

    if str1:
        print(str1 + " - " + str2)
    else:
        print(str2)