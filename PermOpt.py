# An optimized version that uses reverse
# instead of sort for finding the next
# permutation

# A utility function to reverse a
# string str[l..h]
def reverse(str, l, h):
	
	while (l < h) :
		str[l], str[h] = str[h], str[l]
		l += 1
		h -= 1
		
	return str
	
def findCeil(str, c, k, n):
	
	ans = -1
	val = c
	
	for i in range(k, n + 1):
		if str[i] > c and str[i] < val:
			val = str[i]
			ans = i
			
	return ans
			
# Print all permutations of str in sorted order
def sortedPermutations(str):
	
	# Get size of string
	size = len(str)

	# Sort the string in increasing order
	str = ''.join(sorted(str))

	# Print permutations one by one
	isFinished = False
	
	while (not isFinished):
		
		# Print this permutation
		print(str)

		# Find the rightmost character which
		# is smaller than its next character.
		# Let us call it 'first char'

		i = 0
		for i in range(size - 2, -1, -1):
			if (str[i] < str[i + 1]):
				break

		# If there is no such character, all
		# are sorted in decreasing order,
		# means we just printed the last
		# permutation and we are done.
		if (i == -1):
			isFinished = True
		else:
			
			# Find the ceil of 'first char' in
			# right of first character.
			# Ceil of a character is the
			# smallest character greater than it
			ceilIndex = findCeil(str, str[i], i + 1,
										size - 1)

			# Swap first and second characters
			str[i], str[ceilIndex] = str[ceilIndex], str[i]

			# Reverse the string on right of 'first char'
			str = reverse(str, i + 1, size - 1)
   
   
#{ 
 # Driver Code Starts.
if __name__=="__main__":
        
        N = ["1234"]
        
        print(sortedPermutations(N))
        
        

# } Driver Code Ends