import subprocess
"""
python exec shell command 
save the result into file
2018 12 15
"""
def run_cmd(cmd):
    result_str=''
    process = subprocess.Popen(cmd, shell=True,
              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result_f = process.stdout
    error_f = process.stderr
    errors = error_f.read()
    if errors: pass
    result_str = result_f.read().strip()
    if result_f:
       result_f.close()
    if error_f:
       error_f.close()
    return result_str


def execshell(str):
    fd = open("list.txt","a+")
    p =subprocess.Popen(str,stdout=fd,shell=1)
    if p.poll:
        return
    p.wait()
    return 

def main():
    execshell("pip list")

if __name__=="__main__":
    main()