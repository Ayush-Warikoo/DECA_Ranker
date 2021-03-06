import csv
#Prioritizes quality over quantity (Ex will make 1 ICDC person happpy over everybody else, no matter how many people get their second choice as a result)
#Must put in partner's exact name for it to work (spelled correctly to the space, capitals don't matter)
#Principles

#Check for names with apostrophes, check for partner discrepencies, people with the same name, duplicate entries, blank entries
#Run the code, if events don't have enough people do those ones first manually(BTDM, FTDM, BLTDM, TTDM, ASM had the least)(MTDM, STDM, ACT, BFS, MSC, HRM had the most) 
#After you get your list look at all the people at the end and exchange some with other (since the code does first come first serve with people at the same level)

#Last Year test results with algorithm
#131 people get top 3
#8 people partner/name discrepencies
#2 people put manually in

#What if only 1 person has an event in their top 3 (ASM) --> Last year they forced late people into it and it only had 3 flights rather than 6
#Also randomly incomplete flights last year

#ENT is a normal individual event
#-OR, Projects, Plans, IMC-: each event can have 2 groups of 1-3 at most
#x Selling: each event can have 2 individuals

#Need to announce that ENT and selling events are individual

#Finance
BFS = []
ACT = []
FTDM = []

#Marketing
BTDM = []
MTDM = []
STDM = []
AAM = []
ASM = []
MCS = []
FMS = []
SEM = []
RMS = []
BSM = []

#Business Admin
BLTDM = []
HRM = []

#Hospitality and Tourism
TTDM = []
HTDM = []
RFSM = []
HLM = []

#PFL
PFL = []

#Principles
PFN = []
PMK = []
PHT = []
PBM = []
POther = []

#Ent
EIB = []
EIP = []
IBP = []
ESB = []
EFB = []
ENT = []
EPP = []

#Written
IMCP = []
IMCS = []
IMCE = []
FCE = []
HTPS = []
PSE = []
BOR = []
BMOR = []
FOR = []
HTOR = []
SEOR = []

#Project
CSP = []
CMP = []
FLPP = []
LEP = []
PRP = []

#VBC
Fashion = []
Restaurant = []
Hotel = []
Sports = []
Finance = []
Accounting = []
Retail = []


Other = []
Dictionary = {}
NameList = []


with open("DECAFlight.csv") as fileIn:

    reader = csv.reader(fileIn)
    fileIn.readline()
    for line in reader:
        #print(line[0])
        comment = "";
        
        name = str(line[0]).lower() + " " + str(line[1]).lower()
        NameList.append(name)
        grade = line[2]
        years = line[3]
        choice = []
        
        for i in range(4,7):
            #print(i)
            event = ""
            while "(" not in event:
                event += line[i][-1:]
                line[i] = line[i][:-1]
                
            choice.append(event[::-1])
            #print(event[::-1])

        if ", " in line[7]:
            partnerName = line[7].split(", ")[0].lower()
            partnerGrade = line[7].split(", ")[1]
        else:
            partnerName = "X"
            partnerGrade = "X"
        #print(line[8])
        if "-" not in line[8] and line[8][1] == "t":
            experience = 0
        elif "-" not in line[8] and "where are you" not in line[8]:
            comment += str(line[8]) + "; "
            experience = -1
        elif line[8].split("-")[1][1] == "Q":
            experience = 1
        elif line[8].split("-")[1][1] == "R":
            experience = 2
        elif line[8].split("-")[1][1] == "P":
            experience = 3
        elif line[8].split("-")[1][1] == "O":
            experience = 4
        elif line[8].split("-")[1][1] == "M":
            experience = 5
        elif line[8].split("-")[1][1] == "T":
            experience = 6
        elif line[8].split("-")[1][1] == "I":
            experience = 7
        else:
            print(name)
            print(line[8])
            experience = -1
            print("Liar")
        comment += str(line[9])

        if line[10][0] == "N":
            pass            
        elif line[10][4] == "F":
            Fashion.append(str(name.title()) + "{" + str(line[11]) + "}")
        elif line[10][6] == "s":
            Restaurant.append(str(name.title()) + "{" + str(line[11]) + "}")
        elif line[10][4] == "H":
            Hotel.append(str(name.title()) + "{" + str(line[11]) + "}")
        elif line[10][4] == "S":
            Sports.append(str(name.title()) + "{" + str(line[11]) + "}")
        elif line[10][4] == "P":
            Finance.append(str(name.title()) + "{" + str(line[11]) + "}")
        elif line[10][4] == "A":
            Accounting.append(str(name.title()) + "{" + str(line[11]) + "}")
        elif line[10][4] == "R":
            Retail.append(str(name.title()) + "{" + str(line[11]) + "}")
        else:
            print(ERROR)
        
        Dictionary[name] = [grade, years, choice[0], choice[1],choice[2], experience, partnerName,partnerGrade,comment]
        

    #limit = len(NameList) / (33 + 2*7)
    limit = 7
    for i in range(7,-2,-1):
        for name in NameList:
            if Dictionary[name][5] == i:
                for k in range(2,5):
                    chapter = Dictionary[name][k]
                    if chapter[-4:-1] == "TDM":
                        #Teams
                        if Dictionary[name][6] in NameList and Dictionary[Dictionary[name][6]][6] == name:
                            #Finance
                            if chapter == "(FTDM)" and len(FTDM) < limit*2:
                                FTDM.append(str(name) + " " + str(chapter))
                                FTDM.append(str(Dictionary[name][6]) + " " + str(chapter))
                                NameList.remove(Dictionary[name][6])
                                Dictionary[name][6] = "X"
                                break
                            #Marketing
                            elif chapter == "(BTDM)" and len(BTDM) < limit*2:
                                BTDM.append(str(name) + " " + str(chapter))
                                BTDM.append(str(Dictionary[name][6]) + " " + str(chapter))
                                NameList.remove(Dictionary[name][6])
                                Dictionary[name][6] = "X"
                                break
                            elif chapter == "(MTDM)" and len(MTDM) < limit*2:
                                MTDM.append(str(name) + " " + str(chapter))
                                MTDM.append(str(Dictionary[name][6]) + " " + str(chapter))
                                NameList.remove(Dictionary[name][6])
                                Dictionary[name][6] = "X"
                                break
                            elif chapter == "(STDM)" and len(STDM) < limit*2:
                                STDM.append(str(name) + " " + str(chapter))
                                STDM.append(str(Dictionary[name][6]) + " " + str(chapter))
                                NameList.remove(Dictionary[name][6])
                                Dictionary[name][6] = "X"
                                break

                            #Business Admin
                            elif chapter == "(BLTDM)" and len(BLTDM) < limit*2:
                                BLTDM.append(str(name) + " " + str(chapter))
                                BLTDM.append(str(Dictionary[name][6]) + " " + str(chapter))
                                NameList.remove(Dictionary[name][6])
                                Dictionary[name][6] = "X"
                                break

                            #Hospitality and Tourism
                            elif chapter == "(HTDM)" and len(HTDM) < limit*2:
                                HTDM.append(str(name) + " " + str(chapter))
                                HTDM.append(str(Dictionary[name][6]) + " " + str(chapter))
                                NameList.remove(Dictionary[name][6])
                                Dictionary[name][6] = "X"
                                break
                            elif chapter == "(TTDM)" and len(TTDM) < limit*2:
                                TTDM.append(str(name) + " " + str(chapter))
                                TTDM.append(str(Dictionary[name][6]) + " " + str(chapter))
                                NameList.remove(Dictionary[name][6])
                                Dictionary[name][6] = "X"
                                break
                            else:
                                pass
                        
                    elif chapter[1:3] == "Pr" and Dictionary[name][1] == "0":
                        #Principles
                        '''
                        if chapter[15] == "F" and len(PFN) < limit:
                            PFN.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter[15] == "M" and len(PMK) < limit:
                            PMK.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter[15] == "H" and len(PHT) < limit:
                            PHT.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter[15] == "B" and len(PBM) < limit:
                            PBM.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        '''
                        if k == 4:
                            POther.append(str(name) + " (" + str(Dictionary[name][0]) + "): " + str(Dictionary[name][8]))
                            break

                    elif chapter == "(HRM)":
                        #Business Admin
                        if len(HRM) < limit:
                            HRM.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        
                    elif chapter == "(PFL)":
                        #PFL
                        if len(PFL) < limit:
                            PFL.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        
                    elif chapter[1:2] == "E" or chapter == "(IBP)":
                        #Ent
                        #done
                        if chapter == "(EIB)" and len(EIB) < 3:
                            EIB.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #done
                        elif chapter == "(EIP)" and len(EIP) < 4:
                            EIP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #1 more
                        elif chapter == "(IBP)" and len(IBP) < limit:
                            IBP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #done
                        elif chapter == "(ESB)" and len(ESB) < 5:
                            ESB.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #empty
                        elif chapter == "(EFB)" and len(EFB) < limit:
                            EFB.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(ENT)" and len(ENT) < limit:
                            ENT.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #done
                        elif chapter == "(EPP)" and len(EPP) < limit:
                            EPP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break

                    elif chapter[-2:-1] == "P" and chapter != "(IMCP)":
                        if chapter == "(CSP)" and len(CSP) < limit:
                            CSP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(CMP)" and len(CMP) < limit:
                            CMP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(FLPP)" and len(FLPP) < limit:
                            FLPP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(LEP)" and len(LEP) < limit:
                            LEP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(PRP)" and len(PRP) < limit:
                            PRP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        
                    elif chapter[-2:-1] == "E" or chapter[-3:-1] == "OR" or chapter[1:3] == "IM" or chapter == "(HTPS)":
                        #Written
                        if chapter == "(BOR)" and len(BOR) < limit:
                            BOR.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(BMOR)" and len(BMOR) < limit:
                            BMOR.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(FOR)" and len(FOR) < limit:
                            FOR.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #2 so far
                        elif chapter == "(HTOR)" and len(HTOR) < 3:
                            HTOR.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #2 so far
                        elif chapter == "(SEOR)" and len(SEOR) < 3:
                            SEOR.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #2 so far
                        elif chapter == "(IMCP)" and len(IMCP) < 3:
                            IMCP.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(IMCS)" and len(IMCS) < limit:
                            IMCS.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(IMCE)" and len(IMCE) < limit:
                            IMCE.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(FCE)" and len(FCE) < 2:
                            FCE.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        #2 So far
                        elif chapter == "(HTPS)" and len(HTPS) < 2:
                            HTPS.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(PSE)" and len(PSE) < 2:
                            PSE.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break 
                        
                    elif chapter == "(BFS)" or chapter == "(ACT)":
                        #Finance
                        if chapter == "(BFS)" and len(BFS) < limit:
                            BFS.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(ACT)" and len(ACT) < limit:
                            ACT.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        
                    elif chapter[1:2] == "H" or chapter == "(RFSM)":
                        #HandT
                        if chapter == "(HLM)" and len(HLM) < limit:
                            HLM.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(RFSM)" and len(RFSM) < limit:
                            RFSM.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        
                    elif "M" in chapter or chapter == "(RMS)":
                        #Marketing
                        if chapter == "(AAM)" and len(AAM) < limit:
                            AAM.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(ASM)" and len(ASM) < limit:
                            ASM.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(RMS)" and len(RMS) < limit:
                            RMS.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(MCS)" and len(MCS) < limit:
                            MCS.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(FMS)" and len(FMS) < limit:
                            FMS.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(SEM)" and len(SEM) < limit:
                            SEM.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                        elif chapter == "(BSM)" and len(BSM) < limit:
                            BSM.append(str(name) + " " + str(chapter))
                            Dictionary[name][6] = "X"
                            break
                    else:
                        print("ERROR")
                        print(chapter)
                    if k == 4:
                        Other.append(str(name))
                        Dictionary[name][6] = "X"

print("\nFinance")
print(BFS)
print(ACT)
print(FTDM)

print("\nMarketing")
print(BTDM)
print(MTDM)
print(STDM)
print(AAM)
print(ASM)
print(MCS)
print(FMS)
print(SEM)
print(RMS)
print(BSM)

print("\nBusiness Admin")
print(BLTDM)
print(HRM)

print("\nHospitality and Tourism")
print(TTDM)
print(HTDM)
print(RFSM)
print(HLM)

print("\nPFL")
print(PFL)

print("\nEnt")
print(EIB)
print(EIP)
print(IBP)
print(ESB)
print(EFB)
print(ENT)
print(EPP)

print("\nWritten")
print(IMCP)
print(IMCS)
print(IMCE)
print(FCE)
print(HTPS)
print(PSE)
print(BOR)
print(BMOR)
print(FOR)
print(HTOR)
print(SEOR)

print("\nProjects")
print(CSP)
print(CMP)
print(FLPP)
print(LEP)
print(PRP)


print("\nVBC")
print(str(Fashion)+"\n")
print(str(Restaurant)+"\n")
print(str(Hotel)+"\n")
print(str(Sports)+"\n")
print(str(Finance)+"\n")
print(str(Accounting)+"\n")
print(Retail)


print("\nOther")
print(Other)

'''
print("\nPrinciples")
print(PFN)
print(PMK)
print(PHT)
print(PBM)

for i in POther:
    print(i+"\n")
print(len(POther))
print(Dictionary)
print(NameList)
'''

    
                            
 
            
            

        
        
        
            
        
