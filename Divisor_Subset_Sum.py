import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_number', help = 'need input number as integer', required = True)
args = vars(ap.parse_args())

x = int(args["input_number"])
inp_list = []

for i in range(1,x+1):
    if x % i == 0:
        inp_list.append(i)

prod = 1
for j in inp_list:
    prod = prod * (j+1)

print("result of subset of all divisor ", prod - 1)
