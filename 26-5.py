import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))

result=re.match('^Hello.*?(\d+).*Demo',content)
print(result)
print(result.group())
print(result.group(0))
print(result.group(1))
print(result.span())