from enum import Enum
from typing import Any
import dolphin_memory_engine as dme
import time

class Datatype(Enum):
    BYTE = 1
    HALFWORD = 2
    WORD = 3
    FLOAT = 4
    DOUBLE = 5
    STRING = 6
    BYTEARRAY = 7
    BOOL = 8
    VOIDPTR = 9

class MemoryWatch:
    def __init__(self, address: int, datatype: Datatype) -> None:
        self.address = address
        self.datatype = datatype
    
    @staticmethod
    def read_halfword(address:int) -> int:
        return (dme.read_byte(address) << 8) + dme.read_byte(address+1)

    @staticmethod
    def read_string(address:int) -> int:
        s = ""
        i = 0
        cur_char = ""
        while (cur_char := chr(dme.read_byte(address+i))) != '\0':
            s += cur_char
            i += 1
        return s
    
    @staticmethod
    def read_bool(address:int) -> bool:
        return not not dme.read_byte(address)

    @staticmethod
    def write_halfword(address:int, value:int) -> None:
        value %= 65536
        dme.write_byte(address, value >> 8)
        dme.write_byte(address+1, value & 0xff)

    @staticmethod
    def write_string(address:int, value:str) -> None:
        for i,e in enumerate(value):
            dme.write_byte(address+i, ord(e))
        dme.write_byte(address+len(value), 0) # add the null terminator at the end
    
    @staticmethod
    def write_bool(address:int, value:bool) -> None:
        dme.write_byte(address, int(value))
    
    _accessor_methods = {
        Datatype.BYTE: (dme.read_byte, dme.write_byte),
        Datatype.HALFWORD: (read_halfword, write_halfword),
        Datatype.WORD: (dme.read_word, dme.write_word),
        Datatype.FLOAT: (dme.read_float, dme.write_float),
        Datatype.DOUBLE: (dme.read_double, dme.write_double),
        Datatype.STRING: (read_string, write_string),
        Datatype.BOOL: (read_bool, write_bool),
        Datatype.VOIDPTR: (dme.read_word, dme.write_word),
    }

    def get_accessors(self):
        return MemoryWatch._accessor_methods[self.datatype]

    def read(self):
        if self.datatype == Datatype.BYTEARRAY:
            return dme.read_bytes(self.address, self.len)
        return self.get_accessors()[0](self.address)
    
    def write(self, value):
        if isinstance(value, Enum):
            value = value.value
        self.get_accessors()[1](self.address, value)

class ByteArrayMemoryWatch(MemoryWatch):
    def __init__(self, address: int, size: int = 0) -> None:
        super().__init__(address, Datatype.BYTEARRAY)
        self.size = size
    
    def read_all(self) -> bytes:
        return dme.read_bytes(self.address, self.size)
    
    def write_all(self, value: bytes):
        self.size = len(value)
        dme.write_bytes(self.address, value)

    def read(self, index: int, datatype: Datatype, length:int=-1):
        assert(index < self.size)
        if datatype == Datatype.BYTEARRAY:
            return dme.read_bytes(self.address + index, length)
        return MemoryWatch._accessor_methods[datatype][0](self.address + index)

class BitFieldMemoryWatch(MemoryWatch):
    def __init__(self, address: int, datatype: Datatype, bitmask: int = 0):
        super().__init__(address, datatype)
        self.bitmask = bitmask
    
    def read(self) -> bool:
        return self.get_accessors()[0](self.address) & self.bitmask == self.bitmask
    
    def write(self, value:bool) -> None:
        accessors = self.get_accessors()
        res = accessors[0](self.address)
        if value:
            res |= self.bitmask
        else:
            res &= ~self.bitmask
        accessors[1](self.address, res)

dme.hook()

game_region = chr(dme.read_byte(0x80000003))
game_revision = dme.read_byte(0x80000007)

if not dme.is_hooked():
    print(f'{"[" + "Console" + "]":>15} Not hooked to an instance of SPM, defaulting to us0.')
    game_region = chr('E')
    game_revision = 0
    while not dme.is_hooked():
        time.sleep(5)
        dme.hook()
    print(f'{"[" + "Console" + "]":>15} Hooked... Changing Regional Differences')
    game_region = chr(dme.read_byte(0x80000003))
    game_revision = dme.read_byte(0x80000007)
else: 
    print(f'{"[" + "Console" + "]":>15} Hooked... Changing Regional Differences')
    game_region = chr(dme.read_byte(0x80000003))
    game_revision = dme.read_byte(0x80000007)

def get_address(name: str) -> int:
    return watches[name]["addresses"][game_region][game_revision]

def get_watch(name: str) -> MemoryWatch:
    watch = watches[name]
    address = watch["addresses"][game_region][game_revision]
    if watch["datatype"] == Datatype.BYTEARRAY:
        return ByteArrayMemoryWatch(address, watch["size"])
    return MemoryWatch(address, watch["datatype"])

watches = {

}