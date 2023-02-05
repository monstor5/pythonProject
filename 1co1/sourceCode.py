## находить фаил
import os
##from sourceCode2 import pictures
from ngf import Binari_cod

br = Binari_cod
p = str(input())
print(br.text_to_bits1(text = p))
t = str(input("Двоичный код, будет приобрачовываться в текст с двоичного кода: "))
print(br.text_from_bits(bits = t))
