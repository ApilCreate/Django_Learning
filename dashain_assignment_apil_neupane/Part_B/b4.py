# B4
# Given msg = "   Vijaya Dashami ko hardik shubhakamana   ", remove the extra spaces, replace hardik with dherai, and print how many words the sentence has.

msg = "   Vijaya Dashami ko hardik shubhakamana   "
space = msg.strip()
space = space.replace('hardik', 'dherai')
print(space)
list = space.split()
print(list)
# ['Vijaya', 'Dashami', 'ko', 'dherai', 'shubhakamana']
print('Total Word Count: ', len(list))