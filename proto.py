#!/usr/bin/python
import sys
import raspberrylife_pb2 as proto


def sendMessage( message ):
    rbl_message = raspberrylife_pb2.RBLMessage()
    rbl_message.id = "observer_module"
    rbl_message.messageType = raspberrylife_pb2.MessageType.RUN_INSTRUCTION;
    run_instruction = rbl_message.runInstruction.add()
    actuator = runInstruction.Actuator();
    actuator.actuatorType = raspberrylife_pb2.ActuatorType.CLIENT;
    actuator.actuatorId = 0; # id=0 for admin user
    instruction = runInstruction.Instruction();
    instruction.instructionId = 0; # id=0 for user notification
    param = instruction.parameters.add()
    param = "Intruder detected" +  message;

    print( rbl_message );

    return;

sendMessage( "hallo" );
