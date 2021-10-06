"""
Write a program for lottery simulation. Generate 6 digit random number. Allow user to input only 6 digit number.
If all the 6 digits matches then user wins 100000,
if 5 digits match in sequence then user wins 85000,
if 4 digits match in sequence then user wins 50000,
if 3 digits matches in sequence then user wins 20000,
if 2 digit matches user wins 2000.
"""

class Lottery:
    def __init__(self,name="", num=000000):
        self.__name = name
        self.__number = num
        
    def luckyNum(self):
        import random
        self.__lucky_no = random.randrange(100000, 999999)
        string = str(self.__lucky_no)
        
        self.__lottery_no =[]
        for i in string:
            self.__lottery_no.append(i)
        
    def lotteryNum(self):
        string = str(self.__number)
        
        self.__user_lottery_no = []
        for i in string:
            self.__user_lottery_no.append(i)
            
    def verifyLotteryNum(self):
        count = 0
        
        import numpy as np
        self.__ans_bool = ((np.array(self.__lottery_no) == np.array(self.__user_lottery_no)))
        self.__ans_bool= [i for i, x in enumerate(self.__ans_bool) if x]
        
        size = len(self.__ans_bool)

        for i in range(size):
            for j in range(i+1, size): 
                temp = self.__ans_bool[j]
                temp -= 1
                if(self.__ans_bool[i] == temp):
                    count +=1
                else:
                    pass
                    #print("None Numbers matched in Sequences.......")
                    
        self.__result = count
                    
    def display(self):
        print("\n\n|-------------Result of Lottery--------------|")
        print("\nName = ",self.__name)
        print("Your Lottery No. = %s\n\n"%(self.__number))
        
        if(self.__result == 5):
            print("Congratulation You have Won \"Rs 100000/-\" ")
        elif(self.__result == 4):
            print("Congratulation You have Won \"Rs 85000/-\" ")
        elif(self.__result == 3):
            print("Congratulation You have Won \"Rs 50000/-\" ")
        elif(self.__result == 2):
            print("Congratulation You have Won \"Rs 20000/-\" ")
        elif(self.__result == 1):
            print("Congratulation You have Won \"Rs 2000/-\" ")
        elif(self.__result == 0):
            print("You lost the lottery \U0001f614; Better luck for next time..... ") #\U0001f614 = sad emoji
            
            
# =============================================================================
# -----------------------------Driver code-------------------------------------
# =============================================================================
name = input("Enter your name = ")
num = int(input("Enter your six digit Lottery no. = "))
    
n1 = Lottery(name,num)
#n1 = Lottery("A",454545)
n1.luckyNum()
n1.lotteryNum()
n1.verifyLotteryNum()
n1.display()
       
        
        
        
        
