#!/usr/bin/python3
""" UTF-8 validation module.
"""


def validUTF8(data):
	""" Checks if a list of integers are valid UTF-8 codepoints.
	"""
	num_bytes = 0
	for byte in data:
		if num_bytes == 0:
			if (byte >> 5) == 0b110:
				num_bytes = 1
			elif (byte >> 4) == 0b1110:
				num_bytes = 2
			elif (byte >> 3) == 0b11110:
				num_bytes = 3
			elif (byte >> 7):
				return False
		else:
			if (byte >> 6) != 0b10:
				return False
			num_bytes -= 1
	return num_bytes == 0
