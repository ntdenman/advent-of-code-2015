#puzzle_input = "1"
puzzle_input = "3113322113"
n_iter = 50 #40

prev_out = puzzle_input

#print("iter:", 0, "out:", puzzle_input)

for i in range(n_iter):
    output = ""
    if len(prev_out) > 1:
        char_cur = prev_out[0]
    else:
        char_cur = prev_out
    count = 1

    j = 0
    while j < len(prev_out):
        if j == len(prev_out)-1:
            output += str(count)
            output += char_cur
        else: 
            char_next = prev_out[j+1]
            if char_next == char_cur:
                count += 1
            else:
                output += str(count)
                output += char_cur
                char_cur = char_next
                count = 1
        j += 1

    #print("iter:", i+1, "out:", output)
    prev_out = output

print(len(output))
