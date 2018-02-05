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
        def __init__(self, name, location, triageNO,time):
            self.name = name
            self.triage = int(triageNO)
            self.location = location
            self.time=time
        def moveTo(self,location):
            self.location = location
        def getTime(self):
            return self.time

    Patients  = int(input("How many Patients?\n"))
    while Patients >59:
        print("Please print another number less than 60 \n")
        Patients = int(input("How many Patients?\n"))
    eRinput = int(input("How many exam rooms?\n"))
    p1=[]
    def nameGen():
        Patientlist = ["Stubby","Mister Miyagi","Frodo","Ozzy","Garry","Werry"\
                       ,"Winnie","Sarah","Kim","Jimmy","Melvin","Ronald","Tiff",\
                       "Norman","Donald,","Mickey","Bugs","Daff","Goofy","Betty",\
                       "Felix","Yogi","Pop","Scoob","Scooter","Chi","Souly","Jimker",\
                       "Timmy","John","Juhn","Lokar","Kimster","Quin","Monu","Jimster",\
                       ]
        for i in range(Patients):
            if i>35:
                p = ["patient",i]
                p = map(str,p)
                name = ''.join(p)
                p1.append(patient(name,wR,0,0))
                continue
            name = Patientlist[randint(0,int(len(Patientlist)-1))]
            Patientlist.remove(name)
            p1.append(patient(name,wR,0,0))
            
        return name
        
    wR = "WaitingRoom"
    examRooms = 0
    eR = "ExamRoom"
    H = "Home"
    
    nameGen()

    
    nurse = nurse("Larry",randint(1,100))
    Physician1 = physician("Barry")
    Physician2 = physician("Jerry")
    Physician3 = physician("Terry")
    Physician4 = physician("Carey")
    Physician5 = physician("Merey")
    Physician6 = physician("Hairy")
    startTime = time.clock()
    k = 1
    FinalList=[]
    
    mainList = p1
    examRoomList = []
    TimeforNext=[]#minutes before another examRoom available
    Frequency=[]
    mainFrequency = []
    FrequencyHelper=[]
    j=0
    counter1=1
    t = 0
    t1=0
    vari1=0
    lastList=[]
    switcher=0
    for i in mainList:
        print(i.name," added to the simulation")
        time.sleep(.01)
    for i in mainList:
        x = nurse.triagePatient()
        i.triage = x
        print(i.name,"triaged at:",i.triage)
 
    while mainList !=[]:
        if not mainList:
            break
        if t != 0:
            if t==TimeforNext[0]:
                TimeforNext.remove(TimeforNext[0])
                examRooms = examRooms - (1*mainFrequency.pop(0))
            
        for i in mainList:
            if i.triage > 50 and examRooms <eRinput and i.location!="Home":
                i.moveTo(eR)
                examRoomList.append(i)
                mainList.remove(i)
                examRooms = examRooms + 1
                print("Name:",i.name,"added to exam room with triageNO:",i.triage)
        for i in mainList:
            if i.triage < 50 and examRooms < eRinput and i.location!="Home":
                i.moveTo(eR)
                examRoomList.append(i)
                mainList.remove(i)
                examRooms = examRooms + 1
                print("Name:",i.name,"added to exam room with triageNO:",i.triage)
        for i in examRoomList:
            if k==7:
                k=1
            elif k ==1:
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
            i.time = timeTook
            print("Patient:",i.name,",is being treated by:",x.name,"for:",timeTook\
                  ,"minutes")
            if t1 >= 15:
                timeTook = t1 + timeTook
            lastList=TimeforNext
            FrequencyHelper.append(timeTook)
            TimeforNext.append(timeTook)
            i.time = timeTook
            k=k+1
        for i in range(4):
            for i in examRoomList:
                if i.time > 0:
                    examRoomList.remove(i)
                    FinalList.append(i)
        for i in examRoomList:
            print(i.name)
        FrequencyHelper = sorted(FrequencyHelper)
        TimeforNext = sorted(TimeforNext)
        Frequency = FrequencyHelper
        TimeforNext = removeDupl(TimeforNext,1)
        FrequencyHelper = removeDupl(FrequencyHelper,1)
        for i in FrequencyHelper:
            TimeforNext = sorted(TimeforNext)
            lastList.pop(0)
            if i in lastList and t1>0:
                TimeforNext = sorted(TimeforNext)
                mainFrequency.append(Frequency.count(i))
                mainFrequency[TimeforNext.index(i)]= mainFrequency[TimeforNext.index(i)]+1
                continue
            mainFrequency.append(Frequency.count(i))
        FrequencyHelper=[]
        print("Time until next exam rooms:",TimeforNext)    
        
        t=t+1
        t1=t1+1
        print("\nTime passed:",t1,"minutes\n")
        time.sleep(0.3)
    for i in FinalList:
        print(i.name,"waited",i.time,"minutes")
        j = i.time + j
        counter1=1
    print("Average wait time with",eRinput,"exam rooms and",Patients\
          ,"patients:\n",j/Patients)
        
        
        
   
    










main()
