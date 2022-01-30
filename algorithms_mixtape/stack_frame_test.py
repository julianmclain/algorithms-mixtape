"""Virtual OS lab exercise

This program builds on the VM lab from earlier in the course


https://my.bradfieldcs.com/architecture/2021-01/virtual-os-lab/exercise/
"""
import unittest


# Instruction set
# Note that ADD and SUB both store their result in register 1
LOAD_WORD = 0x01
STORE_WORD = 0x02
ADD = 0x03
SUB = 0x04
HALT = 0xFF

memory = [0] * 256
process_counter = 0
memory_entries = {}  # maps process id to location in memory
registers = {
    0x00: 0x0000,  # program counter
    0x01: 0x0000,  # reg 1
    0x02: 0x0000,  # reg 2
    0x03: 0x0000,  # base register
    0x04: 0x0000,  # bounds register
}


def main_loop() -> int:
    """Simulation of the fetch-decode-execute cycle

    :param memory: 20 bytes of memory, simulated by an array with length 20
    """
    while True:
        curr_count = registers[0x00]
        curr_instruction = memory[curr_count]

        if curr_instruction == HALT:
            registers[0x00] = 0
            break

        elif curr_instruction == LOAD_WORD:
            reg = memory[curr_count + 1]
            word_addr = memory[curr_count + 2]
            registers[reg] = load_num(memory[word_addr], memory[word_addr + 1])

        elif curr_instruction == STORE_WORD:
            word = registers[memory[curr_count + 1]]
            output_addr = memory[curr_count + 2]
            store_num(word, output_addr, memory)

        elif curr_instruction == ADD:
            op1 = registers[memory[curr_count + 1]]
            op2 = registers[memory[curr_count + 2]]
            registers[0x01] = op1 + op2

        elif curr_instruction == SUB:
            op1 = registers[memory[curr_count + 1]]
            op2 = registers[memory[curr_count + 2]]
            registers[0x01] = op1 - op2

        # increment program coutner by 3 since each (non HALT) instruction uses 3 bytes
        registers[0x00] = curr_count + 3

    return 0


def load_num(byte1: int, byte2: int) -> int:
    """Load a 16 bit number assuming little-endian representation
    """
    return byte1 + byte2 * 256


def store_num(num: int, addr: int, memory: int):
    """Store a 16 bit number assuming little-endian representation
    """
    byte1 = num % 256
    byte2 = num // 256
    memory[addr] = byte1
    memory[addr + 1] = byte2


def twos_comp(num: int, num_bits: int) -> int:
    """Calculate the two's compliment of an n-bit unsigned int
    """
    if num >> (num_bits - 1) == 1:
        return num - 2 ** num_bits
    else:
        return num


def load_program(file: str) -> None:
    """Load an executable VEF program

    - create a new virtual memory space
    - load the instructions into that virtual memory space
    - load the data into that virtual memory space
    - execute the program

    :param file_path:
    :return:
    """
    program_size_limit = 20  # bytes
    addr_base = len(memory_entries.keys()) * program_size_limit
    addr_bounds = addr_base + program_size_limit
    global process_counter
    process_counter += 1
    memory_entries[process_counter] = addr_base
    # Make space in memory or zero out existing data
    # if addr_base >= len(memory):
    #     for i in range(program_size_limit):
    #         memory.append(0)
    # else:
    #     for i in range(program_size_limit):
    #         memory[addr_base + i] = 0

    with open(file, "rb") as f:
        program = f.read()
    num_segments = program[0]

    for i in range(num_segments):
        # parse segment header
        header_length = 3  # bytes
        offset = i * header_length * 2  # times 2 because 2 hex chars per byte
        segment_type = (
            int(hex_string[2 + offset : 4 + offset], 16) >> 7
        )  # get the most significant bit
        segment_addr = (
            int(hex_string[2 + offset : 4 + offset], 16) % 128
        )  # get the least 7 significant bits
        segment_len = int(hex_string[4 + offset : 6 + offset], 16)
        payload_loc = int(hex_string[6 + offset : 8 + offset], 16)
        absolute_starting_loc = 2 * (3 * num_segments + payload_loc + 1)
        segment_data = []
        for i in range(segment_len):
            if i + 1 >= segment_len:
                segment_data.append(hex_string[i])
            elif i % 2 == 0:
                segment_data.append(
                    hex_string[
                        absolute_starting_loc + i : absolute_starting_loc + i + 2
                    ]
                )
        segment = hex_string[
            absolute_starting_loc : absolute_starting_loc + segment_len
        ]

        # save segment to memory
        for i in range(0, len(segment), 2):
            memory[segment_addr + i] = int(hex_string[absolute_starting_loc + i], 16)
        x = 1


class TestVirtualMachine(unittest.TestCase):
    def test_program(self):
        load_program("add_255_3.vef")
        # [1, 1, 16, 1, 2, 18, 3, 1, 2, 2, 1, 14, 255, 0, 0, 0, 161, 20, 12, 0]
        main_memory = [
            0x01,
            0x01,
            0x10,  # load_word r1 (0x10)
            0x01,
            0x02,
            0x12,  # load_word r2 (0x12)
            0x03,
            0x01,
            0x02,  # add r1 r2
            0x02,
            0x01,
            0x0E,  # store_word r1 (0x0E)
            0xFF,  # halt
            0x00,  # unused
            0x00,
            0x00,  # out
            0xA1,
            0x14,  # in1
            0x0C,
            0x00,  # in2
        ]
        status = main_loop()
        self.assertEqual(status, 0)
        self.assertEqual(memory[14], 173)
        self.assertEqual(memory[15], 20)

    def test_negative_nums(self):
        main_memory = [
            0x01,
            0x01,
            0x10,  # load_word r1 (0x10)
            0x01,
            0x02,
            0x12,  # load_word r2 (0x12)
            0x03,
            0x01,
            0x02,  # add r1 r2
            0x02,
            0x01,
            0x0E,  # store_word r1 (0x0E)
            0xFF,  # halt
            0x00,  # unused
            0x00,
            0x00,  # out
            0x50,
            0x00,  # in1 (80)
            0x9C,
            0xFF,  # in2 (-100)
        ]
        status = main_loop()
        self.assertEqual(status, 0)
        result = load_num(main_memory[14], main_memory[15])
        self.assertEqual(twos_comp(result, 16), -20)


if __name__ == "__main__":
    unittest.main()
