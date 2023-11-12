import os
from tkinter import *  
from random import randint
import time
from tkinter import ttk
from PIL import Image, ImageTk
#----------------------------variable 
tableau_id_map=[]
tableau_id_dame=[]
tableau_id_deplacement=[]
memo_tab=[]
flag_joueur=0
flag_click=0
direction_pion=0
ligne_centre=0
colonne_centre=0
flag_ia_joue=0
#----------variable IA
score=0
memo_ligne=[]
memo_collone=[]
memo_ligne_m=[]
memo_collone_m=[]
profondeur=1
profondeur_n=1

l=0
c=0
l_m=0
c_m=0
partiel_score=0
flag=True
i=0
tab_image=[]
#-----variable couleur pion
couleur_pion_joueur2='red'
couleur_pion_joueur1='yellow'
#----------fonction pour ia 
def valeur_radio():
    global flag_ia_joue
    flag_ia_joue=v.get()

def coup_ordi():
    #parcour tout 
    global flag_joueur,tableau_id_dame,i
    global memo_ligne,memo_collone,memo_ligne_m,memo_collone_m,score
    memo_ligne=[]
    memo_collone=[]
    memo_ligne_m=[]
    memo_collone_m=[]

    for ligne in range(10):
        for colonne in range(10):
            selection_ia(ligne,colonne)
            print(memo_collone_m,memo_collone,memo_ligne_m,memo_ligne)
            
            
            i=i+1
    jouer_ia()
    score=0
    flag_joueur=flag_joueur+2  
def selection_ia(ligne,colonne):
    global ligne_centre,colonne_centre,c,l,c_m,l_m,flag,i
    ligne_centre=ligne
    colonne_centre=colonne
    
    #selectionnne pert rouge 
    if  0<tableau_id_dame[int(ligne)][int(colonne)][0] <=120 and flag==True:
        direction_pion=1
        if profondeur==1:
            l=ligne
            c=colonne
        tab=case_possible_ia(1,direction_pion)
      
        for e in tab:
            
            ligned=(e-1)/10
            colonned=(e-1)%10
            if profondeur==1:
                l_m=ligned
                c_m=colonned
            deplacement_ia(int(ligned),int(colonned),ligne,colonne)
    if  tableau_id_dame[int(ligne)][int(colonne)][0] >120 and flag==False:
        
        direction_pion=-1
        tab=case_possible_ia(1,direction_pion)
        for e in tab:
            ligned=(e-1)/10
            colonned=(e-1)%10
            deplacement_ia(int(ligned),int(colonned),ligne,colonne)
def case_possible_ia(n_case,sens):
    global ligne_centre,colonne_centre,flag_click,flag_joueur
    tableau_id_deplacement=[]
    if n_case==1:
        #elif egale saut
     
        if 9>=colonne_centre+sens>=0:     
           
            if tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre+sens)][0]==0:
                if flag_ia_joue==0 or flag_joueur<2:
                    Canva.itemconfigure(tableau_id_map[int(ligne_centre+sens)][int(colonne_centre+sens)], fill="blue") 
                tableau_id_deplacement.append(int(tableau_id_map[int(ligne_centre+sens)][int(colonne_centre+sens)]))
            elif tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre+sens)][0]>120 and sens==1 or tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre+sens)][0]<=120 and sens==-1:
               
                if 0< colonne_centre+sens<9 and 0< ligne_centre+sens<9:
                    
                    if tableau_id_dame[int(ligne_centre+(2*sens))][int(colonne_centre+(2*sens))][0]==0:
                        if flag_ia_joue==0 or flag_joueur<2:
                            Canva.itemconfigure(tableau_id_map[int(ligne_centre+(2*sens))][int(colonne_centre+(2*sens))], fill="blue") 
                        tableau_id_deplacement.append(int(tableau_id_map[int(ligne_centre+(2*sens))][int(colonne_centre+(2*sens))]))
            
        if 0<=colonne_centre-sens<=9 : 
           
            if tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre-sens)][0]==0:
                tableau_id_deplacement.append(int(tableau_id_map[int(ligne_centre+sens)][int(colonne_centre-sens)]))
                if flag_ia_joue==0 or flag_joueur<2:
                    Canva.itemconfigure(tableau_id_map[int(ligne_centre+sens)][int(colonne_centre-sens)], fill="blue")
            elif tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre-sens)][0]>120 and sens==1  or tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre-sens)][0]<=120 and sens==-1 :
                if 0<colonne_centre-sens<9 and 0< ligne_centre+sens<9:
                    if tableau_id_dame[int(ligne_centre+(2*sens))][int(colonne_centre-(2*sens))][0]==0:
                        if flag_ia_joue==0 or flag_joueur<2:
                            Canva.itemconfigure(tableau_id_map[int(ligne_centre+(2*sens))][int(colonne_centre-(2*sens))], fill="blue") 
                            
                        tableau_id_deplacement.append(int(tableau_id_map[int(ligne_centre+(2*sens))][int(colonne_centre-(2*sens))]))
                 
    else:
        case_possible_dame()
    flag_click=1  
    return tableau_id_deplacement
def deplacement_ia(ligne_move,col_mov,ligne,colonne):
    global c,l,c_m,l_m,partiel_score
    col_result=col_mov-colonne
    lig_result=ligne_move-ligne
    cpt=tableau_id_dame[int(ligne)][int(colonne)][0]
    tableau_id_dame[int(ligne)][int(colonne)][0]=0
    
    d= tableau_id_dame[int(ligne)][int(colonne)][1]
    tableau_id_dame[int(ligne)][int(colonne)][1]=0
    
    tableau_id_dame[int(ligne_move)][int(col_mov)][0]=cpt  
    if (ligne_move==0 or ligne_move==9) or d=='d':
        tableau_id_dame[int(ligne_move)][int(col_mov)][1]='d'
    else:
        tableau_id_dame[int(ligne)][int(col_mov)][1]='p'
        
    if abs(col_result)==2:
        
        memo_e=tableau_id_dame[int(ligne+(lig_result/2))][int(colonne+(col_result/2))][0]
        memo_e2=tableau_id_dame[int(ligne+(lig_result/2))][int(colonne+(col_result/2))][1]
        tableau_id_dame[int(ligne+(lig_result/2))][int(colonne+(col_result/2))][0]=0
        tableau_id_dame[int(ligne+(lig_result/2))][int(colonne+(col_result/2))][1]=0
  
   #-----------------------
    print("toto")
    time.sleep(0.1)
    m=minmax()
    
    if profondeur<profondeur_n:
        m=partiel_score
    
    partiel_score=m
    meilleur(m,l,l_m,c,c_m)
    #----------------------------
 
    tableau_id_dame[int(ligne)][int(colonne)][0]=cpt
    tableau_id_dame[int(ligne)][int(colonne)][1]=d
    
    tableau_id_dame[int(ligne_move)][int(col_mov)][0]=0
    tableau_id_dame[int(ligne_move)][int(col_mov)][1]=0
    if abs(col_result)==2:

        tableau_id_dame[int(ligne+(lig_result/2))][int(colonne+(col_result/2))][0]=memo_e
        tableau_id_dame[int(ligne+(lig_result/2))][int(colonne+(col_result/2))][1]=memo_e2       
def minmax():
    global profondeur,flag
    pion_rouge=0
    pion_jaune=0
    for id2 in  tableau_id_dame:
        for id in id2: 
            
            if int(id[0])>120:
                pion_jaune=pion_jaune+1
            if 0<int(id[0])<=120:
                pion_rouge=pion_rouge+1
    dif=pion_jaune-pion_rouge
    if profondeur==profondeur_n:
       
        if dif >0:
                return -100
        elif dif ==0:
                return 0
        else:
                return dif*-100
    else:
        profondeur=profondeur+1
        
    if flag:
        flag=False
        
        for ligne in range(9):
            
            for colonne in range(9):
                selection_ia(ligne,colonne)
   
        
        flag=True
        if profondeur==profondeur_n-1:
            profondeur=1
    elif flag==False:
        flag=True
        for ligne in range(9):
       
            for colonne in range(9):
                
                selection_ia(ligne,colonne)
        
      
        
        flag=False
        if profondeur==profondeur_n:
            profondeur=2   
def meilleur(m,a1,a2,b1,b2):
    global score,memo_ligne,memo_collone,memo_ligne_m,memo_collone_m
    
    if score<m:
        
        memo_ligne=[]
        memo_ligne.append(a1)
        
        score=m
        
        memo_collone=[]
        memo_collone.append(b1)
        
        memo_collone_m=[]
        memo_collone_m.append(b2)
        
        memo_ligne_m=[]
        memo_ligne_m.append(a2)
    elif score==m:
       
        memo_ligne.append(a1)
        memo_collone.append(b1)
        memo_collone_m.append(b2)
        memo_ligne_m.append(a2)        
def jouer_ia():
    
    i=randint(0,len(memo_collone_m)-1 )
    col_result=int(memo_collone_m[i]-memo_collone[i])
   
    lig_result=int(memo_ligne_m[i]-memo_ligne[i])

    Canva.move(tableau_id_dame[int(memo_ligne[i])][int(memo_collone[i])][0],col_result*50,lig_result*50)
    Canva.tag_raise(tableau_id_dame[int(memo_ligne[i])][int(memo_collone[i])][0])
    
    cpt=tableau_id_dame[int(memo_ligne[i])][int(memo_collone[i])][0]
    tableau_id_dame[int(memo_ligne[i])][int(memo_collone[i])][0]=0
    
    d= tableau_id_dame[int(memo_ligne[i])][int(memo_collone[i])][1]
    tableau_id_dame[int(memo_ligne[i])][int(memo_collone[i])][1]=0
    
    tableau_id_dame[int(memo_ligne_m[i])][int(memo_collone_m[i])][0]=cpt  
    if (memo_ligne_m[i]==0 or memo_ligne_m[i]==9) or d=='d':
        tableau_id_dame[int(memo_ligne_m[i])][int(memo_collone_m[i])][1]='d'
    else:
        tableau_id_dame[int(memo_ligne_m[i])][int(memo_collone_m[i])][1]='p' 
    
    if abs(col_result)==2:
            Canva.delete(tableau_id_dame[int(memo_ligne[i]+(lig_result/2))][int(memo_collone[i]+(col_result/2))][0])
          
            tableau_id_dame[int(memo_ligne[i]+(lig_result/2))][int(memo_collone[i]+(col_result/2))][0]=0
            tableau_id_dame[int(memo_ligne[i]+(lig_result/2))][int(memo_collone[i]+(col_result/2))][1]=0

#-------------------------fonction
def bd_dame(ligne,colonne):
    global tableau_id_dame
    global tableau_id_deplacement,tableau_id_map
    if ligne!=9 and colonne!=0:
        if tableau_id_dame[int(ligne+1)][int(colonne-1)][0]==0:
            Canva.itemconfigure(tableau_id_map[int(ligne+1)][int(colonne-1)], fill="green")
            tableau_id_deplacement.append(tableau_id_map[int(ligne+1)][int(colonne-1)])
def hg_dame(ligne,colonne):
    global tableau_id_dame
    global tableau_id_deplacement,tableau_id_map
    if ligne!=0 and colonne!=9:
        if tableau_id_dame[int(ligne-1)][int(colonne+1)][0]==0:
            Canva.itemconfigure(tableau_id_map[int(ligne-1)][int(colonne+1)], fill="red")
            tableau_id_deplacement.append(tableau_id_map[int(ligne-1)][int(colonne+1)])
def hd_dame(ligne,colonne):
    global tableau_id_dame
    global tableau_id_deplacement,tableau_id_map
    if ligne!=0 and colonne!=0:
        if tableau_id_dame[int(ligne-1)][int(colonne-1)][0]==0:
            Canva.itemconfigure(tableau_id_map[int(ligne-1)][int(colonne-1)], fill="blue")
            tableau_id_deplacement.append(tableau_id_map[int(ligne-1)][int(colonne-1)])                          
def bg_dame(ligne,colonne):
    global tableau_id_deplacement,tableau_id_map
    global tableau_id_dame
    
    if ligne!=9 and colonne!=9:
        
        if tableau_id_dame[int(ligne+1)][int(colonne+1)][0]==0:
            Canva.itemconfigure(tableau_id_map[int(ligne+1)][int(colonne+1)], fill="yellow")
            tableau_id_deplacement.append(tableau_id_map[int(ligne+1)][int(colonne+1)])
def qui_gagne():
    pion_rouge=0
    pion_jaune=0
    for id2 in  tableau_id_dame:
        for id in id2: 
            
            if 0<int(id[0])<=120:
                pion_jaune=pion_jaune+1
            if int(id[0])>=120:
                pion_rouge=pion_rouge+1
    if pion_jaune==0:
        
        top = Toplevel()
        var = StringVar()
        label = Label(top, textvariable=var, relief=RAISED)
        var.set("les jaune on gagné ")
        top.mainloop()
    elif pion_rouge==0:
         
        top = Toplevel()
        var = StringVar()
        label = Label(top, textvariable=var, relief=RAISED)
        var.set("les rouge on gagné ")
        top.mainloop()             
def cre_tableau():
    #creation d'un tableau pour le damier
    global tab_image
    tableau_id_map=[]
    for i in range(10):
        tab1=[]
        for j in range(11):
            tab1.append(0)
        tableau_id_map.append(tab1)
        tab_image.append(tab1)
def curseur_souris(evt):
    pos_x, pos_y = Canva.canvasx(evt.x), Canva.canvasy(evt.y)
    colonne, ligne = pos_x // 50, pos_y // 50  
    return colonne,ligne
def case_possible_dame():
    global ligne_centre,colonne_centre,flag_click
    cpt_px=ligne_centre
    cpt_mx=ligne_centre
    cpt_py=colonne_centre
    cpt_my=colonne_centre
    flag_pg=0
    flag_mg=0
    flag_md=0
    flag_pd=0
    
    for i in range(10):
        #dernier colone
        if cpt_px <= 9 and i>0:
            if cpt_py<=9:
                if tableau_id_dame[int(cpt_px)][int(cpt_py)][0]==0 and flag_pg==0:
                    Canva.itemconfigure(tableau_id_map[int(cpt_px)][int(cpt_py)], fill="blue")
                    tableau_id_deplacement.append(tableau_id_map[int(cpt_px)][int(cpt_py)])
                elif flag_pg==0: 
                    if tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]>=120 and tableau_id_dame[int(cpt_px)][int(cpt_py)][0]<=120:
                        bg_dame(cpt_px,cpt_py)
                    elif tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]<=120 and tableau_id_dame[int(cpt_px)][int(cpt_py)][0]>=120:
                       bg_dame(cpt_px,cpt_py)
                    flag_pg=flag_pg+1
            if cpt_my>=0:
                if tableau_id_dame[int(cpt_px)][int(cpt_my)][0]==0 and flag_mg==0:
                    tableau_id_deplacement.append(tableau_id_map[int(cpt_px)][int(cpt_my)])
                    Canva.itemconfigure(tableau_id_map[int(cpt_px)][int(cpt_my)], fill="blue")
                elif flag_mg==0: 
                    if tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]>=120 and tableau_id_dame[int(cpt_px)][int(cpt_my)][0]<=120:
                        bd_dame(cpt_px,cpt_my)
                    elif tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]<=120 and tableau_id_dame[int(cpt_px)][int(cpt_my)][0]>=120:
                       bd_dame(cpt_px,cpt_my)
                    flag_mg=1
        #collonne de droite 
        if cpt_mx >= 0 and i>0:
            if cpt_py<=9:
                if tableau_id_dame[int(cpt_mx)][int(cpt_py)][0]==0 and flag_pd==0:
                    tableau_id_deplacement.append(tableau_id_map[int(cpt_mx)][int(cpt_py)])
                    Canva.itemconfigure(tableau_id_map[int(cpt_mx)][int(cpt_py)], fill="blue")
                elif flag_pd==0: 
                    if tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]>=120 and tableau_id_dame[int(cpt_mx)][int(cpt_py)][0]<=120:
                        hg_dame(cpt_mx,cpt_py)
                    elif tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]<=120 and tableau_id_dame[int(cpt_mx)][int(cpt_py)][0]>=120:
                       hg_dame(cpt_mx,cpt_py)
                    flag_pd=1
            if cpt_my>=0:
                if tableau_id_dame[int(cpt_mx)][int(cpt_my)][0]==0 and flag_md==0:
                    tableau_id_deplacement.append(tableau_id_map[int(cpt_mx)][int(cpt_my)])
                    Canva.itemconfigure(tableau_id_map[int(cpt_mx)][int(cpt_my)], fill="blue")
                elif flag_md==0:
                    if tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]>=120 and tableau_id_dame[int(cpt_mx)][int(cpt_my)][0]<=120:
                        hd_dame(cpt_mx,cpt_my)
                    elif tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]<=120 and tableau_id_dame[int(cpt_mx)][int(cpt_my)][0]>=120:
                       hd_dame(cpt_mx,cpt_my)
                    flag_md=1
                    
        cpt_py+=1
        cpt_my-=1
        cpt_px+=1
        cpt_mx-=1
def case_possible(n_case,sens):
    global ligne_centre,colonne_centre,flag_click,flag_joueur
    if n_case==1:
        #elif egale saut
     
        if 9>=colonne_centre+sens>=0:     
           
            if tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre+sens)][0]==0:
                if flag_ia_joue==0 or flag_joueur<2:
                    Canva.itemconfigure(tableau_id_map[int(ligne_centre+sens)][int(colonne_centre+sens)], fill="blue") 
                tableau_id_deplacement.append(int(tableau_id_map[int(ligne_centre+sens)][int(colonne_centre+sens)]))
            elif tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre+sens)][0]>120 and sens==1 or tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre+sens)][0]<=120 and sens==-1:
               
                if 0< colonne_centre+sens<9 and 0< ligne_centre+sens<9:
                    
                    if tableau_id_dame[int(ligne_centre+(2*sens))][int(colonne_centre+(2*sens))][0]==0:
                        if flag_ia_joue==0 or flag_joueur<2:
                            Canva.itemconfigure(tableau_id_map[int(ligne_centre+(2*sens))][int(colonne_centre+(2*sens))], fill="blue") 
                        tableau_id_deplacement.append(int(tableau_id_map[int(ligne_centre+(2*sens))][int(colonne_centre+(2*sens))]))
            
        if 0<=colonne_centre-sens<=9 : 
           
            if tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre-sens)][0]==0:
                tableau_id_deplacement.append(int(tableau_id_map[int(ligne_centre+sens)][int(colonne_centre-sens)]))
                if flag_ia_joue==0 or flag_joueur<2:
                    Canva.itemconfigure(tableau_id_map[int(ligne_centre+sens)][int(colonne_centre-sens)], fill="blue")
            elif tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre-sens)][0]>120 and sens==1  or tableau_id_dame[int(ligne_centre+sens)][int(colonne_centre-sens)][0]<=120 and sens==-1 :
                if 0<colonne_centre-sens<9 and 0< ligne_centre+sens<9:
                    if tableau_id_dame[int(ligne_centre+(2*sens))][int(colonne_centre-(2*sens))][0]==0:
                        if flag_ia_joue==0 or flag_joueur<2:
                            Canva.itemconfigure(tableau_id_map[int(ligne_centre+(2*sens))][int(colonne_centre-(2*sens))], fill="blue") 
                            
                        tableau_id_deplacement.append(int(tableau_id_map[int(ligne_centre+(2*sens))][int(colonne_centre-(2*sens))]))
                 
    else:
        case_possible_dame()
    flag_click=1
def selection(evt):
    global flag_joueur,ligne_centre,colonne_centre
    global direction_pion
    #trouve la case 
    colonne, ligne =curseur_souris(evt)
    ligne_centre=ligne
    colonne_centre=colonne
    #un pion?
    if tableau_id_dame[int(ligne)][int(colonne)][0] !=0:
        
        
        Canva.itemconfigure(tableau_id_map[int(ligne)][int(colonne)], fill="green")
        # savoir si c'est un pion du joueur1
        if tableau_id_dame[int(ligne)][int(colonne)][1]=='p' and tableau_id_dame[int(ligne)][int(colonne)][0]>120:
            direction_pion=-1
            
            case_possible(1,direction_pion)
        elif tableau_id_dame[int(ligne)][int(colonne)][1]=='p':
            direction_pion=1
            case_possible(1,direction_pion)
        else:
            
            case_possible(2,0)
def deplacement(evt):
    global tableau_id_deplacement
    global ligne_centre,colonne_centre,flag_joueur
    global flag_click
    colonne, ligne =curseur_souris(evt)
    
    for id in tableau_id_deplacement:
         
         if id == tableau_id_map[int(ligne)][int(colonne)]:
            for id2 in tableau_id_deplacement:
                Canva.itemconfigure(id2,fill="black")
            #ia
            col_result=colonne-colonne_centre
            lig_result=ligne-ligne_centre
            
            #deplacement
            if abs(col_result)==2:
                Canva.delete(tableau_id_dame[int(ligne_centre+(lig_result/2))][int(colonne_centre+(col_result/2))][0])
          
                tableau_id_dame[int(ligne_centre+(lig_result/2))][int(colonne_centre+(col_result/2))][0]=0
                tableau_id_dame[int(ligne_centre+(lig_result/2))][int(colonne_centre+(col_result/2))][1]=0
            if abs(col_result)>2:
                x=-col_result/abs(col_result)
                y=-lig_result/abs(lig_result)
                Canva.delete(tableau_id_dame[int(ligne+y)][int(colonne+x)][0])
                tableau_id_dame[int(ligne+y)][int(colonne+x)][0]=0
                tableau_id_dame[int(ligne+y)][int(colonne+x)][1]=0

            Canva.move(tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0],col_result*50,lig_result*50)
            Canva.tag_raise(tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0])
            flag_click=0
            tableau_id_deplacement=[]
            #affichage 
            Canva.itemconfigure(tableau_id_map[int(ligne_centre)][int(colonne_centre)], fill="black")
       
            # changer la case
            cpt=tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]
            tableau_id_dame[int(ligne_centre)][int(colonne_centre)][0]=0
            d= tableau_id_dame[int(ligne_centre)][int(colonne_centre)][1]
            tableau_id_dame[int(ligne_centre)][int(colonne_centre)][1]=0
            tableau_id_dame[int(ligne)][int(colonne)][0]=cpt  
            if (ligne==0 or ligne==9) or d=='d':
                tableau_id_dame[int(ligne)][int(colonne)][1]='d'
            else:
                tableau_id_dame[int(ligne)][int(colonne)][1]='p'
          
            
            return 0
    flag_joueur=flag_joueur-1 
             
def joueur1(evt):
    global flag_click,flag_joueur
    colonne, ligne =curseur_souris(evt)
    
    if flag_click==1:
       
        deplacement(evt)
    else:
        if tableau_id_dame[int(ligne)][int(colonne)][0]>120:
           
            selection(evt)
        else:
            
            flag_joueur=flag_joueur-1
def joueur2(evt):
    global flag_click,flag_joueur
    
    if flag_click==1:
        
        deplacement(evt)
    else:
        
        colonne, ligne =curseur_souris(evt)
        if tableau_id_dame[int(ligne)][int(colonne)][0]<=120:
            selection(evt)
        else:
            flag_joueur=flag_joueur-1
def jouer(evt):
    global flag_joueur,flag_ia_joue,flag_click
    
    if flag_joueur<2:
        flag_joueur=flag_joueur+1
       
        joueur1(evt)
    else:
        if flag_ia_joue==0:
            flag_joueur=flag_joueur+1
            joueur2(evt)
            if flag_joueur==4:
                flag_joueur=0
        else:
            coup_ordi()
        
        if flag_joueur==4:
            flag_click=0
            flag_joueur=0

    qui_gagne()
    
def create_map():
    #creation du damier et creation des tableau case et tableau id pion 
    changecolor=0
    for j in range(10):
        tab=[]
        tab_pion=[]
        for i in range(11):
            #couleur damier
            if changecolor==1:
                changecolor=0
                couleur = "#000000"
            else:
                changecolor=1
                couleur="#FFFFFF"
            if i<10: 
                id_case=Canva.create_rectangle(0+i*50,0+j*50,50+i*50,50+j*50,fill=couleur)
                tab.append(id_case)
 
                     
        tableau_id_map.append(tab)
   
    for j in range(10):

        tab_pion=[]
        for i in range(11):
            if changecolor==1:
                changecolor=0

            else:
                changecolor=1
            if changecolor==0:
                #dame
                if j<4 and i<10:
                    id_pion=Canva.create_oval(0+i*50,0+j*50,50+i*50,50+j*50, fill='red', outline='red')
                    tab_pion.append([id_pion,'p']) 
                elif j>5 and i<10:
                    id_pion=Canva.create_oval(0+i*50,0+j*50,50+i*50,50+j*50, fill='yellow', outline='red')
                    
                    tab_pion.append([id_pion,'p'])    
                else:
                    tab_pion.append([0,0])   
            else:
                    tab_pion.append([0,0])  
        tableau_id_dame.append(tab_pion)
    
def aide():
    win = Toplevel(root)
    var = StringVar()
    label = Label(win, textvariable=var, relief=RAISED)
    var.set("jeu de dames version TOM \n"
            "ma version des dames et un mélange de plusieur jeu de dame \n"
            "les regles sont les suivante\n"
            "- pas de multi prise pion et dame  \n"
           "-les pion se déplace d’un en diagonale et toujours en avant.\n"
           " -les pion peuvent manger en sautant un seul pion adverse\n"
           " -les dame se déplacent dans tout les sens et de n case.\n"
           " - le choix d’un pion ne ce fait qu’une fois, alors attention \n"
            
)
    label.pack()
##################
def action1(evt):
    select = listej1.get()
    for j in range(10):
        for i in range(10):
            if tableau_id_dame[int(j)][int(i)][0]>120:
                Canva.itemconfigure(tableau_id_dame[int(j)][int(i)][0],fill=select)
                
def action2(evt):
    select = listej2.get()
    for j in range(10):
        for i in range(10):
            if tableau_id_dame[int(j)][int(i)][0]<=120:
                
                Canva.itemconfigure(tableau_id_dame[int(j)][int(i)][0],fill=select)
def action3(evt):
    repertoire_actuel = os.getcwd()

# Affichez le répertoire actuel
    print("Répertoire actuel:", repertoire_actuel)
    select = liste.get()
    if select=="bois":
        im = Image.open('img/bois.jpg')
    if select =="herbe":
        im = Image.open('img/herbe.jpg')
    im = im.resize((50, 50), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(im, master=root)
    change=0
    
    for j in range(10):
        for i in range(11):
            if change==0 :
                if select=="normal":
                    Canva.delete(tab_image[j][i])
                if select=="bois":
                    id=Canva.create_image(i*50, j*50, image=logo, anchor='nw')
                    Canva.tag_raise(id)
                    tab_image[j][i]=id
                if select=="herbe":
                    id=Canva.create_image(i*50, j*50, image=logo, anchor='nw')
                    Canva.tag_raise(id)
                    tab_image[j][i]=id
                change=1
            else:
                change=0
          
    xd,yd=Canva.bbox(id)
def action4(evt):
    global profondeur_n
    select = listepro.get()
    profondeur_n=select
#--------------------------main
if __name__ == "__main__":

    root = Tk()
    Canva = Canvas(root,width=500,height=500)
    Canva.pack(side="left")

    Canva.bind("<Button-1>", jouer)
   
    btn_lancer_partie=Button(root, text="lancer une partie ", width=20, height=5, command=create_map)
    cre_tableau()
    ####################### bouton pour le mode de jeu 
    label1 = Label(root, text = "mode de jeu ")
    btn_aide=Button(root, text="aide ", width=20, height=5, command=aide)
    v     = IntVar ()
    case1 = Radiobutton (variable = v, value = 0,command=valeur_radio)
    case2 = Radiobutton (variable = v, value = 1,command=valeur_radio)
    case2.config (text = "IA")
    case1.config (text = "joueur2")
    ################################### personnalisé les pion 
    label2 = Label(root, text = "couleur de pion joueur1 ")
    listeProduits=["red","yellow","green","pink"]
    listej1 = ttk.Combobox(root, values=listeProduits)
    listej1.current(1)
    listej1.bind("<<ComboboxSelected>>", action1)
    
    label3 = Label(root, text = "couleur de pion joueur2 ")
    listej2 = ttk.Combobox(root, values=listeProduits)
    listej2.current(0)
    listej2.bind("<<ComboboxSelected>>", action2)
    
    label4 = Label(root, text = "couleur du damier ")
    listeProduits=["normal","bois","herbe"]
    liste = ttk.Combobox(root, values=listeProduits)
    liste.current(0)
    liste.bind("<<ComboboxSelected>>", action3)
    
    labelpro = Label(root, text = "couleur du damier ")
    listePro=["1","2","3"]
    listepro = ttk.Combobox(root, values=listePro)
    listepro.current(0)
    
    ##################""
    btn_lancer_partie.pack() 
    btn_aide.pack() 
    
    label4.pack() 
    liste.pack() 
    #affichage 
    label1.pack()
    case1.pack()
    case2.pack()
    label2.pack()
    listej1.pack()
    label3.pack()
    listej2.pack()
    label4.pack()
    liste.pack()
    labelpro.pack()
    listepro.pack()

    root.mainloop()