import mysql.connector
import json
from datetime import datetime
from datetime import date
from decimal import Decimal

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='northwind', port=3307)
cursor= cnx.cursor()
query= ("SELECT * from order_details WHERE inventory_id=63")



def proccessSelect(query,cnx,cursor):
    cursor.execute(query)
    campos = cursor.column_names
    datalist=[]

    for data in cursor:
        datalist.append(list(data))

    #cantidad de filas de la consulta
    rows = cursor.rowcount

    def makeJson(campos, datalist, rows):
        datset=[]
        fields=[]
        
        #se llena la lista fields con lso nombres d elos campos
        for col in campos:
            fields.append(col)   
        
        finalset=[]
        
        
        for y in range(rows):
            midset={}
            for x in range(len(fields)):   #7 campos
                if (isinstance(datalist[y][x],(datetime, date))):
                    midset[fields[x]] = datalist[y][x].strftime("%m/%d/%Y, %H:%M:%S")
                    continue
                if (isinstance(datalist[y][x],bytes)):
                    midset[fields[x]] = datalist[y][x].decode("utf-8")
                    continue
                if (isinstance(datalist[y][x],Decimal)):
                    midset[fields[x]] = float(datalist[y][x])
                    continue


                midset[fields[x]] = datalist[y][x]            

            finalset.append(midset)        

        print(finalset)

        f = json.dumps(finalset, indent=2)

        print(f)


    makeJson(campos,datalist, rows)
    cnx.close()

proccessSelect(query,cnx,cursor)