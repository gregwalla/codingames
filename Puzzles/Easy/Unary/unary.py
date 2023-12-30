import sys

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
        if len(bin(i)[2:]) == 7: 
            m.append(bin(i)[2:])
        elif len(bin(i)[2:]) == 6 : 
            m.append('0' + bin(i)[2:])
  return m

m = input()
m_bin = toBinary(m) 
print(f"input : {m}", file=sys.stderr, flush=True)
print(f"bin  : {m_bin}", file=sys.stderr, flush=True)

prefix = {'0': '00', '1': '0'}
seqs = str()

for j , serie in enumerate(m_bin): 
    assert len(serie) == 7
    print(f"j : {j}", file=sys.stderr, flush=True)
    print(f"serie : {serie}", file=sys.stderr, flush=True)
    seq = str()
    counter = 1
    for i, c in enumerate(serie[:-1]): 
        if c == serie[i+1]: #if same character
            if i == 5: #if last equals just before
                counter += 1 #count it
                seq += f"{prefix[c]} {counter*str(0)}" #add to seq with no space
            else : 
                counter += 1 

        elif c != serie[i+1] : 
            if i == 5: #last 
                seq += f"{prefix[c]} {counter*str(0)} {prefix[serie[-1]]} {str(0)}"
            else : 
                seq += f"{prefix[c]} {counter*str(0)} "
                counter = 1 
                # Write an answer using print
            
    print(f"testing  : {m_bin[j-1][-1]} == {serie[0]}", file=sys.stderr, flush=True)
    if j>0 and str(m_bin[j-1][-1]) == str(serie[0]) :
        print(f"seq before  : {seq}", file=sys.stderr, flush=True)
        if prefix[serie[0]] == '0':
            seq = seq[2:]
        else:
            seq = seq[3:]
        print(f"seq after  : {seq}", file=sys.stderr, flush=True)
    seqs += seq

print(f"{seqs}")


