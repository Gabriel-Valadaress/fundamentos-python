# Data types

# Text Type:	str
string_type = "string type"
print(type(string_type))

# Numeric Types:	int, float, complex
int_type = 2
print(type(int_type))

float_type = 2.5
print(type(float_type))

complex_type = 1j
print(type(complex_type))

# Sequence Types:	list, tuple, range
list_type = [1, "string", 2.5]
print(type(list_type))

tuple_type = (1, "string", 2.5)
print(type(tuple_type))

range_type = range(10)
print(type(range_type))

# Mapping Type:	dict
dict_type = {"name": "Gabriel", "age": 24}
print(type(dict_type))

# Set Types:	set, frozenset
set_type = {"string", 1, True}
print(type(set_type))

frozenset_type = frozenset({"string", 1, True})
print(type(frozenset_type))

# Boolean Type:	bool
boolean_type = True
print(type(boolean_type))

# Binary Types:	bytes, bytearray, memoryview
bytes_type = bytes(4)
print(type(bytes_type))

bytearray_type = bytearray(4)
print(type(bytearray_type))

memoryview_type = memoryview(bytes(4))
print(type(memoryview_type))

# None Type:	NoneType
none_type = None
print(type(none_type))