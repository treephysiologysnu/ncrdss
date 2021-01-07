import os

def check_completed(cultivarID):
    path = './data/{}'.format(cultivarID)
    if not os.path.exists(path):
        return True
    f = open(path, 'r')
    lines = f.readlines()
    if len(lines) >= 400:
        f.close()
        os.rename(path, './completed/{}'.format(cultivarID))
        return True
    else:
        f.close()
        return False

def add_coeffs(cultivarID, coeff):
    path = './data/{}'.format(cultivarID)
    if not os.path.exists(path):
        return False
    with open(path, 'a+') as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0 :
            f.write("\n")
        # Append text at the end of file
        f.write('{}'.format(coeff))