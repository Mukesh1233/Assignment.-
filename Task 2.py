from statistics import mean
miles = []
while True:
    read = input("Enter next reading: ")
    re=read.lower()
    if read == "":
        break
    elif re[0] == "u":
        miles.append(float(read[1:]))
        print("Reading saved")
    elif re[0] == "e":
        miles.append(float(read[1:])/1.61)
        print("Reading saved")

if len(miles) == 0:
    print("No data entered.")
else:
    print("\nReading Summary\n")
    print(len(miles)," Reading Analysed\n")
    print(f"Maximum speed {max(miles):.2f} MPH, {max(miles)*1.61:.2f} KPH")
    print(f"Minimum speed {min(miles):.2f} MPH, {min(miles)*1.61:.2f} KPH")
    print(f"Average speed {mean(miles):.2f} MPH, {mean(miles)*1.61:.2f} KPH")
        