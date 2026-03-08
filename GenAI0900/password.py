import re
exp = "[1-100{4}]+@,$,#,!,*[a-zA-Z0-9{6}]"
st = "the password is 1234@kawal and the other is 1256*singh and one more is 2345 and 89045kwalnain678"
print(re.findall(pattern=exp, string=st))
