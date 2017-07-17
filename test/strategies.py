import hypothesis.strategies as ST
import string

ascii_string = ST.text(alphabet=string.ascii_letters, min_size=1, max_size=100)
whitespace = ST.text(alphabet=string.whitespace, min_size=1, max_size=100)
