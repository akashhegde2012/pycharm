# password should be 8 charecters can contain number letter and special charecters
import re
pattern=re.compile(r"[a-zA-z0-9%$@#]{8,}\d")#\d to make sure it ends with a digit
string='asdfljk232$5'
check=pattern.fullmatch(string)
print(check)

