from audioop import add
from fastapi import FastAPI, Request, Query, Depends
from sqlalchemy.orm import Session
import os
import configparser
from datetime import *
from typing import Optional
import uvicorn
from model import ToDo
import schema
from database import SessionLocal, engine
import model
dateToday = datetime.date(datetime.now()).strftime("%Y%m%d")
config = configparser.ConfigParser()
pwd=os.getcwd()
#Logging
def logwriterfunc(msg):
    os.makedirs(pwd+"/logs/", exist_ok=True)
    logWriter = open (pwd+"/logs/"+dateToday+"_ragtagrecoveryapi.log", "a+")
    logWriter.write(datetime.time(datetime.now()).strftime("[%H:%M:%S]")+" "+msg+"\n")
    logWriter.close()

#Check if config file exists
#if (os.path.isfile(pwd+"/config.ini")):
#    config.read(pwd+'/config.ini')

#else:
#    print("ERROR: NO CONFIG FILE! Exiting...")
#    logwriterfunc("[ERROR] - Started without config File, please rename TEMPLATEconfig.ini to config.ini and fill the parameters.\n")
#    quit()

#checkerdir = config['MAIN']['checkerdir']
#dldir = config['MAIN']['dldir']

#DB STUFF
model.Base.metadata.create_all(bind=engine)
def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI(
    title="Ragtag Recovery API",
    description="A simple API for recovering ragtags archive.",
    version="0.0.1"
)

@app.on_event("startup")
async def startup_event():
    logwriterfunc("[INFO] - Started with config File, harobo-!\n")

@app.on_event("shutdown")
async def shutdown_event():
    logwriterfunc("[INFO] - Shutting down...otsurobo...\n")

@app.get('/', tags=['main'])
async def root():
  return {'message':'Harooboo, Ragtag recovery API Online!'}

@app.get('/todo/list', tags=['checker'])
async def todolist(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(ToDo).all()
    return {'result:':records}
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5069)