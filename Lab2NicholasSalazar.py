#Nicholas Salazar
#Lab 2
#Simulation Part 1
import time
from itertools import groupby
from random import *

def main():
    #from youtube
    def removeDupl(inputList,option):
        if option==1:
            secondList=[]
            thirdList=[]
            for x in inputList:
                if x not in secondList:
                    secondList.append(x)
            return secondList
        else:
            secondList=[]
            thirdList=[]
            for x in inputList:
                if x not in secondList:
                    secondList.append(x)
                else:
                    thirdList.append(x)
            return thirdList
            
    #
    class physician:
        def __init__(self,name):
            self.name = name
            self.random = randint(15,20)
        def seePatient(self):
            self.random = randint(15,20)
            return self.random

    class nurse:
        def __init__(self,name,random):
            self.name = name
            self.random = random
        def triagePatient(self):
            self.random = randint(1,100)
            return self.random
            
    class patient:
        def __init__(self, name, location, triageNO):
            self.name = name
            self.triage = int(triageNO)
            self.location = location
        def moveTo(self,location):
            self.location = location
        def getName(self):
            return self.name
        
    wR = "WaitingRoom"
    examRooms = 0
    eR = "ExamRoom"
    H = "Home"


    Patient1 = patient("Lucy",wR,0)
    Patient2 = patient("Frodo",wR,0)
    Patient3 = patient("Mister Miyagi",wR,0)
    Patient4 = patient("Elmo",wR,0)
    Patient5 = patient("Cody",wR,0)
    Patient6 = patient("Jimmy",wR,0)
    Patient7 = patient("Ozzy",wR,0)
    Patient8 = patient("Kim",wR,0)
    Patient9 = patient("Sarah",wR,0)
    Patient10 = patient("Winnie",wR,0)
    Patient11 = patient("Garry",wR,0)
    Patient12 = patient("Werry",wR,0)
    nurse = nurse("Larry",randint(1,100))
    Physician1 = physician("Barry")
    Physician2 = physician("Jerry")
    Physician3 = physician("Terry")
    Physician4 = physician("Carey")
    Physician5 = physician("Merey")
    Physician6 = physician("Hairy")
    startTime = time.clock()
    endTime = time.clock()
    k = 1
    mainList = [Patient1,Patient2,Patient3,Patient4,Patient5,Patient6\
                ,Patient7,Patient8,Patient9,Patient10,Patient11,Patient12]
    examRoomList = []
    TimeforNext=[15]#minutes before another examRoom available
    Frequency=[]
    t = 0
    for i in mainList:
        x = nurse.triagePatient()
        i.triage = x
    while t !=25:
        if t== TimeforNext[0]:
            examRooms= examRooms-1
            TimeforNext.remove(TimeforNext[0])
        for i in mainList:
            if i.triage > 50 and examRooms <6 and i.location!="Home":
                i.moveTo(eR)
                examRooms = examRooms + 1
                examRoomList.append(i)
                mainList.remove(i)
                print("Name:",i.name,"added to exam room with triageNO:",i.triage)
        for i in mainList:
            if i.triage < 50 and examRooms < 6 and i.location!="Home":
                i.moveTo(eR)
                examRooms = examRooms + 1
                examRoomList.append(i)
                mainList.remove(i)
                print("Name:",i.name,"added to exam room with triageNO:",i.triage)
        for i in examRoomList:
            if k==7:
                k=1
            if k ==1:
                x = Physician1
            elif k==2:
                x= Physician2
            elif k==3:
                x= Physician3
            elif k==4:
                x= Physician4
            elif k==5:
                x= Physician5
            elif k==6:
                x= Physician6
            i.moveTo(H)
            timeTook = int(x.seePatient())
            TimeforNext.append(timeTook)
            print("Patient:",i.name,",is being treated by:",x.name,"for:",timeTook\
                  ,"minutes")
            examRoomList.remove(i)
            time.sleep(0.5)
            k=k+1
        TimeforNext = sorted(TimeforNext)
        Frequency = removeDupl(TimeforNext,0)
        TimeforNext = removeDupl(TimeforNext,1)
        t=t+1
        print("Time passed:",t,"minutes")
        time.sleep(2)
        
        
   
    









main()
