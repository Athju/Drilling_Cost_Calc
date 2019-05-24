
units=raw_input("If units are in meteres press 1 for feet please press 2:  ")

if units=="1":
    Bitcost=float(raw_input("Please input the cost of the Drill Bit: "))
    Drilltime=float(raw_input("Please input the drilling time in hours: "))
    Triptime=float(raw_input("Please input the Trip time in hours: "))
    Rigop=float(raw_input("Please input Rig operating costs in $/hr: "))
    Distance=float(raw_input("Please input the distance drilled in meters: "))

    Costperm=(Rigop*(Drilltime+Triptime)+Bitcost)/Distance

    print "The Cost per meter is: " , Costperm , " ($/m)"

elif units=="2":
    Bitcost=float(raw_input("Please input the cost of the Drill Bit: "))
    Drilltime=float(raw_input("Please input the drilling time in hours: "))
    Triptime=float(raw_input("Please input the Trip time in hours: "))
    Rigop=float(raw_input("Please input Rig operating costs in $/hr: "))
    Distance=float(raw_input("Please input the distance drilled in feet: "))

    Costperm=(Rigop*(Drilltime+Triptime)+Bitcost)/Distance

    print "The Cost per feet is: " , Costperm , " ($/ft)"

else:
    print "invalid input, please try again"
