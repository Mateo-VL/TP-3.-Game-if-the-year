import mapping
import human
import actions
import player
import items         #cambiar los imports para entrega final
#from src.templates.oop.human import Human
#from src.templates.oop.items import Item
#import src.templates.oop.actions as actions


ROWS = 25
COLUMNS = 80
DUNGEON = mapping.Dungeon(ROWS, COLUMNS)   #pedir parametros para ver longitud y ver que no pase limites
PLAYER = human.Human('Mateo', DUNGEON.dungeon[DUNGEON.level].index(mapping.STAIR_UP))
GNOMES = [player.Gnome('Gnome', DUNGEON.find_free_tile()) for _ in range(len(DUNGEON.dungeon))]

SWORD= items.Sword("Sword", "/", 10, 20, DUNGEON.find_free_tile())
AMULET= items.Amulet("Amulet", '"', DUNGEON.dungeon[2].find_free_tile())
PICKAXE= items.PickAxe("Pickaxe", "(", DUNGEON.find_free_tile())

rows= DUNGEON.rows
columns= DUNGEON.columns

if __name__ == "__main__":
   
    game = True 
    DUNGEON.add_item(PICKAXE, 1, PICKAXE.loc())
    DUNGEON.add_item(SWORD, 1, SWORD.loc())
    DUNGEON.add_item(AMULET, 3, AMULET.loc())
    DUNGEON.render(PLAYER, GNOMES[DUNGEON.level], DUNGEON.level)

    turns=0
    while game and PLAYER.alive==True:
        turns +=1
        
        game = actions.use_turn(PLAYER, GNOMES[DUNGEON.level], DUNGEON, game)
        PLAYER.pickup(DUNGEON.get_items(PLAYER.loc()))      
        DUNGEON.render(PLAYER, GNOMES[DUNGEON.level], DUNGEON.level)
    if PLAYER.treasure == True:
        print('''MMMMMMMMMMMMMMMMMMMMMMMMMMMWMWWNXXXXXNXXNNNWWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWMWNKOxolc::::cccclloxO0XNWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWN0dl:;,,;;;;;,;c:,;;;;;cldOKNWWWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXko:,;;;::::ccc:clc:ccccccclldk0XWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNOl;;;::cccclloollllllooooodxxxddxxONMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWKd:,,;:cdxxooooolllllooooddxk0KXXK0kkKWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKo:;;;:ldkOxllodolllllodddxkO0XWWWWNKOOKNWMMMMMMMMMMM
MMMMMMMMMMMMMMMW0o::;;:lododdocclccllollcloxOKNNKNWNXXKOO0NMMMMMMMMMMM
MMMMMMMMMMMMMMMKoc:::cloooc;;;;;::cllc:cloco0NWNO0NNNWXK0OKWWMMMMMMMMM
MMMMMMMMMMMMMMNxcc:::cool:,',,',,:lccccclolckNNNN0KXXWNX0kOXWMMMMMMMMM
MMMMMMMMMMMMMMXocc:;:c:,'..   ;cclccc:clllolok0XNX0KNNNNKOkKWMMMMMMMMM
MMMMMMMMMMMMWMKlcc:;;:,....'';llllcccclol:lxxxOXNX00KXXX00O0NMMMMMMMMM
MMMMMMMMMMMWNXOl:c:;;,'....',lccccccloodolxOkockNNXKX000OOOOKNWWMMMMMM
MMMMMMMMMWWWkc:;;:::;,'....'':llcccloddddddxo;,c0WNXKXK000OxdkNMMMMMMM
MMMMMMMMMMWNxcc::::::;;,,,;::coolcloddxxxddoc:;l0WWNNXXKK0kdldKMMMMMMM
MMMMMMMMWWMNd;:::::::cllollllodlccoxxxxxdddoc:lkXNNNNXX0OkxdldXWMMMMMM
MMMMMMMMMMMW0ol:,;::::loddddddooodkkxdddoll:cllkXXNNXK0kkkxxxKWMMMMMMM
MMMMMMMMMMMWNOdl'',;::coddxkkxdodxkxdloolc:cdocxKKXX0O0OxddxONMMMMMMMM
MMMMMMMMMMMMW0dl,.'',;:lodxkxddodddoolcc:;cxOdcd0KKOkkxocoxOKWMMMMMMMM
MMMMMMMMMMMMMXxl:,,'.',;:lodooooolccc:;,,ckK0xco0X0ddocclodkXWMMMMMMMM
MMMMMMMMMMMMWWOdl,''....';:ccccc:;,,,'';oO0OkkllOXKxlodoc:lONMMMMMMMMM
MMMMMMMMMMMMMMKxo;''......',,     .. :ok0KKOxkxokXXxoO0x:,lKWMMMMMMMMM
MMMMMMMMMMMMMMNkdl,,,'.......... ;ldxO0KKKKOkOOddKXOxkddocxXWMMMMMMMMM
MMMMMMMMMMMMMMWKxl;:lllc:::;;;:clx0KKK0KKKKOkOOxlxK0xdoclxOXWMMMMMMMMM
MMMMMMMMMMMMMMMNOo:;cdxxxxxxdxxxxxkxk0XXK00Okk0kooO0xollldONWMMMMMMMMM
MMMMMMMMMMMMMMMWKxc;;lddddddddxxdxxxdxOKK00OOO0Oxlx0kdlldOKWMMMMMMMMMM
MMMMMMMMMMMMMMMMNkl:,:looooooodddxxddxdxOKK0OOOOxook0kdokKNWMMMMMMMMMM
MMMMMMMMMMMMMMMMWOol;;:ldolllllooddddxdddOKK0OOOkdooOKK00XNWMMMMMMMMMM
MMMMMMMMMMMMMMMMWKdlcc::lolcllloodddodddddk000O0kdolxKXK00NWMMMMMMMMMM
MMMMMMMMMMMMMMMWWWOlccc;:llclolllloooldxdodkO00Oxolld0K00KNMMMMMMMMMMM
MMMMMMMMMMMMMMMMWWNkcclc;:clooolllccldddxdlokOOkllclxO00KNWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWXdccl:;:lllcllllcldooddolx00xlc:lk000NWMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMKl:lolcccccccoooooloddodk0klcc:d0K0XWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWk::lolc:::;:cccclllodddkko:::oOK0XWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMKl;:looccc:::ccc:clloddxo;,;lOK0KWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWMNx;;:cllolccc:::cc:cool:;;;lOK00XWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWWOl;;:looolllooooololc;;;:oOXXKXWWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWWKdc;;clooodxdoooddol::::dKXXXXXWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNOoc::coooooddxdol::::lxKKKO0KNWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXkoc:::clooodxxdl::cok00OxoOXNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMN0xc::::::clllccldkOO0koco0NWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWNkl::::::c::clxOOkkdlclkXWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNklllllcccldkkkxoccclxKWWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMW0llooclloxkkxoc::lx0XWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWOlcccldxkkdlc:coxOXNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWxcccoxxxdl:::ok0KKNWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWOc:oddolcc:loxOKXXXNWWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWW0lcooolccloddddk0KXNNXNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWXdclc:cloooooodkOOKXNNXXWMWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNkc:::clllcccldxxxOKXXXXKXWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMM0:;:::::ccccloooxOKXXXXKOkKWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXd,..   ;;:ccllccdOK0OOkdloOXWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWKo;,... ......    ,:cccccloxO0XWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWKo;;;;,,'..........';codkOO000OOXWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXd::;,;;:::::,,,,:llld0KKXNXKK0kxkXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWk:;;;,;;:c::c;;cclddoxO00KNXKKKOxd0WMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMXl.',,,;::;;:;;:::lllodOKOKXKK0OxookNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWK:.....',;,'';;:c:::cloxOK00OOxocclkNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNx'..........','' ,,::;:ldolcccccld0WMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWNx;'.................'',;:::codkOXWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWKxl:;;;,,'..'''''',,;:lodkOKNNWWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWNKOkkxdoooooooooddxOKXNNWWWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWMMMMWWNXNNNNNNNNNNWWWWWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMM''')
    else:
        print('''                                                         ........................................'''''',,,,,,;;;;:::ccll
                                                              ..................................     ,,,,,;;;;::::cccllo
                                                                  ........   .................'''''',,,,;;;;;:::cccllllo
                                      ......                         .....',;;,,.............     ,,,,;;;;;:::cccclllooo
                                      ...                           ........,,;:::;,........    ,,,,,;;;;:::cccclllooodd
                                        .......   .            ... ..........',,;codl:'....     ,,,,;;;;::cccclllloodddd
                                       ..''....................................',:lxO0d;..''  ,,,,,;;;:::cccllllooodddxx
                                     .',;:::;;;;,,,,,,,    ................... ,,:lxOXXO:   ,,,,;;;;:::ccclllloooodddxxx
                                   . ;:::cccccc::::::;;;,,,    ............... ,:lodO0XKdc; ,,,;;;::::ccclllloooddddxxxk
                                  .;:::c:ccccc:cccc:::;;;,,,''''''............,;cxO0OO00ko;',,;;;:::cccllllooooddddxxxkk
                         .       .,::::ccc::::::::::::::;;,,,,,,''  ......... ,:lxKNKOxkOo;,;,,;;:::cccllllooooddddxxkkk
                        ..      .,::::ccccccc:::::cc:::::;;;;;,,,,''  ........,:ld0NN0dx00kc,,,;:::ccclllloooodddxxxkkkO
                       ...     .';::cccccccccccccccccccc:;;;;;;;;,,,' '....... ;cdONN0dlxKNOl;;;:::cclllloooodddxxxxkkOO
                     . ..     ..;:ccccclllllllccccclcccc:::::;;;;;,,,' '.......,;o0NWKdccxKN0l;;::ccclllloooddddxxxkkkOO
                    ......   ..':ccclllllllllllcccccccccc:::::;;;;;,,,' '.......':ONWXxc:lkXN0l:::cccllloooddddxxxxkkOOO
                    ......  ...,clclllloooollllccclllcccccc:::;;;;;;,,,'  '......,xXWXkl:co0NN0l:ccclllooooddddxxxkkkOOO
                  .   ....  ...,cllloooooooooolccccllccccccc::;;;;;;;,,'  '......'oKNN0dcclxKWNOlccclllooodddddxxkkkOOO0
                 ...  .... ..'.,clllooooooooollccccccccc:cccc::;;;;;,,,  ''.......;ONNKxoodx0NWXdcccllloooodddxxxkkkOOO0
                 ........  ..'',:lloooooooooollcllccclccccccc::;;;;;,,'  '........'dXWXOxdxOKXWNklccllloooddddxxkkkOOO00
                .............',;:lloooooooooolllllccclcccccccc::;;;;,,'  '.........:OWNKOxxOKNWW0occlllooodddxxxkkkOOO00
                ...... ....,,,;;:clooooooooooollllccccccccccccc:::;;,,'  '........':OWNKOOOOKNWWKocllllooodddxxxkkkOOO00
                ..........';::::ccloooooooooooolllcc:cclccclllc:::;;,,''..........'c0WWXOk0KKNWW0ocllloooodddxxxkkkOO000
                 ...  ....,::::cclloooooodddddoollccccccccllllcc:::;,,,''........',o0WWXkx0XNNWW0ocllloooodddxxxkkkOO000
                 ..    ...,:::cccllloodddddddddooollccclllolllcc:::;,,,,'  ''....':kXWWNOdONWWWNOolllloooodddxxxkkkOO000
                       ...,:::cccllllodddddddooodooollllccooolccc::;,,,,,'' ''.'',lONWWW0xONWWWKdlllllooooddxxxkkkkOO000
                       ...,;::c:::;;;;:::clloooooooolcllc:lddocccc:;,''''''... .';lkXNWWKk0NWWNOollllloooodddxxxkkkOO000
                        .';;:::;,,' '.....',,,:ccclc:lolc::looc::;,,'...........'':x0NWWXk0NNNXxlllllllooodddxxxkkkOO000
                        .';;;;;;;:cc::;;;,,''..'',;;;looc;,;cc:,,'.....'',,,,' '..,cxKWWNOOXKXKdlllllllooodddxxxkkkOO000
                        .,;;;,;:clooodooolc:;,,,,;;:codol;'.''.......'',;:;;;,,' ',;:dKWNOk00K0occlllllooodddxxxkkkkOO00
             ...        .,;;;;:clllc::;;,.....',;:cloddol;'...........' '....'' '',;,;xNW0dkOkkdccccllloooddddxxxkkkOO00
            ......     ..,;:::cc:;'.',''...'''';:clooddol; .......... ,,,''''' '.' '',dNWKxkOxkdccccllloooodddxxxkkkOO00
           ....        ..,;:ccc::cccccc:;;,,,,,;clloooool;'.........',;;;;;,,'...''.',lKWKkxOOkocccclllloooddddxxxkkkOO0
           ....        ..,;:cccclooooddollcc::;:clooooolc;,..........',;;:;;,'....' ',c0WXOkO0Oo:ccllllllooodddxxxxkkOOO
           ....        ..';:cclllooddddddddolc:coooooool:;,...........'',,;,,,'''''',,l0NXkkOkOd:cccclllllooodddxxxkkkOO
           ....        ..';:cllooooddxddddollloddoooooolc;,............'',,,,,,' ',,,;l0W0dddoxxc:cccclllllooodddxxxkkkO
          .....        ..',:clloooodddddooooodxddoooooooc;,.............'',,,,,,,,,'',lKNkldd;ldl::cccccllllooodddxxxkkk
      .........         ..,;:cloooddddddddddddddooooollol:'..............'''''',,'' ',oKNxlkxccol:::cccccllllloodddxxxxk
      .........        ...';:cllloodddddddddddddooooolool:,...............''''''' ''.,lKN00Olodoc;:::ccccccllllooodddxxx
      .........         ..',:ccllloodddddddddxddooooooooc:,'...............''''''....'l0WNWO::do:;;:::::ccccclllooodddxx
      .........      . ...',;::clllodddddddddddoolloodddlc;''........................'lKWNWO;;oc,;;;;:::::cccclllooodddx
       .........   .......',;::cclloddddddddoooooollodxdol:,'.....................''.'lKWWWk;;:;;;;;;;;;::::cccllllooodd
          .................';::ccllooddddddollloooc:cloolc:,'.....................,' 'lKNNWk;,,,,,,,;;;;;;::::cccllllooo
         ..................',;:cclllooddddoooodoollccllcc:;,'....................',,',o0XNNd,,,,,,,,,,;;;;;;::::cccllllo
       ....................',;:ccclloooddooooooolllllll:,;;,..............''.....',,',lk0X0c,,,',,,,,,,,;;;;;;::::ccccll
       ....................',;:cccllloooooooollllllllol;';lc;,...................',,,:lox0x;','''''',,,,,,,;;;;;;:::cccl
       ....................'',;:ccclllollllllllllllcloc;,:ll:;''..................'';cc:od:'' '' '' '',,,,,,,;;;;;::::cc
         ...................',;:cccllllllcccccllllllllc;;:ccc:,' '............... ..,:;;c:'' .'' '' '' '',,,,,,;;;;;::::
          ..................',;::cclllccccccclllllollllc::;;;;''.................,'.,;,,;''....''''''''''''',,,,,,;;;;;:
       ......................',;:ccllllccc::::c:::;::;;;,'.......................,'.,;,''...........'' '' ' ' ',,,,,;;;;
        ......................',;::clllccccccclllccccc::;;;,,''.............''...''. ;, ..............''''''' '',,,,,,,,
               ................';;::cllccccccccllccccc::;;;,,,' '................'.',:;..................''''''' '',,,,,
                ...............',;;::cccccccccccccc:;;,,,,,,,,''...................,;c:....................'''''' '' ',,
                 ....... .......',;;::ccccccccccc::::;;;;,,,,,,''................. ,,cc ........................''''''''
                  ......  .......',;;::ccccllllccccccccccc::::;,, ................ ..co,............................'' '
                    ........ .....',;:::::ccllllccclllllccc:::;,,'...........   .....cx:.'............................''
                       ..      ..' ',;;;;;:cccllllccllllcc:::;;,''........    .......:Od..,'............................
                               ....' ',;;;;;::cccccllcc:;;,,;;,,'.........   ........:OO,.,:, ..........................
                               ....' ',,,,;;;::::::::::;,''''''''........  ..........:xk; .,lc;,'.......................
                               ..'''',,,,,,,;;;:;;;;;,,'''''............. ...... ....:do'  .:lc,''  '...................
                               ..',,'',,,,,,;;;;,,,'''''''...............         ...,l:.  .,cc;........'',,''..........
                               ..'',;,,,,;;;;;;,,,,,,,,' '................         ...,'.   .;c:,'..........,,;;;,'.....
                               ..'',;;;;;;;;::;;;;;,,' '  ................     .........     .,:, ..............,;::c:; 
                               ..',,,;:::::;;:::::;;,,,,,,,,' '.........    ...........      ..,,'..................,:ll
                                .',,;;;;:ccccc::::::;;,;;;:;;;,,''..............  . .      .  ...''....................'
                                .',,;;;::ccllllc:::::;;;;:::::;,'.................             .........................
                                 .,;;;;:::ccclllllc:;;;;:;;;;;,'....,,,.........               .........................
                                 .',;;;;::cccllloooll::;,,,,,'' ',;:;  .........                  ......................
                                  . ;;;;::ccclllooooollc,.. ,,,:cc:,''........ .          .            ....    .........
                                   .';;;::ccclllloooooc,..,;:::::;,''........            ...                    ........
                                   ..';;;::cccllloooo:'':lodolc,'' '........       ...  ....                       .....
                                    ..,;;::ccclllloc,',colclol;.............      ....  ....             .....          
                                    ..,;;:::ccccll;....,;:'',,'............     .........''.           ......           
                                     .',;;:::cclc'. ....,,.......     .....    .....   ..,'.           .. . ..          
                                     .',;;;::cc;.  ......'.....   .     ....   .....  ..',,.              . ..          
                                     ..,;;::c:'.....,,.,co:...         ..',.........  .',,,.                            
                                      .,;:c:,. ....':c;lxx:.          ...',;'......  ..,,;;.                            
                                      .';:;.. ....',:c;lkx,.         ....',,;,.....  .',;;;.                            
                                      ..,.......'' ':::dOx;.         ....,;;,,, .. .. ,,,,;.                            
                                       ....'' '',,..;clxxo,.         ...',;;,'......',,,,,;.                            
                                        ..'' '',;'..,looc:'.         ...';:,,'......'',;;;;.                            
''')
        
