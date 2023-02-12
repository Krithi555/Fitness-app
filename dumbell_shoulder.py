import  cv2
import time
import practices11 as pr
import numpy as np
score = 0
total_score = 0
average_score=0

#def give_score(total_score):
    # nTime = time.time()
    #timeDiff = nTime - bTime
    # fps = 1 / (nTime-bTime)
    #print(timeDiff)



cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
bTime = 0
timeDiff = 0
nTime = time.time()


detector = pr.poseDetector()
count = 0
rep_up=0
ptime=0






while True and count<=20:
    success, image = cap.read()
    image = cv2.resize(image, (1280, 720))
    image = cv2.flip(image, 2)
    image = detector.findPose(image,False)
    lmList =detector.findPosition(image,False)
    wrist = []
    if len(lmList) !=0:
        arm_r = detector.findAngle(image, 12, 14, 16)
        arm_l = detector.findAngle(image, 11, 13, 15)
        upbody_r =detector.findAngle(image,24,12,14)
        upbody_l = detector.findAngle(image, 23, 11, 13)
        per_l = np.interp(upbody_l, (235, 270), (100, 0))
        per_r = np.interp(upbody_r, (95, 124), (0, 100))
        angle = detector.findAngle(image, 12, 14, 16)
        per = np.interp(angle, (210, 310), (0, 100))
        if lmList[11][2]>lmList[14][2]:  #  khuy tay cao hon vai
            wrist.append([lmList[14][1], lmList[14][2]-detector.lenght(image,14,16)]) # ve co tay chuan ben phai
            wrist.append([lmList[13][1], lmList[13][2]-detector.lenght(image,14,16)])#ve co tay chuan trai
            angle_r = detector.cosin2goc(image,wrist[0],14,16)
            angle_l = detector.cosin2goc(image, wrist[1], 13, 15)

        color = (255, 0, 255)
        if (per_l == 100 and per_r == 100):
            color = (255, 0, 255)
            if rep_up == 0:
                count += 0.5
                bTime = nTime
                rep_up = 1
        if (per_l == 0 and per_r == 0):
            color = (0, 255, 0)
            if rep_up == 1:
                count += 0.5
                rep_up = 0
                nTime = time.time()

                timeDiff = nTime - bTime
            # fps = 1 / (nTime-bTime)
                print(timeDiff)
                if (timeDiff < 5 and timeDiff > 0):
                    score = 95
                    total_score += score

                elif (timeDiff < 10 and timeDiff > 5):
                    score = 90
                    total_score += score
                elif (timeDiff < 15 and timeDiff > 10):
                    score = 85
                    total_score += score
                elif (timeDiff < 20 and timeDiff > 15):
                    score = 80
                    total_score += score
                elif (timeDiff < 25 and timeDiff > 20):
                    score = 75
                    total_score += score
                elif (timeDiff < 30 and timeDiff > 25):
                    score = 70
                    total_score += score
                elif (timeDiff < 35 and timeDiff > 30):
                    score = 65
                    total_score += score
                elif (timeDiff < 40 and timeDiff > 35):
                    score = 60
                    total_score += score
                elif (timeDiff < 45 and timeDiff > 40):
                    score = 55
                    total_score += score
                elif (timeDiff < 50 and timeDiff > 45):
                    score = 50
                    total_score += score
                elif (timeDiff < 55 and timeDiff > 50):
                    score = 45
                    total_score += score
                elif (timeDiff < 60 and timeDiff > 55):
                    score = 40
                    total_score += score
                else:
                    score = 0
                average_score = (total_score/950) * 100

        # total_score += score
        # cv2.putText(image, f"TIME PERIOD: {int(timeDiff)}", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)

    print(count)
    cv2.rectangle(image, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
    cv2.putText(image, str(int(count)), (40, 670), cv2.FONT_HERSHEY_PLAIN, 10,
                    (255, 0, 0), 13)
    #cv2.rectangle(image, (350, 450), (720, 550), (0, 255, 0), cv2.FILLED)
    cv2.putText(image, f"TIME PERIOD: {int(timeDiff)}", (50, 70), cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 0, 0), 3)





    #bTime = nTime

    cv2.putText(image, f"SCORE: {int(score)}", (50, 350), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)
    cv2.putText(image, f"TOTAL SCORE: {int(total_score)}", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("hienthi", image)
    if count == 10:

       cv2.putText(image, f"WORKOUT COMPLETE", (350, 400), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255), 2)
       cv2.putText(image, f"OVERALL PERFORMANCE: {int(average_score)}", (400, 500), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2)
       cv2.imshow("hienthi", image)
    if count == 11:
        break


    if cv2.waitKey(5) & 0xff == ord("q"):
        break





cap.release()


cv2.destroyAllWindows()

