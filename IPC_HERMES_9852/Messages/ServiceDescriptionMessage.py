'''
Convert the Model to serialized XML Hermes ServiceDescription message
'''
from IPC_HERMES_9852.Models import ServiceDescription
import xml.etree.ElementTree as ET
import datetime as DT

def ServiceDescriptionMessage(ServiceDescription: ServiceDescription):
    # Create the root element
    root = ET.Element("Hermes")
    message = ET.SubElement(root, "ServiceDescription")
    
    # Add optional timestamp to root in W3C_DATE_TIME
    now = DT.datetime.now()
    
    root.set("Timestamp",DT.datetime.strftime(now,"%Y-%m-%dT%H:%M:%S.%f"))
    
    # Create the child elements and add them to the root element
    machine_id = ET.SubElement(message, ServiceDescription.MachineId)
    lane_id = ET.SubElement(message, ServiceDescription.LaneId)
    interface_id = ET.Subelement(message, ServiceDescription.InterfaceId)
    version = ET.SubElement(message, ServiceDescription.Version)
    supported_features = ET.SubElement(message, "list of feature here")
    
    return ET.tostring(root)