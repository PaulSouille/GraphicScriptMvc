from Tkinter import *
import os
import mysql.connector


def callback():
    print("callback ok")



def getUsableTableName(tableName):
    UsableTableName = tableName
    UsableTableName = UsableTableName.replace("'",'')
    UsableTableName = UsableTableName.replace("(",'')
    UsableTableName = UsableTableName.replace(")",'')
    UsableTableName = UsableTableName.replace(",",'')
    #UsableTableName = UsableTableName[1:]
    UsableTableName = UsableTableName[0].upper()+UsableTableName[1:]
    return UsableTableName


def getUsableTableNameWithoutLower(tableName):
    UsableTableName = tableName
    UsableTableName = UsableTableName.replace("'",'')
    UsableTableName = UsableTableName.replace("(",'')
    UsableTableName = UsableTableName.replace(")",'')
    UsableTableName = UsableTableName.replace(",",'')
    #UsableTableName = UsableTableName[1:]

    return UsableTableName


def getUsableTableNameMin(tableName):
    UsableTableName = tableName
    UsableTableName = UsableTableName.replace("'",'')
    UsableTableName = UsableTableName.replace("(",'')
    UsableTableName = UsableTableName.replace(")",'')
    UsableTableName = UsableTableName.replace(",",'')
    #UsableTableName = UsableTableName[1:]
    return UsableTableName





def createFolder():

    global databasenameInput
    global usernameInput
    global ipInput
    global passwordInput



    nameDB = databasenameInput.get()
    host = ipInput.get()
    user = usernameInput.get()
    password = passwordInput.get()
    print(nameDB)


    conn = mysql.connector.connect(host=host, user=user, password=password, database=nameDB)
    cursor = conn.cursor()
    cursor.execute("""SHOW TABLES""")
    tables = cursor.fetchall()
    conn.close()


    try:
        os.mkdir('Controllers')
    except OSError:
        pass
    try:
        os.mkdir('Models')
    except OSError:
        pass
    try:
        os.mkdir('Views')
    except OSError:
        pass
    try:
        os.mkdir('Views/_Helpers')
    except OSError:
        pass
    i=0
    numberTable = len(tables)
    while(i<numberTable):


        ##CREATION DES FICHIERS DU CONTROLLER
        nomFichier = getUsableTableName(str(tables[i]))+'.php'
        try:
            fichier = open('Controllers/'+nomFichier, "w")
            fichier.write('<?php\nnamespace Controllers;\nuse Kernel\Session,\n    Kernel\\Ut')
            fichier.write('ils,\n    Kernel\View;\nclass '+getUsableTableName(str(tables[i]))+' exte')
            fichier.write('nds \Kernel\Controller { \n    public static function _setAction($actionName){ \n        switch($actionName){ \n            case"display":\n                self::display();\n                break;\n            }\n        }\n    public static function display(){\n        $table'+getUsableTableName(str(tables[i]))+' = \Models\\'+getUsableTableName(str(tables[i]))+'::getAll();\n        self::setView(new View("'+getUsableTableName(str(tables[i])))
            fichier.write(' ","display"));\n        self::getView()->'+getUsableTableNameMin(str(tables[i]))+' = $table'+getUsableTableName(str(tables[i]))+';\n        }\n    }')
        except OSError:
            pass

        ##CREATION DES FICHIERS DU MODELS



        try:
            fichier = open('Models/'+nomFichier, "w")

            fichier.write("<?php\nnamespace Models;\nclass "+getUsableTableName(str(tables[i]))+" extends \Kernel\Object{\n    protected static $_table='"+getUsableTableNameMin(str(tables[i]))+"';\n}")
        except OSError:
            pass
        ##CREATION DES DOSSIER/FICHIERSDES VUES


        try:
            os.mkdir('Views/'+getUsableTableName(str(tables[i])))
        except OSError:
            pass
        try:
            fichier = open('Views/'+getUsableTableName(str(tables[i]))+'/display.php', "w")
            fichier.write("<?php \n")
            fichier.write("var_dump($this->"+getUsableTableNameWithoutLower(str(tables[i]))+");")
        except OSError:
            pass
        try:
            fichier = open('Views/_Helpers/header.php', "w")
            fichier.write('<?php')
            fichier = open('Views/_Helpers/footer.php', "w")
            fichier.write('<?php')
        except OSError:
            pass
        i=i+1


















fenetre = Tk()
fenetre.resizable(width=False, height=False)
fenetre.title("Script Python Mvc !")
fenetre.configure(bg = "black")
fenetre.configure(width = 400,height=400)


cadre1 = Frame(fenetre, width=1, height=300, borderwidth=0, bg='black')
cadre1.grid(row=0,column=1)


cadre1 = Frame(fenetre, width=300, height=1, borderwidth=0, bg='black')
cadre1.grid(row=1,column=0)



can = Frame(fenetre, width=300, height=300,bg='black')
can.grid(row=0,column=0)




##Initize Label Form


labelIp = Label(can, text="Ip :",background="black",foreground="green")
labelIp.pack()


##Initize Input Form
global ipInput

varIpInput = StringVar()


ipInput= Entry(can,bg="black",fg = "green",textvariable=varIpInput)
ipInput.pack()


labelIp = Label(can, text="Database : ",background="black",foreground="green")
labelIp.pack()


databasenameInput= Entry(can,bg="black",fg = "green")
databasenameInput.pack()


labelIp = Label(can, text="UserName :  ",background="black",foreground="green")
labelIp.pack()


usernameInput = Entry(can,bg="black",fg = "green")
usernameInput.pack()

labelIp = Label(can, text="Password :  ",background="black",foreground="green")
labelIp.pack()


passwordInput = Entry(can, show="*",bg="black",fg = "green")
passwordInput.pack()


labelEmpty = Label(can, background="black",foreground="black")
labelEmpty.pack()



b = Button(can, text="Executer", width=10, command=createFolder,background="black",foreground="green",activebackground="black",activeforeground="green")
b.pack()
b.flash()




fenetre.mainloop()