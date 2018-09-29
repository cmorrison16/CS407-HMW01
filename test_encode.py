from encode import encode

def test_string():
	assert encode("aaa") == "a3"
def test_empty_string():
	assert encode("") == ""
def test_two_letter_string():
	assert encode("aabbb") == "a2b3"
def test_single_letter():
	assert encode("a") == "a1"
	assert encode("abcd") == "a1b1c1d1"
def test_long_string():
	assert encode("aaabbbcddcc") == "a3b3c1d2c2"
	assert encode("abcdaaaaaaaz") == "a1b1c1d1a7z1"
