str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(":")+1
end = len(str)
number = float(str[colon:end])
print(number)
