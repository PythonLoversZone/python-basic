var1 = 'Hello World!'
var2 = "Hello World!"
#       0123456789


var3 = 'Hello'
var4 = "World!"


print(var1)
print(var2)
print(var1[1])  # 'e'
print(var1[3])  # 'l'
print(var1[1:3])  # 'ell'
print("H" in var1)  # true
print("H" not in var1)  # false


print(var3)
print(var4)
print(var3 + var4)
print(var3 * 10)

# 特殊字符
print("hello's worldhello's worldhello's worldhello's worldhello's\
worldhello's worldhello's worldhello's worldhello's worldhello's\
worldhello's worldhello's worldhello's worldhello's worldhello's world")
print("hello's worldhello's worldhello's worldhello's worldhello'sworldhello's worldhello's worldhello's worldhello's worldhello'sworldhello's worldhello's worldhello's worldhello's worldhello's world")

print("\\")
print("\'")
print("'")
print("\"")
print("abcde\bf")  # abcdf

print("xiaomo\n")
print("xinyi\n")
print("nuonuo")

print("xiaomo\txinyi\tnuonuo")
print("xiaomo\vxinyi\vnuonuo")
print(r"xiaomo\vxinyi\vnuonuo")

print("""hello world
I am xiaomo
please teach me english
""")

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''

print(errHTML)

print('''
CREATE TABLE users (
login VARCHAR(8),
uid INTEGER,
prid INTEGER)
''')


print(u'Hello\u0020World !')  # Hello World !
