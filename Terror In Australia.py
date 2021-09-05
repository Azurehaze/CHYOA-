#functions for pages with choices are defined here.
def pause():
    input("Type any input to continue.")
def p10():
    global pagenum
    while pagenum not in ('3','18'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 3
            break
        elif choice == '2':
            pagenum = 18
            break
        else:
            print("Invalid Input.")
            continue
def p14():
    global pagenum
    while pagenum not in ('13','27'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 13
            break
        elif choice == '2':
            pagenum = 27
            break
        else:
            print("Invalid Input.")
            continue
def p24():
    global pagenum
    while pagenum not in ('40','101'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 40
            break
        elif choice == '2':
            pagenum = 101
            break
        else:
            print("Invalid Input.")
            continue
def p25():
    global pagenum
    while pagenum not in ('80','69'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 80
            break
        elif choice == '2':
            pagenum = 69
            break
        else:
            print("Invalid Input.")
            continue
def p28():
    global pagenum
    while pagenum not in ('65','34'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 65
            break
        elif choice == '2':
            pagenum = 34
            break
        else:
            print("Invalid Input.")
            continue
def p35():
    global pagenum
    while pagenum not in ('76','51'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 76
            break
        elif choice == '2':
            pagenum = 51
            break
        else:
            print("Invalid Input.")
            continue
def p38():
    global pagenum
    while pagenum not in ('63','42'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 63
            break
        elif choice == '2':
            pagenum = 42
            break
        else:
            print("Invalid Input.")
            continue
def p49():
    global pagenum
    while pagenum not in ('15','92'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 15
            break
        elif choice == '2':
            pagenum = 92
            break
        else:
            print("Invalid Input.")
            continue
def p59():
    global pagenum
    while pagenum not in ('46','68'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 46
            break
        elif choice == '2':
            pagenum = 68
            break
        else:
            print("Invalid Input.")
            continue
def p62():
    global pagenum
    while pagenum not in ('71','87'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 71
            break
        elif choice == '2':
            pagenum = 87
            break
        else:
            print("Invalid Input.")
            continue
def p77():
    global pagenum
    while pagenum not in ('100','57'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 100
            break
        elif choice == '2':
            pagenum = 57
            break
        else:
            print("Invalid Input.")
            continue
def p107():
    global pagenum
    while pagenum not in ('82','110'):
        choice = input("Make your choice:")
        if choice == '1':
            pagenum = 82
            break
        elif choice == '2':
            pagenum = 110
            break
        else:
            print("Invalid Input.")
            continue

#use "active" as a variable to change later that can end the program.
global active
active = "yes"
#Open starting page
pagenum = 0
page0 = open("Files\page0.txt","r")
print(page0.read())
pause()
page0.close()

pagenum = 1
page1 = open("Files\page1.txt","r")
print(page1.read())
pause()
page1.close()

pagenum = 2
page2 = open("Files\page2.txt","r")
print(page2.read())
pause()
page2.close()

pagenum = 6
page6 = open("Files\page6.txt","r")
print(page6.read())
pause()
page6.close()

#####first story branch, page 10
pagenum = 10
page10 = open("Files\page10.txt","r")
print(page10.read())
p10()
page10.close()
if pagenum == 3:
    page3 = open("Files\page3.txt","r")
    print(page3.read())
    pause()
    page3.close()
    #turn to page 8
    page8 = open("Files\page8.txt","r")
    print(page8.read())
    pause()
    page8.close()
    #turn to page 14
    page14 = open("Files\page14.txt","r")
    print(page14.read())
    p14()
    page14.close()
    #####story branch, page 14
    if pagenum == 13:
        page13 = open("Files\page13.txt","r")
        print(page13.read())
        pause()
        #turn to page 25
        page13.close()
        page25 = open("Files\page25.txt","r")
        print(page25.read())
        #####story branch, page 25
        p25()
        page25.close()
        if pagenum == 80:
            page80 = open("Files\page80.txt","r")
            print(page80.read())
            pause()
            #turn to page 75
            page80.close()
            page75 = open("Files\page75.txt","r")
            print(page75.read())
            pause()
            #turn to page 39
            page39 = open("Files\page39.txt","r")
            print(page39.read())
            pause()
            #turn to page 45
            page39.close()
            page45 = open("Files\page45.txt","r")
            print(page45.read())
            pause()
            #turn to page 77
            page45.close()
            page77 = open("Files\page77.txt","r")
            p77()
            page77.close()
            #####story branch, page 77
            if pagenum == 100:
                page100 = open("Files\page100.txt","r")
                print(page100.read())
                pause()
                #turn to page 104
                page100.close()
                page104 = open("Files\page104.txt","r")
                print(page104.read())
                pause()
                #turn to page 83
                page104.close()
                page83 = open("Files\page83.txt","r")
                print(page83.read())
                pause()
                #turn to page 89
                page83.close()
                page89 = open("Files\page89.txt","r")
                print(page89.read())
                pause()
                #turn to page 4
                page89.close()
                page4 = open("Files\page4.txt","r")
                print(page4.read())
            elif pagenum == 57:
                page57 = open("Files\page57.txt","r")
                print(page57.read())
                pause()
                #turn to page 73
                page57.close()
                page73 = open("Files\page73.txt","r")
                page73.close()
        elif pagenum == 69:
            page69 = open("Files\page69.txt","r")
            print(page69.read())
            page69.close()
    elif pagenum == 27:
        page27 = open("Files\page27.txt","r")
        print(page27.read())
        pause()
        #turn to page 17
        page27.close()
        page17 = open("Files\page17.txt","r")
        print(page17.read())
        pause()
        #turn to page 28
        page17.close()
        page28 = open("Files\page28.txt","r")
        print(page28.read())
        #####Story branch, page 28
        p28()
        page28.close()
        if pagenum == 65:
            page65 = open("Files\page65.txt","r")
            print(page65.read())
            pause()
            #turn to page 66
            page65.close()
            page66 = open("Files\page66.txt","r")
            print(page66.read())
            page67 = open("Feils\page67.txt","r")
            print(page67.read())
            pause()
            #turn to page 29
            page66.close()
            page67.close()
            page29 = open("Files\page29.txt","r")
            print(page29.read())
            pause()
            #turn to page 106
            page29.close()
            page106 = open("Files\page106.txt","r")
            print(page106.read())
            pause()
            page106.close()
            #turn to page 38
            page38 = open("Files\page38.txt","r")
            print(page38.read())
            page38.close()
            p38()
            if pagenum == 63:
                page63 = open("Files\page63.txt","r")
                print(page63.read())
                pause()
                page63.close()
                #turn to page 41
                page41 = open("Files\page41.txt","r")
                print(page41.read())
                page41.close()
            elif pagenum == 42:
                page42 = open("Files\page42.txt","r")
                print(page42.read())
                pause()
                page42.close()
                #turn to page 61
                page61 = open("Files\page61.txt","r")
                print(page61.read())
                pause()
                page61.close()
                #turn to page 53
                page53 = open("Files\page53.txt","r")
                print(page53.read())
                pause()
                page53.close()
                #turn to page 74
                page74 = open("Files\page74.txt","r")
                print(page74.open())
                page74.close()
        elif pagenum == 34:
            page34 = open("Files\page34.txt","r")
            print(page34.read())
            pause()
            #turn to page 35
            page34.close()
            page35 = open("Files\page35.txt","r")
            print(page35.read())
            page35.close()
            p35()
            #####Story branch, page 35#####
            if pagenum == 76:
                page76 = open("Files\page76.txt","r")
                print(page76.read())
                pause()
                page76.close()
                #turn to page 22
                page22 = open("Files\page22.txt","r")
                print(page22.read())
                page22.close()
            elif pagenum == 51:
                page51 = open("Files\page51.txt","r")
                print(page51.read())
                pause()
                #turn to page 43
                page51.close()
                page43 = open("Files\page43.txt","r")
                print(page43.read())
                pause()
                #turn to page 58
                page43.close()
                page58 = open("Files\page58.txt","r")
                print(page58.read())
                pause()
                #turn to page 50
                page58.close()
                page50 = open("Files\page50.txt","r")
                print(page50.read())
                pause()
                #turn to page 54
                page50.close()
                page54 = open("Files\page54.txt","r")
                print(page54.read())
                pause()
                #turn to page 59
                page54.close()
                page59 = open("Files\page59.txt","r")
                print(page59.read())
                page59.close()
                p59()
                #####Story branch, page 59#####
                if pagenum == 46:
                    page46 = open("Files\page46.txt","r")
                    print(page46.read())
                    pause()
                    page46.close()
                    #turn to page 52
                    page52 = open("Files\page52.txt","r")
                    print(page52.read())
                    pause()
                    page52.close()
                    #turn to page 64
                    page64 = open("Files\page64.txt","r")
                    print(page64.read())
                    pause()
                    page64.close()
                    #turn to page 37
                    page37 = open("Files\page37.txt","r")
                    print(page37.read())
                    pause()
                    page37.close()
                    #turn to page 11
                    page11 = open("Files\page11.txt","r")
                    print(page11.read())
                    pause()
                    page11.close()
                    #turn to page 62
                    page62 = open("Files\page62.txt","r")
                    print(page62.read())
                    page62.close()
                    p62()
                    #####Story branch, page 62#####
                    if pagenum == 71:
                        page71 = open("Files\page71.txt","r")
                        print(page71.read())
                        pause()
                        page71.close()
                        #turn to page 56
                        page56 = open("Files\page56.txt",'r')
                        print(page56.read())
                        pause()
                        page56.close()
                        #turn to page 7
                        page7 = open("Files\page7.txt","r")
                        print(page7.read())
                        page7.close()
                    elif pagenum == 87:
                        page87 = open("Files\page87.txt","r")
                        print(page87.read())
                        pause()
                        page87.close()
                        #turn to page 97
                        page97 = open("Files\page97.txt","r")
                        print(page97.read())
                        pause()
                        page97.close()
                        page98 = open("Files\page98.txt","r")
                        print(page98.read())
                        page98.close()
                        page99 = open("Files\page99.txt","r")
                        print(page99.read())
                        pause()
                        page99.close()
                        #turn to page 81
                        page81 = open("Files\page81.txt","r")
                        print(page81.read())
                        pause()
                        page81.close()
                        #turn to page 86
                        page86 = open("Files\page86.txt","r")
                        print(page86.read())
                        page86.close()
                #choice from page 59#
                elif pagenum == 68:
                    page68 = open("Files\page68.txt","r")
                    print(page68.read())
                    pause()
                    page68.close()
                    #turn to page 84
                    page84 = open("Files\page84.txt","r")
                    print(page84.read())
                    pause()
                    page84.close()
                    #turn to page 31
                    page31 = open("Files\page31.txt","r")
                    print(page31.read())
                    pause()
                    page31.close()
                    #turn to page 113
                    page113 = open("Files\page113.txt","r")
                    print(page113.read())
                    page113.close()
elif pagenum == 18:
    page18 = open("Files\page18.txt","r")
    print(page18.read())
    pause()
    #turn to page 49
    page18.close()
    page49 = open("Files\page49.txt","r")
    print(page49.read())
    p49()
    #####Story branch, page 49#####
    page49.close()
    if pagenum == 15:
        page15 = open("Files\page15.txt","r")
        print(page15.read())
        pause()
        #turn to page 19
        page15.close()
        page19 = open("Files\page19.txt","r")
        print(page19.read())
        pause()
        #turn to page 95
        page19.close()
        page95 = open("Files\page95.txt","r")
        print(page95.read())
        pause()
        #turn to page 32
        page95.close()
        page32 = open("Files\page32.txt","r")
        print(page32.read())
        pause()
        #turn to page 70
        page32.close()
        page70 = open("Files\page70.txt","r")
        print(page70.read())
        pause()
        #turn to page 24
        page70.close()
        page24 = open("Files\page24.txt","r")
        print(page24.read())
        p24()
        page24.close()
        #####story branch, page 24#####
        if pagenum == 40:
            page40 = open("Files\page40.txt","r")
            print(page40.read())
            pause()
            #turn to page 94
            page40.close()
            page94 = open("files\page94.txt","r")
            print(page94.read())
            page94.close()
        elif pagenum == 101:
            page101 = open("Files\page101.txt","r")
            print(page101.read())
            pause()
            page101.close()
            #turn to page 111
            page111 = open("Files\page111.txt","r")
            print(page111.read())
            pause()
            page111.close()
            #turn to page 47
            page47 = open("Files\page47.txt","r")
            print(page47.read())
            page47.close()
    elif pagenum == 92:
        page92 = open("Files\page92.txt","r")
        print(page92.read())
        page92.close()
        pause()
        page93 = open("Files\page93.txt","r")
        print(page93.read())
        pause()
        #turn to page 20
        page20 = open("Files\page20.txt","r")
        print(page20.read())
        pause()
        page20.close()
        #turn to page 96
        page96 = open("Files\page96.txt","r")
        print(page96.read())
        pause()
        page96.close()
        #turn to page 21
        page21 = open("Files\page21.txt","r")
        print(page21.read())
        pause()
        page21.close()
        #turn to page 103
        page103 = open("Files\page103.txt","r")
        print(page103.read())
        pause()
        page103.close()
        #turn to page 30
        page30 = open("Files\page30.txt","r")
        print(page30.read())
        pause()
        page30.close()
        #turn to page 107
        page107 = open("Files\page107.txt","r")
        print(page107.read())
        #####Story branch, page 107
        page107.close()
        p107()
        if pagenum == 82:
            page82 = open("Files\page82.txt","r")
            print(page82.read())
            pause()
            #turn to page 90
            page82.close()
            page90 = open("Files\page90.txt","r")
            print(page90.read())
            pause()
            #turn to page 109
            page90.close()
            page109 = open("Files\page109.txt","r")
            print(page109.read())
            pause()
            #turn to page 112
            page112 = open("Files\page112.txt","r")
            print(page112.read())
            pause()
            #turn to page 78
            page112.close()
            page78 = open("Files\page78.txt","r")
            print(page78.read())
            pause()
            #turn to page 88
            page78.close()
            page88 = open("Files\page88.txt","r")
            print(page88.read())
            page88.close()
        elif pagenum == 110:
            page110 = open("Files\page110.txt","r")
            print(page110.read())
            pause()
            #turn to page 102
            page110.close()
            page102 = open("Files\page102.txt","r")
            print(page102.read())
            page102.close()



while active not in('exit','Exit'):
    active = input("You have reached one of the story's many endings. Thank you for reading.  T0 exit this program, type 'exit' and press the enter key.")
    if active in('exit,"Exit'):
        print("Thank you for reading.")
        exit()

