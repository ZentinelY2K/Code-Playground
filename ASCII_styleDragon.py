# TODO: Dragon blowing fire ACII Art by Axel Quinonez
#Color section: This section will be used to store all colors needed 
green = "\u001b[38;5;28m" #Dragon's main color
red = "\u001b[38;5;196m" #Fire color palette
yellow = "\u001b[38;5;220m" #secondary color
orange = "\u001b[38;5;202m" #Fire color palette
purple = "\u001b[38;5;141m"#This is only for the eye
reset = "\u001b[0m"
#Color section: Closing

#Variable Section: / This section contains all variables we'll need to use/
slash_clockwise = "/"  #we'll recall them as SC for efficiency
slash_counterclockwise = "\\" #we use an escape sequence to make it work since '\' its a built-in function + #we'll recall them as SCC for efficiency

slash_straight = "|" #we'll recall them as SS for efficiency
quotes = '"' #we'll recall them as QU for efficiency
dots = '.' #we'll recall them as DO for efficiency
commas = "," #we'll recall them as CO for efficiency
fire_balls = "*" #we'll recall them as FB for efficiency
space = " " #just for me to ease the separation of characters
single_quotes = "'"
parentheses = "("
eye = f"{purple}/@ {reset}"
#README
#we'll be using IND and OUT, which stand for index and ouput, if its assigned as an "IND" it means its in preparation whereas an output just means its going to be sent to the print statemen
#We'll also use numeration for variables that essentially do the same thing but need certain accomodations, or are simply part of the same dragon's body part and need little to no change (e.g:n1)
    
#Functionality Section: Using the variables we'll use built-in functions for a good and organized output
FirstlineSC_OUT = f"{slash_clockwise:>26}{space*15}{slash_clockwise}"
slashSC_in_row_OUT = "/\n"
moustache_slashSS_OUT = f"{slash_straight}"
moustache = "_ _ _"
moustache_slashCC_OUT = f"{slash_counterclockwise}{moustache}{slash_clockwise}"
singleChinHair_OUT = "'"
#Print statement section: This section will store all the output /the dragon/
print(f"{yellow}{FirstlineSC_OUT}")
print(f"{slash_clockwise:>25}'{dots:>5}{commas*4:>3}{space*3}.{slash_clockwise}")
print(f"{slash_clockwise:>24}';'{commas:>10}{slash_clockwise}")
print(f"{slash_clockwise: >23}{space*1}{slash_clockwise}{space *5},,{slash_clockwise*2},`'`")
print(f"{'(':>22}{space}{commas*2} '_, {space*3}{commas*3}'` ` ")
print(f"{slash_straight:>22}{space*4}{reset}{eye}{green} {space*2}{commas*3:>3}{space};{quotes} ` ") 
print(f"{slash_clockwise:>21}    .     ,''/'`,``") 
print(f"{slash_clockwise:>20}   .      ./,  `,,`;")
print(f"{dots + commas:>18}{slash_clockwise:}  .      ,-,',`,,/''\,'")
print(f"{moustache_slashSS_OUT:>18}  /;   ./,,'`,,''{slash_straight}{space*3}{slash_straight}")
print(f"{moustache_slashSS_OUT:>18}      /    ','   /   |")
print(f"{moustache_slashCC_OUT:>24}'  '      {slash_straight}{space*3}{slash_straight}")
print(f"{singleChinHair_OUT:>20}{commas*2:>0}'{space*3}{slash_straight}{space*6}{slash_clockwise}{space*4}`{slash_counterclockwise}`")
print(f"{slash_clockwise:>27}{space*5}{slash_straight}{space*7}~{slash_counterclockwise}")
print(f"{single_quotes:>26} :    {parentheses} ")
print(f"{orange}{slash_straight:>23}{red}{fire_balls*4}{slash_counterclockwise}")
print(f"{slash_straight:>23}{orange}{fire_balls*5}{slash_counterclockwise}")
print(f"{slash_straight:>23}{red}{fire_balls*6}{slash_counterclockwise}")
print(f"{slash_straight:>23}{orange}{fire_balls*7}{slash_counterclockwise}")
print(f"{slash_straight:>23}{red}{fire_balls*8}{slash_counterclockwise}")
print(f"{slash_straight:>23}{orange}{fire_balls*9}{slash_counterclockwise}")
print(f"{slash_straight:>23}{red}{fire_balls*10}{slash_counterclockwise}")
print(f"{slash_straight:>23}{orange}{fire_balls*11}{slash_counterclockwise}")
print(f"{slash_straight:>23}{red}{fire_balls*12}{slash_counterclockwise}")
print(f"{slash_clockwise:>22}{orange}{fire_balls*13}{slash_counterclockwise}")
print(f"{slash_clockwise:>21}{red}{fire_balls*15}{slash_counterclockwise}")
print(f"{slash_clockwise:>20}{orange}{fire_balls*17}{slash_counterclockwise}")
print(f"{slash_clockwise:>19}{red}{fire_balls*19}{slash_counterclockwise}")
print(f"{slash_clockwise:>18}{orange}{fire_balls*21}{slash_counterclockwise}")
print(f"{slash_clockwise:>17}{red}{fire_balls*23}{slash_counterclockwise}")
print(f"{slash_clockwise:>16}{orange}{fire_balls*25}{slash_counterclockwise}")
print(f"{slash_clockwise:>15}{red}{fire_balls*27}{slash_counterclockwise}")
print(f"{slash_clockwise:>14}{orange}{fire_balls*29}{slash_counterclockwise}")
print(f"{slash_clockwise:>13}{red}{fire_balls*31}{slash_counterclockwise}")
print(f"{slash_clockwise:>12}{orange}{fire_balls*33}{slash_counterclockwise}")