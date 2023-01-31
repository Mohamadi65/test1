import pandas as pd


def Not_Null(nom_colonne):

        lire = pd.read_csv("C:/code/python/Mouna/Données-Etudiants.csv", header=0, sep=";")

        for i in range(len(lire)):
            # print(format(row.id,'0.0f'), row.nom)
            essayer = lire.loc[i, nom_colonne]

            if str(essayer) == 'nan' or str(essayer)=='null':
                #print("différent de null", format(essayer, '0.0f'))



                with open("fichier_log.txt", "a", encoding='utf-8') as f:

                        f.write("la colonne ")
                        f.write("'")
                        f.write(nom_colonne)
                        f.write("'")
                        f.write(" à la ligne ")
                        f.write(str(i + 2))
                        f.write(" est vide\n")



if __name__ == '__main__':
    Not_Null('id_dept')
