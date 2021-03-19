
# -*- coding: utf-8 -*-
import os
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *
from MCP23XXX.MCP23017_I2C import MCP23017_I2C


logger = logging.getLogger(__name__)


@parameters([Property.Select("MCPPin", options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),
             Property.Select("MCPAddress", options=["0x20", "0x21","0x22","0x23","0x24","0x25","0x26","0x27"]),
             Property.Select("MCPInverted", options=["True", "False"])
             ])
class MCP23XXX(CBPiActor):
    
    SetValueOff=0
    SetValueOn=1
    
    @action("action", parameters={})
    async def action(self, **kwargs):
        print("Action Triggered", kwargs)
        pass
    
    def init(self):
        print("INIT MCP")
        
        
        self.state = False
        pass

    async def on(self, power=0):
        self.MCP1.set_mode(int(self.MCPPin)-1, "output")
        self.MCP1.output(int(self.MCPPin)-1, self.SetValueOn)

        logger.info("ACTOR %s ON" % self.id)
        self.state = True

    async def off(self):
        self.MCP1.set_mode(int(self.MCPPin)-1, "output")
        self.MCP1.output(int(self.MCPPin)-1, self.SetValueOff)

        logger.info("ACTOR %s OFF " % self.id)
        self.state = False

    def get_state(self):
        return self.state
    
    async def run(self):
        self.MCPPin = int(self.props.get("MCPPin"))
        self.MCPAddress = int(self.props.get("MCPAddress"),16)
        self.MCPInverted = self.props.get("MCPInverted")

        self.MCP1 = MCP23017_I2C("MCP23017", self.MCPAddress , "16bit")
        
        
        #self.MCP = MCP23017_I2C("MCP23017", self.MCPAddress) 
        
        if self.MCPInverted == "True":
            self.SetValueOn=0
            self.SetValueOff=1
        else:  
            self.SetValueOn=1
            self.SetValueOff=0

        pass


def setup(cbpi):
    cbpi.plugin.register("MCP23XXX", MCP23XXX)
    #cbpi.plugin.register("MyCustomSensor", CustomSensor)
    #cbpi.plugin.register("MyustomWebExtension", CustomWebExtension)
    pass

