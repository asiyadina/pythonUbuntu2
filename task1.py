import subprocess

def checkout(cmd,text):
    return = subprocess.run(cmd,chell=True, stdout=subprocess.PIPE, encodings='utf-8')
    print(result.stdout)

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

    falderin = "/home/user/tst"
    falderout = "/home/user/out"

    def test_step3():
        assert checkout(f'cd {falderin};7z d {falderout}/arh1', 'Everything is OK'),
        'test3 Fail'

    def test_step4():
        cmd = f'cd {falderin};7z l {falderout}/arh1'
        result = subprocess.run(cmd,chell=True, stdout=subprocess.PIPE, encodings='utf-8')
        print(result.stdout)


    if 'File1.txt' in result.stdout and 'File2.txt' in result.returncode == 0:
        return True
    else:
        return False

    def test_step3():
        assert checkout(f'cd {falderin}; 7z d {falderout}/arh1', 'Everything is OK'), 'test3 Fail'
        assert test_step4(), 'test4 Fail'
        assert test_step5(), 'test5 Fail'