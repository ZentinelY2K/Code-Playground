ip_addresses = ['192.168.1.1','172.18.3.3','12.12.12.12']
class ipv4: 
    """
    This class sorts IPV4 addresses into public or private given a list
    """
    def __init__(self):
        self.ipv4 = 'Default'
        self.counter_private = 0
        self.counter_public = 0
        self.empty_list = []
    def sort(self,list):
        for i in range(len(list)):
            if list[i].startswith('192.168') or list[i].startswith('10'):
                self.counter_private += 1
                self.empty_list.append(list[i])
            for x in range(16,31):
                x = str(x)
                if list[i].startswith(f'172.{x}'):
                   self.counter_private += 1
                   self.empty_list.append(list[i])
                   
                
        return print(f"Total number of private addresses: {self.counter_private} and those are {self.empty_list}")
        
ipv4 = ipv4()
ipv4.sort(ip_addresses)