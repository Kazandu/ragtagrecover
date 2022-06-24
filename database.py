from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import configparser
from datetime import *
from typing import Optional
dateToday = datetime.date(datetime.now()).strftime("%Y%m%d")
config = configparser.ConfigParser()
pwd=os.getcwd()

def logwriterfunc(msg):
    os.makedirs(pwd+"/logs/", exist_ok=True)
    logWriter = open (pwd+"/logs/"+dateToday+"_ragtagrecoveryapi.log", "a+")
    logWriter.write(datetime.time(datetime.now()).strftime("[%H:%M:%S]")+" "+msg+"\n")
    logWriter.close()


if (os.path.isfile(pwd+"/config.ini")):
    config.read(pwd+'/config.ini')
else:
    print("ERROR: NO DB-CONFIG FILE! Exiting...")
    logwriterfunc("[ERROR] - Started without DB config File, please rename TEMPLATEdbconfig.ini to dbconfig.ini and fill the parameters.\n")
    quit()

dbuser = config['MAIN']['dbuser']
dbpw= config['MAIN']['dbpw']

DATABASE_URL = "mysql+mysqlconnector://"+dbuser+"@localhost:3306/ragtagrecover"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()