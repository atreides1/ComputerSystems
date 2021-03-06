import statistics 
def read_coords(filename):
    y_coords = []
    with open(filename, "r") as file:
        s  = file.readlines()

        for i in range(len(s)):
            coord = s[i].split(", ")
            coord = coord[1].split("\n")[0]
            coord = float(coord)
            y_coords.append(coord)
    return y_coords

# coords_1 = read_coords("hw1data.csv")
# coords_2 = read_coords("hw1data_2.csv")
# coords_3 = read_coords("hw1data_3.csv")
# coords_4 = read_coords("hw1data_4.csv")
# coords_5 = read_coords("hw1data_5.csv")
# coords_6 = read_coords("hw1data_6.csv")
# coords_7 = read_coords("hw1data_7.csv")
# coords_8 = read_coords("hw1data_8.csv")
# coords_9 = read_coords("hw1data_9.csv")
# coords_10 = read_coords("hw1data_10.csv")
# coords_11 = read_coords("hw1data_11.csv")

coords_1_ = read_coords("1hw1data_1.csv")
coords_2_ = read_coords("1hw1data_2.csv")
coords_3_ = read_coords("1hw1data_3.csv")
coords_4_ = read_coords("1hw1data_4.csv")
coords_5_ = read_coords("1hw1data_5.csv")
coords_6_ = read_coords("1hw1data_6.csv")
coords_7_ = read_coords("1hw1data_7.csv")
coords_8_ = read_coords("1hw1data_8.csv")
coords_9_ = read_coords("1hw1data_9.csv")
coords_10_ = read_coords("1hw1data_10.csv")
coords_11_ = read_coords("1hw1data_11.csv")



def take_average(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11):
    average = []
    for i in range(len(l1)):
        average.append((l1[i] + l2[i] + l3[i] + l4[i] +l5[i] + l6[i] +l7[i] + l8[i] +l9[i] + l10[i] +l11[i])/11)
    return average

def take_min(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11):
    mins = []
    for i in range(len(l1)):
        mins.append(min(l1[i],l2[i], l3[i], l4[i], l5[i], l6[i], l7[i], l8[i], l9[i], l10[i], l11[i]))
    return mins

def take_median(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11):
    meds = []
    for i in range(len(l1)):
        meds.append(statistics.median([l1[i],l2[i], l3[i], l4[i], l5[i], l6[i], l7[i], l8[i], l9[i], l10[i], l11[i]]))
    return meds

# avgs = take_average(coords_1, coords_2, coords_3, coords_4, coords_5, coords_6, coords_7, coords_8, coords_9, coords_10, coords_11)
# mins = take_min(coords_1, coords_2, coords_3, coords_4, coords_5, coords_6, coords_7, coords_8, coords_9, coords_10, coords_11)
# meds = take_median(coords_1, coords_2, coords_3, coords_4, coords_5, coords_6, coords_7, coords_8, coords_9, coords_10, coords_11)

avgs_ = take_average(coords_1_, coords_2_, coords_3_, coords_4_, coords_5_, coords_6_, coords_7_, coords_8_, coords_9_, coords_10_, coords_11_)
mins_ = take_min(coords_1_, coords_2_, coords_3_, coords_4_, coords_5_, coords_6_, coords_7_, coords_8_, coords_9_, coords_10_, coords_11_)
meds_ = take_median(coords_1_, coords_2_, coords_3_, coords_4_, coords_5_, coords_6_, coords_7_, coords_8_, coords_9_, coords_10_, coords_11_)
import matplotlib.pyplot as plt


plt.title("Average Access time in nanoseconds vs. buffer size")

x_axis = []
for i in range(10,30):
    x_axis.append(2**(i)/1024)

plt.plot(x_axis, avgs_)

#plt.xticks(x_axis)
plt.xscale("log", basex=2)
plt.xlabel("Buffer Size in KB")
plt.ylabel("Time in nanoseconds")
plt.axvline(x = 64, color = "r", alpha = 0.3)
plt.axvline(x = 1028, color = "r", alpha = 0.3)
plt.axvline(x = 34307, color = "r", alpha = 0.3)
plt.show()
