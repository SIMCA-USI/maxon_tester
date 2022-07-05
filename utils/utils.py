import struct


def decoder_can(msg: bytearray, extended=False):
    try:
        if extended:
            cobid, specifier = struct.unpack('>IB8x', msg)
            index, sub_index = struct.unpack('<5xHB5x', msg)
        else:
            cobid, specifier = struct.unpack('>2xHB8x', msg)
            index, sub_index = struct.unpack('<5xHB5x', msg)
        data_raw = bytearray(msg[8:-1])
    except Exception as e:
        print(f'Error decoding CAN {msg}')
        data_raw, cobid, specifier, index, sub_index = 0, 0, 0, 0, 0
    return msg, data_raw, cobid, specifier, index, sub_index


def make_can_frame(node, index, sub_index=0, data=0, write=True) -> bytearray:
    if write:
        return bytearray(struct.pack('<2xBBBHBiB', 6, node, 0x22, index, sub_index, data, 0x08))
    else:
        return bytearray(struct.pack('<2xBBBHBiB', 6, node, 0x40, index, sub_index, data, 0x08))


def make_can_msg(node, index=0x0000, sub_index=0, data=0, write=True):
    msg = make_can_frame(node, index, sub_index, data, write)
    return msg


def convert_types(ros2_type, data):
    function = ros2_types.get(ros2_type)
    if function is not None:
        return function(data)
    else:
        return data


ros2_types = {
    'string': str,
    'int32': int,
    'double': float
}
