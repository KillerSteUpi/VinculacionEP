
#from asyncio import SafeChildWatcher
#from http import client
import pygsheets
import pandas as pd 
from statistics import mean
from datetime import datetime
from numpy.random import randn
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime

while True:
    now = datetime.now()
    data= pd.read_csv(
    'https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
    df = pd.DataFrame(data, columns = ['nombre', 'edad', 'sexo','peso','altura', 'colesterol'])
    promedio= df['peso'].iloc[0:4].mean(skipna = True)#omite los ceros: skipna = True
    promedio1=df['colesterol'].iloc[0:4].mean(skipna = True)
    promedio2=df['altura'].iloc[0:4].mean(skipna = True)
    promedio3=df['edad'].iloc[0:4].mean(skipna = True)
    moda=df['sexo'].iloc[0:4].mode()
    print("Datos de colesterol\t",now,"\n",df.iloc[0:4],"\n")
    print('El promedio del Peso es:',promedio)
    print('El promedio del Colesterol es:',promedio1)
    print('El promedio del Altura es:',promedio2)
    print('El promedio de la Edad es:',promedio3)
    print('La moda del sexo es\n',moda)
    #print(df.describe())


    #prueba 2
    #gc = pygsheets.authorize(service_file='promediomapa-b71ffa8ace47.json')
    gc = pygsheets.authorize(service_file='promedios-399723-9f2eb75362f1.json')

    #open the google spreadsheet 
    #sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/18Q-wIYeEqXGWty0od5t-U49JgcVJ-FEHEA2u1R6wcLk/edit#gid=0')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nK3WYNyq-FtFSkrCtpLJ7zji3Sm367VAb3U0BoaoSvw/edit#gid=0')
    #select the first sheet 
    wks = sh[0]

    #update the first sheet with df, starting at cell B2. 
    wks.set_dataframe(df,'B2')

    #Actualizo la celda de promdeio
    #sh.update_acell('E17',promedio1)


    #Prueba1

    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds= ServiceAccountCredentials.from_json_keyfile_name("promedios-399723-9f2eb75362f1.json", scope)
    client=gspread.authorize(creds)
    sheet= client.open("PromediosXotepingo").sheet1
    sheet.update_acell('E17',promedio)
    sheet.update_acell('G17',promedio1)
    sheet.update_acell('F17',promedio2)
    sheet.update_acell('C17',promedio3)
    sheet.update_acell('B17','Promedio')
    sheet.update_acell('A1','Prueba General')


    
    time.sleep(60)




