# ord()查看字符的Unicode码，chr()将Unicode码转为字符
# 加密代码
text = input('请输入要加密的文字：')
secret = ''
for char in text:
    secret += chr(ord(char) + 1)
print(f'加密后的内容为：{secret}')

# 解密代码
secret = input('请输入要解密的文字：')
text = ''
for char in secret:
    text += chr(ord(char) - 1)
print(f'解密后的内容为：{text}')