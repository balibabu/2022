try:
    f = open('file1', 'r')
    f.write('”work is worship”')
    f.close()
except Exception as e:
    print(e)

#[Errno 2] No such file or directory: 'file1'
