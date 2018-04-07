import numpy as np
# MIN_NOTE = 1/8
# note_vals = [2**x * MIN_NOTE for x in range(6)]
# # print('note_vals: ', note_vals)
# note_vals2 = [x + x/2 for x in note_vals[:-1]]
# note_vals += note_vals2
# print('note vals: ', sorted(note_vals))


def note_pattern_gen(n_beats=4):
    note_vals = [0.125, 0.1875, 0.25, 0.375, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0]
    pattern = []
    count = 0
    while sum(pattern) <= n_beats * 2:
        count += 1
        if count > n_beats * 4:
            pattern = []
            count = 0
        if sum(pattern) == n_beats:
            break    
        new_note = np.random.choice(note_vals)
        pattern.append(new_note)
        if sum(pattern) > n_beats:
            while sum(pattern) > n_beats:
                pattern.pop()
                if sum(pattern) <= n_beats:
                    break
                pattern.append(np.random.choice(note_vals))
    return pattern
    
    
if __name__ == '__main__':
    foo = note_pattern_gen(17)
    print(foo, sum(foo))
    
    