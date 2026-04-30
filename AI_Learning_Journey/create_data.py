import csv
import random as rm


def build_private_ip_address():

    choose_first_octet = [192,172,10]
    first_octet = rm.choice(choose_first_octet)
    second_octet = 0
    third_octet = 0
    fourth_octet = 0

    if first_octet == 192:
       second_octet = 168

    elif first_octet == 172:
       random_range_16_to_31 = rm.randint(16,31)
       second_octet = random_range_16_to_31

    elif first_octet == 10:
       second_octet = rm.randint(0,255)
    
    third_octet = rm.randint(0,255)
    fourth_octet = rm.randint(0,255)

    return first_octet,second_octet,third_octet,fourth_octet

def ensure_no_private_publics():
   first,second,third,fourth = rm.randint(0,255),rm.randint(0,255),rm.randint(0,255),rm.randint(0,255)
   private_ips_first_octet = [192,172,10]
   for i in range(len(private_ips_first_octet)):
      if private_ips_first_octet[i] == first:
         not_yet = rm.randint(0,255)
         for i in range(len(private_ips_first_octet)):
            if private_ips_first_octet[i] == not_yet:
               first = rm.randint(0,255)
            else:
               first = not_yet
      else:
         continue
    
   return first,second,third,fourth

with open ("/home/zentinely2k/Documents/Y2K-Zone/Code-Playground/AI_Learning_Journey/DataBase.csv","w",newline="") as f:
    write = csv.writer(f)
    for i in range(10000):
      first,second,third,fourth = build_private_ip_address()
      lol1,lol2,lol3,lol4 = ensure_no_private_publics()
      write.writerow([first,second,third,fourth,1]) #private ip addresses
      write.writerow([lol1,lol2,lol3,lol4,0]) # any public



