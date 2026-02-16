text = "ihave2penpencil3onecar"

# w.a.p to display digits in the text

iis_digit = False

for ch in text:

    if ch.isdigit():

        print(ch,end=" ")

        iis_digit = True


if iis_digit == False:

    print("No digits found")

