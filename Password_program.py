###############################################
################
### This Program Assigns a Score and Strength#
### to a Password ############################
###############################################


## Importing APIs'

import random
import re

    
### Display Menu
def Display_Menu():
    print("\nPlease choose an option")
    print("1.Enter a Password")
    print("2.Ask the Computer to Generate Password")
    print("3. Quit")

# User Entry of Password

def Enter_Password():
    Pswd = input("Please enter a Password: ")


    Validation_Check = Password_Validation(Pswd)
    if Validation_Check == False:
        main()
    else:
        Score_from_Addition = Addition_Score(Pswd)
        Score_from_Subtraction = Subtract_Points(Pswd, Score_from_Addition)
        Strength_of_Password = Password_Strength_Assign(Score_from_Subtraction)
        final_output(Pswd,Score_from_Subtraction,Strength_of_Password)
        
# Validating the Password 
def Password_Validation(Pswd):
    Capitals_ASCII = list(range(65,91))
    Lowercase_ASCII = list(range(97,123))
    Digits_ASCII = list(range(48,58))
    Symbols_ASCII =[33,36,37,38,42,40,41,95,94,45]
    Allowed_Characters = (Capitals_ASCII + Lowercase_ASCII + Digits_ASCII + Symbols_ASCII)

    length_of_password = len(Pswd)
    validate = True
    if length_of_password <8 or length_of_password >24:
        
        validate = False
        print("Password should be between 8 and 24 characters")
        return(validate)
    
    for i in range(0,length_of_password):
        ascii_value=ord(Pswd[i])
        
    if(ascii_value not in Allowed_Characters):
        validate = False
        print("Password contains characters that it should not")
        return(validate)
        
# Exiting Code
def quit():
    print("Exiting code")

##### Adding Score#####
def Addition_Score(Password):
    Score_Add = 0
    Score_Add = Score_Add + len(Password)

    lower_case = re.match(".*[a-z].*",Password)
    if lower_case:
        Score_Add = Score_Add + 5
        

    upper_case = re.match(".*[A-Z].*",Password)
    if upper_case:
        Score_Add = Score_Add + 5
        
    digits = re.match(".*[0-9].*",Password)
    if digits:
        Score_Add = Score_Add + 5
     

    symbols = re.match(".*[!,$,%,^,&,*,(,),-,_,=,+,].*",Password)
    if symbols:
        Score_Add = Score_Add + 5
       
    if(upper_case and lower_case and digits and symbols):
       Score_Add = Score_Add + 10
       
       
    return(Score_Add)





#### Subtract Score
def Subtract_Points(password, New_Score_Add):

     Set_of_symbols = {'!','$','%','^','&','*','(',')','-','_','=','+'}
     keyboard_firstrow = "QWERTYUIOP"
     keyboard_secondrow = "ASDFGHJKL"
     keyboard_thirdrow="ZXCVBNM"
     Score_Add = New_Score_Add

     is_lower = password.isalpha() and password.islower()
     if   is_lower:
          Score_Add = Score_Add - 5
          print(Score_Add)


     is_upper = password.isalpha() and password.isupper()
     if   is_upper:
          Score_Add = Score_Add - 5
          print(Score_Add)

     is_digit = password.isdigit()
     if   is_digit:
          Score_Add = Score_Add - 5
          print(Score_Add)



     Set_password = set(list(password))
     if ((Set_password | Set_of_symbols)== Set_of_symbols):
          Score_Add = Score_Add - 10
          


###  Check for 3 consecutive letters matching on keyboard
     count_consecutive_letters= 0
     
     S1 = 0
     for  j in range(len(keyboard_firstrow)-2):
          for i in range(len(password)-2):
                 if (password[i:i+3].upper()== keyboard_firstrow[j:j+3].upper()):
                     count_consecutive_letters =count_consecutive_letters +1
                     

     for  j in range(len(keyboard_secondrow)-2):
          for i in range(len(password)-2):
                 if (password[i:i+3].upper()== keyboard_secondrow[j:j+3].upper()):
                     count_consecutive_letters =count_consecutive_letters +1
                    

     for  j in range(len(keyboard_thirdrow)-2):
          for i in range(len(password)-2):
                 if (password[i:i+3].upper()== keyboard_thirdrow[j:j+3].upper()):
                     count_consecutive_letters =count_consecutive_letters +1
                    

     print("No of consecutive letters ", count_consecutive_letters)
     S1 =count_consecutive_letters * 5

     Score_Add = Score_Add - S1
     return(Score_Add)   
    


## Associating Score_Add with Strength of Password
def Password_Strength_Assign(n):

     if (n >  20):
          Strength = "STRONG"
     elif ( n <= 0):
          Strength = "WEAK"
     else:
          Strength = "MEDIUM"

     return(Strength)


# Display of Final Details 
def final_output(password,New_Score_Add,Assigned_Strength):

     print("\nThe Password is: ", password, " And the Score is ", New_Score_Add, " And the Strength is", Assigned_Strength)
     
# Random Password Generated
def Generate_Random_Password():
    j = random.randint(8,12)
    new_password = ""

    letters =[]
    for w in list(range(65,91)):
        letters.append(chr(w))


    for x in list(range(97,123)):
        letters.append(chr(x))


    for y in list(range(48,58)):
        letters.append(chr(y))

    symbols_code = [33,36,37,38,42,40,41,95,94,45]
    for z in symbols_code:
         letters.append(chr(z))
         
    
    for i in range(0,j):
         generated_letter = random.choice(letters)
         new_password = new_password + generated_letter
  
    Score_Add = Addition_Score(new_password)    
    New_Score_Add = Subtract_Points(new_password, Score_Add)
    New_Strength = Password_Strength_Assign(New_Score_Add)
    
    if (New_Strength !="STRONG"):
        Generate_Random_Password()

    final_output(new_password,New_Score_Add,New_Strength)
         

# Display Choices to User
def main():
     try:
         Display_Menu()
         choice = input("Select an option ")
         if choice == '3':
            quit()
         if choice == '1':
            Enter_Password()
         if choice == '2':
            Generate_Random_Password()
     except:
         print("There is an error. You need to fix it ")
     finally:
         print("Exiting program")
if __name__== "__main__":
  main()



