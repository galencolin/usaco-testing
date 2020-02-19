import os, sys, subprocess

print('Compiling...')
sys.stdout.flush()
cmd = ['g++', 'file.cpp', '-O2', '-Wl,--stack,268435456']
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

cases = 10
filename = ''
if (sys.argv[1]):
	cases = int(sys.argv[1])
if (sys.argv[2]):
	filename = sys.argv[2]

print('Judging...')
sys.stdout.flush()
for i in range(cases):
	p = subprocess.Popen('cp test-files/' + str(i + 1) + '.in ' + filename + '.in')
	p.wait()
	
	cmd = ['./a']
	verdict = '*'
	try:
		subprocess.run(cmd, timeout = 2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	except subprocess.TimeoutExpired:
		verdict = 't'
	except:
		verdict = '!'
		
	os.system('tr -d \'\\r\' < test-files/' + str(i + 1) + '.out > '+ str(i + 1) + '.out')
		
	if (verdict == '*'):
		res = subprocess.check_output('bash comper ' + str(i + 1) + '.out ' + filename + '.out')
		res = int(res)
		if (res == 1):
			verdict = 'x'
		
	print(verdict, end = ' ')
	sys.stdout.flush()
	
	p = subprocess.Popen('rm ' + filename + '.in')
	p.wait()
	p = subprocess.Popen('rm ' + str(i + 1) + '.out')
	p.wait()

os.system('rm ' + filename + '.out')