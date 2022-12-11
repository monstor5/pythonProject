## находить фаил
import os
from sourceCode2 import pictures
from ngf import Binari_cod

br = Binari_cod()
t = int(input("Двоичный код, будет приобрачовываться в текст с двоичного кода: "))
p = ("Текст, будем преобразовывать в двоичный код: ")
print(br.text_from_bits(bits = t))
print(br.text_to_bits1(text = p))