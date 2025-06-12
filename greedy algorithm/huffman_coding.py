import heapq

# Step 1: Count frequencies
input = "aaabbbcddccddd"
freq = {}

for char in input:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Step 2: Create min-heap
heap = [[count, char] for char, count in freq.items()]
heapq.heapify(heap)

# Step 3: Build Huffman Tree
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    combined_frequency = left[0] + right[0]
    new_node = [combined_frequency, [left, right]]
    heapq.heappush(heap, new_node)

# Step 4: Generate Huffman Codes
def generate_codes(node, code="", codes={}):
    if isinstance(node[1], str):
        codes[node[1]] = code
        return codes
    generate_codes(node[1][0], code + "0", codes)
    generate_codes(node[1][1], code + "1", codes)
    return codes

# There's only one node left in heap, the root of the tree
huffman_tree = heap[0]
codes = generate_codes(huffman_tree)

# Step 5: Encode the input using Huffman codes
def encode_string(input_string, codes):
    encoded_string = ""
    for char in input_string:
        encoded_string += codes[char]
    return encoded_string

encoded_output = encode_string(input, codes)

# Display results
print("Character Frequencies:", freq)
print("Huffman Codes:", codes)
print("Encoded String:", encoded_output)
