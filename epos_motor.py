from common import make_can_frame
from enum import IntEnum

# QC_FACTOR = 402000 / 360
QC_FACTOR = 1  # 625000 / 360
DIGITAL_OUTPUT_1 = False
DIGITAL_OUTPUT_2 = False


class EPOSCommand(IntEnum):
    SHUTDOWN = 0b00000110
    SWITCH_ON = 0b00000111
    SWITCH_ON_AND_ENABLE = 0b00001111
    DISABLE_VOLTAGE = 0b00000000
    QUICK_STOP = 0b00000010
    DISABLE_OPERATION = 0b00000111
    ENABLE_OPERATION = 0b00001111
    FAULT_RESET = 0b10000000


def enable(node: int):
    return [
        make_can_frame(node=node, index=0x6040, data=EPOSCommand.SHUTDOWN),
        make_can_frame(node=node, index=0x6040, data=EPOSCommand.SWITCH_ON),
        make_can_frame(node=node, index=0x6040, data=EPOSCommand.SWITCH_ON_AND_ENABLE),
        make_can_frame(node=node, index=0x6060, data=0x10)]


def disable(node: int):
    return [make_can_frame(node=node, index=0x6040, data=EPOSCommand.DISABLE_OPERATION)]


def read_status(node: int):
    return [make_can_frame(node=node, index=0x6041, write=False)]


def read_position(node: int):
    return [make_can_frame(node=node, index=0x6064, write=False)]


def fault_reset(node: int):
    return [make_can_frame(node=node, index=0x6040, data=EPOSCommand.FAULT_RESET),
            make_can_frame(node, 0x6040, 0, EPOSCommand.SHUTDOWN),
            make_can_frame(node, 0x6040, 0, EPOSCommand.SWITCH_ON_AND_ENABLE), ]


def set_angle_value(node: int, angle: int, absolute=False):
    qc_to_rotate = int(QC_FACTOR * angle)
    if absolute:
        return [
            make_can_frame(node=node, index=0x607A, data=qc_to_rotate),
            # make_can_frame(node=node, index=0x6040, data=0x000F),
            # make_can_frame(node=node, index=0x6040, data=0x002F),
            make_can_frame(node=node, index=0x6040, data=0x003F)
        ]
    else:
        return [
            make_can_frame(node=node, index=0x607A, data=qc_to_rotate),
            # make_can_frame(node=node, index=0x6040, data=0x000F),
            # make_can_frame(node=node, index=0x6040, data=0x007F)]
            # make_can_frame(node=node, index=0x6040, data=0x006F),
            make_can_frame(node=node, index=0x6040, data=0x007F)]


def enable_digital_1(node: int):
    global DIGITAL_OUTPUT_1, DIGITAL_OUTPUT_2
    DIGITAL_OUTPUT_1 = True
    if DIGITAL_OUTPUT_2:
        return [make_can_frame(node, 0x60FE, 1, 0x30000)]
    else:
        return [make_can_frame(node, 0x60FE, 1, 0x10000)]


def enable_digital_2(node: int):
    global DIGITAL_OUTPUT_1, DIGITAL_OUTPUT_2
    DIGITAL_OUTPUT_2 = True
    if DIGITAL_OUTPUT_1:
        return [make_can_frame(node, 0x60FE, 1, 0x30000)]
    else:
        return [make_can_frame(node, 0x60FE, 1, 0x20000)]


def disable_digital_1(node: int):
    global DIGITAL_OUTPUT_1, DIGITAL_OUTPUT_2
    DIGITAL_OUTPUT_1 = False

    if DIGITAL_OUTPUT_2:
        return [make_can_frame(node, 0x60FE, 1, 0x20000)]
    else:
        return [make_can_frame(node, 0x60FE, 1, 0x0)]


def disable_digital_2(node: int):
    global DIGITAL_OUTPUT_1, DIGITAL_OUTPUT_2
    DIGITAL_OUTPUT_2 = False

    if DIGITAL_OUTPUT_1:
        return [make_can_frame(node, 0x60FE, 1, 0x10000)]
    else:
        return [make_can_frame(node, 0x60FE, 1, 0x0)]


def init_device(node: int, rpm=0x1388):
    return [
        make_can_frame(node, 0x6040, 0, 0x0080),
        # make_can_frame(node, 0x6060, 0, 0x08),  # operation mode=Cyclic Synchronous Position Mode
        make_can_frame(node, 0x6060, 0, 10),  # operation mode=profile position
        make_can_frame(node, 0x6081, 0, rpm),  # rpm speed 1-25000 = 10_000 rpm
        make_can_frame(node, 0x6040, 0, EPOSCommand.SHUTDOWN),  # ????
        make_can_frame(node=node, index=0x6040, data=EPOSCommand.SWITCH_ON),
        # make_can_frame(node, 0x6040, 0, EPOSCommand.SWITCH_ON_AND_ENABLE),
        # make_can_frame(node, 0x2078, 2, 0x3000)  # DO configuration
    ]
