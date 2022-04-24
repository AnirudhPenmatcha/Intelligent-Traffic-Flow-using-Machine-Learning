import detections
import cv2
import threading
import ManualCheck

green_min = 10
green_max = 90
yellow = 5
min_red = 10
max_red = 180
car_time = 2; motorbike_time = 2; bus_time = 3; truck_time = 4; Emergency_vehicle_time = 20
no_oflanes = 4
order = [-1,-1,-1,-1]
order_of_emergency = [-1,-1,-1,-1]
Starvation_vehicle_limits = 5
Starvation = {1: 0, 2: 0, 3: 0, 4: 0}
old_den_value = []
Starvation_max_limit = 300

def Starvation_check(old_values, new_values):
    for q in range(4):
        if(new_values[str(q)] > old_values[q+1]-5 or new_values[str(q)] < old_values[q+1]+5):
            print(Lane + " " + str(q+1) + "should turn green as soon as possible")
            return True
    return False

def Density(Road):
    if Road["Emergency_vehicle"] > 0:
        return True, Road["car"] + Road["motorbike"] + Road["bus"] + Road["truck"]
    else:
        return False, Road["car"] + Road["motorbike"] + Road["bus"] + Road["truck"]


def GreenSignalTime_Normal(Road):
    cars = Road["car"] * car_time
    motorbikes = Road["motorbike"] * motorbike_time
    buses = Road["bus"] * bus_time
    trucks = Road["truck"] * truck_time
    return (cars+motorbikes+buses+trucks)//no_oflanes

def GreenSignalTime_Emergency(Road):
    emergency_vehicles = Road["Emergency_vehicle"] * Emergency_vehicle_time
    return emergency_vehicles//(no_oflanes-2)

def AIProcessing(Road1, Road2, Road3, Road4, network, class_names, class_colors, v4_network, v4_class_names, v4_class_colors):

    print("###############Processing images through the AI model#################")

    Roads, img_bbox, v4_img_bbox = detections.detect(Road1, Road2, Road3, Road4, network, class_names, class_colors, v4_network, v4_class_names, v4_class_colors)
    return Roads, img_bbox, v4_img_bbox

def printSignalsTime_Emergency():

            O = -1
            if(order_of_emergency == [-1,-1,-1,-1]):
                return

            for n, i in enumerate(order_of_emergency):
                if i >= 0:
                    O = i
                    break

            for l in range(1,5):
                if TS[l]["R"] < 0:
                    TS[l]["R"] = min_red
                if TS[l]["R"] > max_red:
                    TS[l]["R"] = max_red
                if TS[l]["Y"] <= 0:
                    TS[l]["Y"] = 5


            if O == 0:
                if TS[1]["G"] > 0:
                    TS[1]["G"] -= 1;
                    print("Traffic Signal 1", TS[1], "< --Green")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("--------------Emergency Vehicle Alert----------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1

                elif TS[1]["G"] == 0:
                    TS[1]["Y"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Yellow")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("--------------Emergency Vehicle Alert----------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                if TS[1]["Y"] == 0:
                    order_of_emergency[n] = -1
            elif O == 1:
                if TS[2]["G"] > 0:
                    TS[2]["G"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Green")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("--------------Emergency Vehicle Alert----------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                elif TS[2]["G"] == 0:
                    TS[2]["Y"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Yellow")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("--------------Emergency Vehicle Alert----------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                if TS[2]["Y"] == 0:
                    order_of_emergency[n] = -1
            elif O == 2:
                if TS[3]["G"] > 0:
                    TS[3]["G"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Green")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("--------------Emergency Vehicle Alert----------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                elif TS[3]["G"] == 0:
                    TS[3]["Y"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Yellow")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("--------------Emergency Vehicle Alert----------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                if TS[3]["Y"] == 0:
                    order_of_emergency[n] = -1
            elif O == 3:
                if TS[4]["G"] > 0:
                    TS[4]["G"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Green")
                    print("--------------Emergency Vehicle Alert----------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                elif TS[4]["G"] == 0:
                    TS[4]["Y"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Yellow")
                    print("--------------Emergency Vehicle Alert----------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                if TS[4]["Y"] == 0:
                    order_of_emergency[n] = -1

            # print("Traffic Signal 1", TS[1],"Traffic Signal 2", TS[2],"Traffic Signal 3", TS[3],"Traffic Signal 4", TS[4], sep = "\n")
            # print("------------------------------")

            t2 = threading.Timer(1.0, printSignalsTime_Emergency)
            t2.start()
            t2.join()

def printSignalsTime():

            O = -1
            for n, i in enumerate(order):
                if i >= 0:
                    O = i
                    break

            for l in range(1,5):
                if TS[l]["R"] < 0:
                    TS[l]["R"] = min_red
                if TS[l]["R"] > max_red:
                    TS[l]["R"] = max_red
                if TS[l]["Y"] <= 0:
                    TS[l]["Y"] = 5


            if O == 0:
                if TS[1]["G"] > 0:
                    TS[1]["G"] -= 1; TS[2]["R"] -= 1; TS[3]["R"] -= 1; TS[4]["R"] -= 1;
                    print("Traffic Signal 1", TS[1], "< --Green")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("------------------------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                elif TS[1]["G"] == 0:
                    TS[1]["Y"] -= 1; TS[2]["R"] -= 1; TS[3]["R"] -= 1; TS[4]["R"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Yellow")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("------------------------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                if TS[1]["Y"] == 0:
                    order[n] = -1
            elif O == 1:
                if TS[2]["G"] > 0:
                    TS[2]["G"] -= 1; TS[1]["R"] -= 1; TS[3]["R"] -= 1; TS[4]["R"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Green")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("------------------------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                elif TS[2]["G"] == 0:
                    TS[2]["Y"] -= 1; TS[1]["R"] -= 1; TS[3]["R"] -= 1; TS[4]["R"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Yellow")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("------------------------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                if TS[2]["Y"] == 0:
                    order[n] = -1
            elif O == 2:
                if TS[3]["G"] > 0:
                    TS[3]["G"] -= 1; TS[1]["R"] -= 1; TS[2]["R"] -= 1; TS[4]["R"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Green")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("------------------------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                elif TS[3]["G"] == 0:
                    TS[3]["Y"] -= 1; TS[1]["R"] -= 1; TS[2]["R"] -= 1; TS[4]["R"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Yellow")
                    print("Traffic Signal 4", TS[4], "<-- Red")
                    print("------------------------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                if TS[3]["Y"] == 0:
                    order[n] = -1
            elif O == 3:
                if TS[4]["G"] > 0:
                    TS[4]["G"] -= 1; TS[1]["R"] -= 1; TS[2]["R"] -= 1; TS[3]["R"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Green")
                    print("------------------------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                elif TS[4]["G"] == 0:
                    TS[4]["Y"] -= 1; TS[1]["R"] -= 1; TS[2]["R"] -= 1; TS[3]["R"] -= 1;
                    print("Traffic Signal 1", TS[1], "<-- Red")
                    print("Traffic Signal 2", TS[2], "<-- Red")
                    print("Traffic Signal 3", TS[3], "<-- Red")
                    print("Traffic Signal 4", TS[4], "<-- Yellow")
                    print("------------------------------")
                    Starvation[1] += 1; Starvation[2] += 1; Starvation[3] += 1; Starvation[4] += 1
                if TS[4]["Y"] == 0:
                    order[n] = -1

            # print("Traffic Signal 1", TS[1],"Traffic Signal 2", TS[2],"Traffic Signal 3", TS[3],"Traffic Signal 4", TS[4], sep = "\n")
            # print("------------------------------")

            t1 = threading.Timer(1.0, printSignalsTime)
            t1.start()


if __name__ == "__main__":

    network, class_names, class_colors, v4_network, v4_class_names, v4_class_colors = detections.start_yolo()

# def main():

    TS = {
    1 : {"R":max_red, "Y":5, "G":0},
    2 : {"R":max_red, "Y":5, "G":0},
    3 : {"R":max_red, "Y":5, "G":0},
    4 : {"R":max_red, "Y":5, "G":0}
    }

    R = ["Road1", "Road2", "Road3", "Road4"]
    density = {'0': 0, '1': 0,'2': 0, '3': 0}
    Emergency = []

    print("Default Values :", "Traffic Signal 1", TS[1],"Traffic Signal 2", TS[2],"Traffic Signal 3", TS[3],"Traffic Signal 4", TS[4], sep = "\n")


    Road1 = cv2.imread("test_images/roads/road1.jpeg")
    Road2 = cv2.imread("test_images/roads/road2.jpeg")
    Road3 = cv2.imread("test_images/roads/road3.jpeg")
    Road4 = cv2.imread("test_images/roads/road4.jpeg")


    Roads, img_bbox, v4_img_bbox = AIProcessing(Road1, Road2, Road3, Road4, network, class_names, class_colors, v4_network, v4_class_names, v4_class_colors)

    # print(Roads)

    for i in range(4):
        Emerg_veh, dense = Density(Roads[R[i]])
        Emergency.append(Emerg_veh)
        density[str(i)] = dense

    if(Starvation[1] == Starvation_max_limit or Starvation[2] == Starvation_max_limit or Starvation[3] == Starvation_max_limit or Starvation[4] == Starvation_max_limit):
        file2 = open("starvation.txt","r+")
        old_den = file2.readlines()
        for p in range(1,5):
            old_den_value.append(old_den[p][0:2])
        file2.close()
        Starv_result = Starvation_check(old_den_value, density)
        if Starv_result == False:
            Starvation[1] = 0; Starvation[2] = 0; Starvation[3] = 0; Starvation[4] = 0
        elif Starv_result == True:
            ManualCheck.manual_check()
            print("Manual check alert")

    prev_density = density
    # density.sort(reverse=True)
    # print(Emergency, density)

    for k in range(4):
        Keyofmaxvalue = max(zip(density.values(), density.keys()))[1]
        order[k] = (int(Keyofmaxvalue))
        density[Keyofmaxvalue] = 0

    prev_order = order
    printSignalsTime()


    GST = [0,0,0,0]
    Emergency_GST = [0,0,0,0]
    for j in range(4):
        GST[j] = GreenSignalTime_Normal(Roads[R[j]])
        # print("Green signal times in order of signals TS1, TS2, TS3, TS4 :", GST)


    # print(density[Keyofmaxvalue])
    # print("GST in original order", GST)
    # print("GST", GST[order[0]], GST[order[1]], GST[order[2]], GST[order[3]])
    # print("ORDER", order)

    redsignalsumm = [0, 5+GST[order[0]], 5+GST[order[0]]+GST[order[1]], 5+GST[order[0]]+GST[order[1]]+GST[order[2]]]


    if True in Emergency:
        order = [-1,-1,-1,-1]
        printSignalsTime()
        print("!!!!!!!!!!!!!!!!!!!!!!!! EMERGENCY VEHICLE DETECTED !!!!!!!!!!!!!!!!!!!!!!!!!!")
        for num, m in enumerate(Emergency):
            if m == True:
                order_of_emergency[num] = num
                Emergency_GST[num] = GreenSignalTime_Emergency(Roads[R[num]])
                if (num == 0):
                    TS[num+1] = {"R":0, "Y":5, "G":Emergency_GST[num]}
                elif (num == 1):
                    TS[num+1] = {"R":0, "Y":5, "G":Emergency_GST[num]}
                elif (num == 2):
                    TS[num+1] = {"R":0, "Y":5, "G":Emergency_GST[num]}
                elif (num == 3):
                    TS[num+1] = {"R":0, "Y":5, "G":Emergency_GST[num]}
        printSignalsTime_Emergency()



    order = prev_order
    for n, j in enumerate(order):
        if (j == 0):
            TS[j+1] = {"R":redsignalsumm[n], "Y":5, "G":GST[j]}
        elif (j == 1):
            TS[j+1] = {"R":redsignalsumm[n], "Y":5, "G":GST[j]}
        elif (j == 2):
            TS[j+1] = {"R":redsignalsumm[n], "Y":5, "G":GST[j]}
        elif (j == 3):
            TS[j+1] = {"R":redsignalsumm[n], "Y":5, "G":GST[j]}


    printSignalsTime()

    file1 = open("starvation.txt","w")
    file1.writelines([str(density['0']), '\n'])
    file1.writelines([str(density['1']), '\n'])
    file1.writelines([str(density['2']), '\n'])
    file1.writelines([str(density['3']), '\n'])
    file1.close()
    # GreenSignalTimer(Roads["Road1"])

# main()
