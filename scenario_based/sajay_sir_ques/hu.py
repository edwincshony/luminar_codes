note="aab"
magazine="ab"

#kangaroo

strt1=0
strt2=0


while strt1 <len(note) and strt2 <len(magazine):
    if note[strt1]==magazine[strt2]:
        strt1+=1
    strt2+=1

if strt1==len(note):
    print(f"{note} is formed by {magazine}")
else:
    print(f"{note} is not formed by {magazine}")