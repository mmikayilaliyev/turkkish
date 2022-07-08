import subprocess
import sys
from more_itertools import strip

"""
fi - file input
fo - file output
pm - function which will be tested
"""

def func(fi ,fo ,pm) :
	count = 0
	test = 1
	with open(fi,'r') as file_in :
		with open(fo,'r') as file_out :		
			while True:
				count = count + 1
				line_in = (file_in.readline()).strip()
				line_out = (file_out.readline()).strip()
				if line_in == '':
					if count == test:
						print('All tests passed')
					print('Test ended')
					sys.exit()
				p = subprocess.run([pm],input = line_in,text = True, capture_output = True)
				k = str(p.stdout.strip())
				if (k == line_out) == True:
					test = test +1
				else:
					print('Test {} failed.\nExpected output: {}\nActual output: {}'.format(count,line_out,k))

func(fi = sys.argv[1],fo = sys.argv[2],pm = sys.argv[3])
