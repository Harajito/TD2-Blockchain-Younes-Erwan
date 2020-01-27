


def convertir_base_vers_dec(mot,base):
    nombre,compteur = 0,0
    for i in mot:
        nombre += "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/".index(i)*base**(len(mot)-compteur-1)
        compteur += 1
    return nombre

def convertir_dec_vers_base(nbr,base):
    liste = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/")
    if not nbr:
        return "0"
    else:
        mot = ""
        compteur = 0
        while nbr>=base**compteur:
            compteur += 1
        compteur -=1
        for i in range(compteur,-1,-1):
            val = nbr//(base**i)
            nbr -= val*base**i
            mot += liste[val]
        return mot

liste_bip_39 = ["abandon","ability","able","about","above","absent","absorb","abstract","absurd","abuse","access","accident","account","accuse","achieve","acid","acoustic","acquire","across","act","action","actor","actress","actual","adapt","add","addict","address","adjust","admit","adult","advance","advice","aerobic","affair","afford","afraid","again","age","agent","agree","ahead","aim","air","airport","aisle","alarm","album","alcohol","alert","alien","all","alley","allow","almost","alone","alpha","already","also","alter","always","amateur","amazing","among","amount","amused","analyst","anchor","ancient","anger","angle","angry","animal","ankle","announce","annual","another","answer","antenna","antique","anxiety","any","apart","apology","appear","apple","approve","april","arch","arctic","area","arena","argue","arm","armed","armor","army","around","arrange","arrest","arrive","arrow","art","artefact","artist","artwork","ask","aspect","assault","asset","assist","assume","asthma","athlete","atom","attack","attend","attitude","attract","auction","audit","august","aunt","author","auto","autumn","average","avocado","avoid","awake","aware","away","awesome","awful","awkward","axis","baby","bachelor","bacon","badge","bag","balance","balcony","ball","bamboo","banana","banner","bar","barely","bargain","barrel","base","basic","basket","battle","beach","bean","beauty","because","become","beef","before","begin","behave","behind","believe","below","belt","bench","benefit","best","betray","better","between","beyond","bicycle","bid","bike","bind","biology","bird","birth","bitter","black","blade","blame","blanket","blast","bleak","bless","blind","blood","blossom","blouse","blue","blur","blush","board","boat","body","boil","bomb","bone","bonus","book","boost","border","boring","borrow","boss","bottom","bounce","box","boy","bracket","brain","brand","brass","brave","bread","breeze","brick","bridge","brief","bright","bring","brisk","broccoli","broken","bronze","broom","brother","brown","brush","bubble","buddy","budget","buffalo","build","bulb","bulk","bullet","bundle","bunker","burden","burger","burst","bus","business","busy","butter","buyer","buzz","cabbage","cabin","cable","cactus","cage","cake","call","calm","camera","camp","can","canal","cancel","candy","cannon","canoe","canvas","canyon","capable","capital","captain","car","carbon","card","cargo","carpet","carry","cart","case","cash","casino","castle","casual","cat","catalog","catch","category","cattle","caught","cause","caution","cave","ceiling","celery","cement","census","century","cereal","certain","chair","chalk","champion","change","chaos","chapter","charge","chase","chat","cheap","check","cheese","chef","cherry","chest","chicken","chief","child","chimney","choice","choose","chronic","chuckle","chunk","churn","cigar","cinnamon","circle","citizen","city","civil","claim","clap","clarify","claw","clay","clean","clerk","clever","click","client","cliff","climb","clinic","clip","clock","clog","close","cloth","cloud","clown","club","clump","cluster","clutch","coach","coast","coconut","code","coffee","coil","coin","collect","color","column","combine","come","comfort","comic","common","company","concert","conduct","confirm","congress","connect","consider","control","convince","cook","cool","copper","copy","coral","core","corn","correct","cost","cotton","couch","country","couple","course","cousin","cover","coyote","crack","cradle","craft","cram","crane","crash","crater","crawl","crazy","cream","credit","creek","crew","cricket","crime","crisp","critic","crop","cross","crouch","crowd","crucial","cruel","cruise","crumble","crunch","crush","cry","crystal","cube","culture","cup","cupboard","curious","current","curtain","curve","cushion","custom","cute","cycle","dad","damage","damp","dance","danger","daring","dash","daughter","dawn","day","deal","debate","debris","decade","december","decide","decline","decorate","decrease","deer","defense","define","defy","degree","delay","deliver","demand","demise","denial","dentist","deny","depart","depend","deposit","depth","deputy","derive","describe","desert","design","desk","despair","destroy","detail","detect","develop","device","devote","diagram","dial","diamond","diary","dice","diesel","diet","differ","digital","dignity","dilemma","dinner","dinosaur","direct","dirt","disagree","discover","disease","dish","dismiss","disorder","display","distance","divert","divide","divorce","dizzy","doctor","document","dog","doll","dolphin","domain","donate","donkey","donor","door","dose","double","dove","draft","dragon","drama","drastic","draw","dream","dress","drift","drill","drink","drip","drive","drop","drum","dry","duck","dumb","dune","during","dust","dutch","duty","dwarf","dynamic","eager","eagle","early","earn","earth","easily","east","easy","echo","ecology","economy","edge","edit","educate","effort","egg","eight","either","elbow","elder","electric","elegant","element","elephant","elevator","elite","else","embark","embody","embrace","emerge","emotion","employ","empower","empty","enable","enact","end","endless","endorse","enemy","energy","enforce","engage","engine","enhance","enjoy","enlist","enough","enrich","enroll","ensure","enter","entire","entry","envelope","episode","equal","equip","era","erase","erode","erosion","error","erupt","escape","essay","essence","estate","eternal","ethics","evidence","evil","evoke","evolve","exact","example","excess","exchange","excite","exclude","excuse","execute","exercise","exhaust","exhibit","exile","exist","exit","exotic","expand","expect","expire","explain","expose","express","extend","extra","eye","eyebrow","fabric","face","faculty","fade","faint","faith","fall","false","fame","family","famous","fan","fancy","fantasy","farm","fashion","fat","fatal","father","fatigue","fault","favorite","feature","february","federal","fee","feed","feel","female","fence","festival","fetch","fever","few","fiber","fiction","field","figure","file","film","filter","final","find","fine","finger","finish","fire","firm","first","fiscal","fish","fit","fitness","fix","flag","flame","flash","flat","flavor","flee","flight","flip","float","flock","floor","flower","fluid","flush","fly","foam","focus","fog","foil","fold","follow","food","foot","force","forest","forget","fork","fortune","forum","forward","fossil","foster","found","fox","fragile","frame","frequent","fresh","friend","fringe","frog","front","frost","frown","frozen","fruit","fuel","fun","funny","furnace","fury","future","gadget","gain","galaxy","gallery","game","gap","garage","garbage","garden","garlic","garment","gas","gasp","gate","gather","gauge","gaze","general","genius","genre","gentle","genuine","gesture","ghost","giant","gift","giggle","ginger","giraffe","girl","give","glad","glance","glare","glass","glide","glimpse","globe","gloom","glory","glove","glow","glue","goat","goddess","gold","good","goose","gorilla","gospel","gossip","govern","gown","grab","grace","grain","grant","grape","grass","gravity","great","green","grid","grief","grit","grocery","group","grow","grunt","guard","guess","guide","guilt","guitar","gun","gym","habit","hair","half","hammer","hamster","hand","happy","harbor","hard","harsh","harvest","hat","have","hawk","hazard","head","health","heart","heavy","hedgehog","height","hello","helmet","help","hen","hero","hidden","high","hill","hint","hip","hire","history","hobby","hockey","hold","hole","holiday","hollow","home","honey","hood","hope","horn","horror","horse","hospital","host","hotel","hour","hover","hub","huge","human","humble","humor","hundred","hungry","hunt","hurdle","hurry","hurt","husband","hybrid","ice","icon","idea","identify","idle","ignore","ill","illegal","illness","image","imitate","immense","immune","impact","impose","improve","impulse","inch","include","income","increase","index","indicate","indoor","industry","infant","inflict","inform","inhale","inherit","initial","inject","injury","inmate","inner","innocent","input","inquiry","insane","insect","inside","inspire","install","intact","interest","into","invest","invite","involve","iron","island","isolate","issue","item","ivory","jacket","jaguar","jar","jazz","jealous","jeans","jelly","jewel","job","join","joke","journey","joy","judge","juice","jump","jungle","junior","junk","just","kangaroo","keen","keep","ketchup","key","kick","kid","kidney","kind","kingdom","kiss","kit","kitchen","kite","kitten","kiwi","knee","knife","knock","know","lab","label","labor","ladder","lady","lake","lamp","language","laptop","large","later","latin","laugh","laundry","lava","law","lawn","lawsuit","layer","lazy","leader","leaf","learn","leave","lecture","left","leg","legal","legend","leisure","lemon","lend","length","lens","leopard","lesson","letter","level","liar","liberty","library","license","life","lift","light","like","limb","limit","link","lion","liquid","list","little","live","lizard","load","loan","lobster","local","lock","logic","lonely","long","loop","lottery","loud","lounge","love","loyal","lucky","luggage","lumber","lunar","lunch","luxury","lyrics","machine","mad","magic","magnet","maid","mail","main","major","make","mammal","man","manage","mandate","mango","mansion","manual","maple","marble","march","margin","marine","market","marriage","mask","mass","master","match","material","math","matrix","matter","maximum","maze","meadow","mean","measure","meat","mechanic","medal","media","melody","melt","member","memory","mention","menu","mercy","merge","merit","merry","mesh","message","metal","method","middle","midnight","milk","million","mimic","mind","minimum","minor","minute","miracle","mirror","misery","miss","mistake","mix","mixed","mixture","mobile","model","modify","mom","moment","monitor","monkey","monster","month","moon","moral","more","morning","mosquito","mother","motion","motor","mountain","mouse","move","movie","much","muffin","mule","multiply","muscle","museum","mushroom","music","must","mutual","myself","mystery","myth","naive","name","napkin","narrow","nasty","nation","nature","near","neck","need","negative","neglect","neither","nephew","nerve","nest","net","network","neutral","never","news","next","nice","night","noble","noise","nominee","noodle","normal","north","nose","notable","note","nothing","notice","novel","now","nuclear","number","nurse","nut","oak","obey","object","oblige","obscure","observe","obtain","obvious","occur","ocean","october","odor","off","offer","office","often","oil","okay","old","olive","olympic","omit","once","one","onion","online","only","open","opera","opinion","oppose","option","orange","orbit","orchard","order","ordinary","organ","orient","original","orphan","ostrich","other","outdoor","outer","output","outside","oval","oven","over","own","owner","oxygen","oyster","ozone","pact","paddle","page","pair","palace","palm","panda","panel","panic","panther","paper","parade","parent","park","parrot","party","pass","patch","path","patient","patrol","pattern","pause","pave","payment","peace","peanut","pear","peasant","pelican","pen","penalty","pencil","people","pepper","perfect","permit","person","pet","phone","photo","phrase","physical","piano","picnic","picture","piece","pig","pigeon","pill","pilot","pink","pioneer","pipe","pistol","pitch","pizza","place","planet","plastic","plate","play","please","pledge","pluck","plug","plunge","poem","poet","point","polar","pole","police","pond","pony","pool","popular","portion","position","possible","post","potato","pottery","poverty","powder","power","practice","praise","predict","prefer","prepare","present","pretty","prevent","price","pride","primary","print","priority","prison","private","prize","problem","process","produce","profit","program","project","promote","proof","property","prosper","protect","proud","provide","public","pudding","pull","pulp","pulse","pumpkin","punch","pupil","puppy","purchase","purity","purpose","purse","push","put","puzzle","pyramid","quality","quantum","quarter","question","quick","quit","quiz","quote","rabbit","raccoon","race","rack","radar","radio","rail","rain","raise","rally","ramp","ranch","random","range","rapid","rare","rate","rather","raven","raw","razor","ready","real","reason","rebel","rebuild","recall","receive","recipe","record","recycle","reduce","reflect","reform","refuse","region","regret","regular","reject","relax","release","relief","rely","remain","remember","remind","remove","render","renew","rent","reopen","repair","repeat","replace","report","require","rescue","resemble","resist","resource","response","result","retire","retreat","return","reunion","reveal","review","reward","rhythm","rib","ribbon","rice","rich","ride","ridge","rifle","right","rigid","ring","riot","ripple","risk","ritual","rival","river","road","roast","robot","robust","rocket","romance","roof","rookie","room","rose","rotate","rough","round","route","royal","rubber","rude","rug","rule","run","runway","rural","sad","saddle","sadness","safe","sail","salad","salmon","salon","salt","salute","same","sample","sand","satisfy","satoshi","sauce","sausage","save","say","scale","scan","scare","scatter","scene","scheme","school","science","scissors","scorpion","scout","scrap","screen","script","scrub","sea","search","season","seat","second","secret","section","security","seed","seek","segment","select","sell","seminar","senior","sense","sentence","series","service","session","settle","setup","seven","shadow","shaft","shallow","share","shed","shell","sheriff","shield","shift","shine","ship","shiver","shock","shoe","shoot","shop","short","shoulder","shove","shrimp","shrug","shuffle","shy","sibling","sick","side","siege","sight","sign","silent","silk","silly","silver","similar","simple","since","sing","siren","sister","situate","six","size","skate","sketch","ski","skill","skin","skirt","skull","slab","slam","sleep","slender","slice","slide","slight","slim","slogan","slot","slow","slush","small","smart","smile","smoke","smooth","snack","snake","snap","sniff","snow","soap","soccer","social","sock","soda","soft","solar","soldier","solid","solution","solve","someone","song","soon","sorry","sort","soul","sound","soup","source","south","space","spare","spatial","spawn","speak","special","speed","spell","spend","sphere","spice","spider","spike","spin","spirit","split","spoil","sponsor","spoon","sport","spot","spray","spread","spring","spy","square","squeeze","squirrel","stable","stadium","staff","stage","stairs","stamp","stand","start","state","stay","steak","steel","stem","step","stereo","stick","still","sting","stock","stomach","stone","stool","story","stove","strategy","street","strike","strong","struggle","student","stuff","stumble","style","subject","submit","subway","success","such","sudden","suffer","sugar","suggest","suit","summer","sun","sunny","sunset","super","supply","supreme","sure","surface","surge","surprise","surround","survey","suspect","sustain","swallow","swamp","swap","swarm","swear","sweet","swift","swim","swing","switch","sword","symbol","symptom","syrup","system","table","tackle","tag","tail","talent","talk","tank","tape","target","task","taste","tattoo","taxi","teach","team","tell","ten","tenant","tennis","tent","term","test","text","thank","that","theme","then","theory","there","they","thing","this","thought","three","thrive","throw","thumb","thunder","ticket","tide","tiger","tilt","timber","time","tiny","tip","tired","tissue","title","toast","tobacco","today","toddler","toe","together","toilet","token","tomato","tomorrow","tone","tongue","tonight","tool","tooth","top","topic","topple","torch","tornado","tortoise","toss","total","tourist","toward","tower","town","toy","track","trade","traffic","tragic","train","transfer","trap","trash","travel","tray","treat","tree","trend","trial","tribe","trick","trigger","trim","trip","trophy","trouble","truck","true","truly","trumpet","trust","truth","try","tube","tuition","tumble","tuna","tunnel","turkey","turn","turtle","twelve","twenty","twice","twin","twist","two","type","typical","ugly","umbrella","unable","unaware","uncle","uncover","under","undo","unfair","unfold","unhappy","uniform","unique","unit","universe","unknown","unlock","until","unusual","unveil","update","upgrade","uphold","upon","upper","upset","urban","urge","usage","use","used","useful","useless","usual","utility","vacant","vacuum","vague","valid","valley","valve","van","vanish","vapor","various","vast","vault","vehicle","velvet","vendor","venture","venue","verb","verify","version","very","vessel","veteran","viable","vibrant","vicious","victory","video","view","village","vintage","violin","virtual","virus","visa","visit","visual","vital","vivid","vocal","voice","void","volcano","volume","vote","voyage","wage","wagon","wait","walk","wall","walnut","want","warfare","warm","warrior","wash","wasp","waste","water","wave","way","wealth","weapon","wear","weasel","weather","web","wedding","weekend","weird","welcome","west","wet","whale","what","wheat","wheel","when","where","whip","whisper","wide","width","wife","wild","will","win","window","wine","wing","wink","winner","winter","wire","wisdom","wise","wish","witness","wolf","woman","wonder","wood","wool","word","work","world","worry","worth","wrap","wreck","wrestle","wrist","write","wrong","yard","year","yellow","you","young","youth","zebra","zero","zone","zoo"]


from tkinter import *
import hashlib
import secrets

def generer_128(*args):
    seed_dec = secrets.randbits(128)
    seed_bin = convertir_dec_vers_base(seed_dec,2)
    seed_bin = "0"*(128-len(seed_bin))+seed_bin
    blocs = [seed_bin[11*i:11*i+11] for i in range(len(seed_bin)//11)]
    blocs += [seed_bin[-7:]]
    text_label1.set(" ".join(blocs))

def generer_mnemonique(*args):
    global liste_bip_39
    m = hashlib.sha256()
    m.update(bytes(text_label1.get().replace(" ",""), encoding='utf8'))
    m.digest()
    valeur = m.hexdigest()
    valeur_bin = convertir_dec_vers_base(convertir_base_vers_dec(valeur,16),2)
    valeur_bin_moitie1 = valeur_bin[:128+1]
    valeur_bin_moitie2 = valeur_bin[128:]
    text_label2.set("Le hash obetnu par la fonction de hash256 pour ce nombre est : "+valeur_bin_moitie1)
    text_label3.set(valeur_bin_moitie2)
    text_label1.set(text_label1.get().replace(" ","-"))
    text_label4.set("Le mot binaire était : "+text_label1.get())
    text_label5.set("Il devient                   : "+text_label1.get()+valeur_bin[:4])
    text_label1.set(text_label1.get().replace("-"," "))
    seed_bin = text_label1.get().replace(" ","")+valeur_bin[:4]
    blocs = [seed_bin[11*i:11*i+11] for i in range(len(seed_bin)//11)]
    blocs_mots = [liste_bip_39[convertir_base_vers_dec(i,2)] for i in blocs]
    text_label6.set("La clé mnémonique est alors : "+"-".join(blocs_mots))

def verifier_integre(*args):
    global liste_bip_39
    labels = [text_label7,text_label8,text_label9,text_label10,text_label11,text_label12,text_label13,text_label14,text_label15,text_label16,text_label17,text_label18]
    for i in labels:
        if not len(i.get()):
            text_label19.set("Il faut entrer 12 mots.")
            return 
        if not liste_bip_39.count(i.get()):
            text_label19.set("Un des mots n'a pas été trouvé dans la liste bip39")
            return
    seed_recup = ["0"*(11-len(convertir_dec_vers_base(liste_bip_39.index(i.get(),2),2)))+convertir_dec_vers_base(liste_bip_39.index(i.get(),2),2) for i in labels]
    text_label19.set("Le mot binaire de 132 bit extrait est : "+" ".join(seed_recup))
    text_label20.set("Le mot binaire de 128 bit extrait est : "+" ".join(seed_recup)[:-4])
    m = hashlib.sha256()
    m.update(bytes("".join(seed_recup)[:-4], encoding='utf8'))
    m.digest()
    valeur_bin = convertir_dec_vers_base(convertir_base_vers_dec(m.hexdigest(),16),2)
    valeur_bin_moitie1 = valeur_bin[:128+1]
    valeur_bin_moitie2 = valeur_bin[128:]
    text_label20.set("Le hash obetnu par la fonction de hash256 pour ce nombre est : "+valeur_bin_moitie1)
    text_label21.set(valeur_bin_moitie2)
    if valeur_bin[:4] != "".join(seed_recup)[-4:]:
        text_label22.set("La clé n'est pas intègre, on a : "+valeur_bin[:4]+" != "+"".join(seed_recup)[-4:])
    else:
        text_label22.set("L'intégrité de la clé est bien vérifiée")
        "".join(seed_recup)
        m = hashlib.sha512()
        m.update(bytes("".join(seed_recup), encoding='utf8'))
        m.digest()
        valeur = m.hexdigest()
        valeur_bin = convertir_dec_vers_base(convertir_base_vers_dec(valeur,16),2)
        master_private_key = valeur_bin[:int(len(valeur_bin)/2)+1]
        master_chain_code = valeur_bin[int(len(valeur_bin)/2):]
        text_label23.set("Après avoir procédé au hash512, on obtient : ")
        master_private_key_moitie1 = master_private_key[:128+1]
        master_private_key_moitie2 = master_private_key[128:]
        master_chain_code_moitie1 = master_chain_code[:128+1]
        master_chain_code_moitie2 = master_chain_code[128:]
        text_label24.set("La master private key : "+master_private_key_moitie1)
        text_label25.set(master_private_key_moitie2)
        text_label26.set("Et le master chain code : "+master_chain_code_moitie1)
        text_label27.set(master_chain_code_moitie2)
            


fenetre = Tk()
fenetre.geometry("1500x950+100+25")


label1 = Label(fenetre,text="Nombre codé sur 128 bits : ")
label1.place(x=100,y=100)

text_label1 = StringVar()
stock = "0"*11+" "
text_label1.set(stock*11+"0"*7)
champs1 = Entry(fenetre,textvariable=text_label1,width=150)
champs1.place(x=100,y=120)

bouton = Button(fenetre,text="Générer un nouveau nombre aléatoire codé sur 128 bits",width=128,command=generer_128)
bouton.place(x=100,y=140)

bouton = Button(fenetre,text="Faire les calculs qui, à partir de ce nombre permettent de générer la clé mnémonique",width=128,command=generer_mnemonique)
bouton.place(x=100,y=180)

text_label2 = StringVar()
text_label2.set("")
label2 = Label(fenetre,textvariable = text_label2)
label2.place(x=100,y=220)

text_label3 = StringVar()
text_label3.set("")
label3 = Label(fenetre,textvariable = text_label3)
label3.place(x=439,y=240)

text_label4 = StringVar()
text_label4.set("")
label4 = Label(fenetre,textvariable = text_label4)
label4.place(x=100,y=260)

text_label5 = StringVar()
text_label5.set("")
label5 = Label(fenetre,textvariable = text_label5)
label5.place(x=100,y=280)

text_label6 = StringVar()
text_label6.set("")
label6 = Label(fenetre,textvariable = text_label6)
label6.place(x=100,y=300)




text_label7 = StringVar()
text_label7.set("gate")
champs2 = Entry(fenetre,textvariable=text_label7,width=15)
champs2.place(x=100,y=350)

text_label8 = StringVar()
text_label8.set("ill")
champs3 = Entry(fenetre,textvariable=text_label8,width=15)
champs3.place(x=200,y=350)

text_label9 = StringVar()
text_label9.set("apology")
champs4 = Entry(fenetre,textvariable=text_label9,width=15)
champs4.place(x=300,y=350)

text_label10 = StringVar()
text_label10.set("ring")
champs5 = Entry(fenetre,textvariable=text_label10,width=15)
champs5.place(x=400,y=350)

text_label11 = StringVar()
text_label11.set("chase")
champs6 = Entry(fenetre,textvariable=text_label11,width=15)
champs6.place(x=500,y=350)

text_label12 = StringVar()
text_label12.set("speak")
champs7 = Entry(fenetre,textvariable=text_label12,width=15)
champs7.place(x=600,y=350)

text_label13 = StringVar()
text_label13.set("august")
champs8 = Entry(fenetre,textvariable=text_label13,width=15)
champs8.place(x=700,y=350)

text_label14 = StringVar()
text_label14.set("true")
champs9 = Entry(fenetre,textvariable=text_label14,width=15)
champs9.place(x=800,y=350)

text_label15 = StringVar()
text_label15.set("toy")
champs10 = Entry(fenetre,textvariable=text_label15,width=15)
champs10.place(x=900,y=350)

text_label16 = StringVar()
text_label16.set("helmet")
champs11 = Entry(fenetre,textvariable=text_label16,width=15)
champs11.place(x=1000,y=350)

text_label17 = StringVar()
text_label17.set("example")
champs12 = Entry(fenetre,textvariable=text_label17,width=15)
champs12.place(x=1100,y=350)

text_label18 = StringVar()
text_label18.set("daring")
champs13 = Entry(fenetre,textvariable=text_label18,width=15)
champs13.place(x=1200,y=350)




bouton = Button(fenetre,text="Si la clé est bien intègre, on extrait la master private key, le chain code, la master public key et on génère une clé enfant.",width=100,command=verifier_integre)
bouton.place(x=100,y=380)

text_label19 = StringVar()
text_label19.set("")
label7 = Label(fenetre,textvariable = text_label19)
label7.place(x=100,y=420)

text_label20 = StringVar()
text_label20.set("")
label8 = Label(fenetre,textvariable = text_label20)
label8.place(x=100,y=440)

text_label21 = StringVar()
text_label21.set("")
label9 = Label(fenetre,textvariable = text_label21)
label9.place(x=439,y=460)

text_label22 = StringVar()
text_label22.set("")
label10 = Label(fenetre,textvariable = text_label22)
label10.place(x=100,y=480)

text_label23 = StringVar()
text_label23.set("")
label11 = Label(fenetre,textvariable = text_label23)
label11.place(x=100,y=500)

text_label24 = StringVar()
text_label24.set("")
label12 = Label(fenetre,textvariable = text_label24)
label12.place(x=100,y=520)

text_label25 = StringVar()
text_label25.set("")
label13 = Label(fenetre,textvariable = text_label25)
label13.place(x=222,y=540)

text_label26 = StringVar()
text_label26.set("")
label14 = Label(fenetre,textvariable = text_label26)
label14.place(x=100,y=560)

text_label27 = StringVar()
text_label27.set("")
label15 = Label(fenetre,textvariable = text_label27)
label15.place(x=232,y=580)








fenetre.mainloop()




































