from IPC_HERMES_9852.Models import CheckAlive
import xml.etree.ElementTree as ET
import datetime as DT

def CheckAliveMessage(CheckAlive: CheckAlive):
    # Create the root element
    root = ET.Element("Hermes")

    # Add optional timestamp to root in W3C_DATE_TIME
    now = DT.datetime.now()
    root.set("Timestamp",DT.datetime.strftime(now,"%Y-%m-%dT%H:%M:%S.%f"))
    
    return "hello world: server check alive"