try:
    file=open('sample.txt','r')
    result=file.read()
    print(result)
except FileNotFoundError:
    print("file not found")
file.close()