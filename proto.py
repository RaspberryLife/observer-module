#!/usr/bin/python
import sys
import raspberrylife_pb2 as proto


def sendMessage( message ):
    rbl_message = raspberrylife_pb2.RBLMessage()
    rbl_message.id = "observer_module"
    rbl_message.messageType = addressbook_pb2.MessageType.RUN_INSTRUCTION;
    run_instruction = rbl_message.runInstruction.add()
    runInstruction.

    print( rbl_message );
    return;

sendMessage( "hallo" );
