#Globals

alpha = [
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
]

# Functions

def Check_Txt (String): 
    for letter in String.upper():
        if letter not in alpha and letter != " ":
            raise Exception ("Invalid Text")

def Split_String_Into_Letter_Array(String): 
    Output_Array = []
    for Letter in String.upper():
        Output_Array.append(Letter)
    return Output_Array
    
def Encrypt(Text_Array,KeyArray):
    Text_Index_Int = 0
    Key_Index_Int = 0
    Final_Index_Int = 0
    Final_String = ""
    i = 0
    Output_Array = []
    for Letter in Text_Array:
        if i >= len(KeyArray):
            i=0
        if Letter in alpha:
            Text_Index_Int = alpha.index(Letter)
            Key_Index_Int = alpha.index(KeyArray[i])
            Final_Index_Int = Text_Index_Int + Key_Index_Int
            while Final_Index_Int < 0:
                Final_Index_Int = Final_Index_Int + len(alpha)
            Output_Array.append(alpha[Final_Index_Int])
        else:
            Output_Array.append(" ")
        i = i + 1
    Final_String = "".join(Output_Array)
    return Final_String
  
# Call Stack

Input_Text = input("Please Enter Text: ")
Input_Key = input("Pleas Enter Key: ")
Split_Text = []
Split_Key = []
Check_Txt(Input_Key)
Check_Txt(Input_Text)
Split_Text = Split_String_Into_Letter_Array(Input_Text)
Split_Key = Split_String_Into_Letter_Array(Input_Key)
print("Encrpted Text: "+Encrypt(Split_Text,Split_Key))
