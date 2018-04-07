import random
import numpy as np
from midiutil import MIDIFile
import midi_scales
import matplotlib.pyplot as plt


def brownian_value_gen(buffer_size=200, number_of_notes=1000):
    '''
    generate a series of values approximating brownian motion.
    values are shifted and normalized to fall between 0 and 1
    '''
    buffer = np.zeros(buffer_size)
    brownian_values = []
    for i in range(number_of_notes):
        index = i % buffer_size
        buffer[index] = np.random.uniform(-1, 1)
        buffer_sum = sum(buffer)
        brownian_values.append(buffer_sum)
    min_val = abs(min(brownian_values))
    span = max(brownian_values) + min_val
    brownian_values = [(val + min_val)/span for val in brownian_values]
    return brownian_values
 
def map_to_pitch(arr, min_pitch, max_pitch):
    '''
    map brownian values to midi pitches
    '''
    pitch_array = []
    span = max_pitch - min_pitch
    for val in arr:
        note = val * span + min_pitch
        pitch_array.append(int(note))
    return pitch_array
    
def map_to_velocity(arr, min_velocity, max_velocity):
    '''
    map brownian values to midi velocities
    '''
    velocity_array = []
    span = max_velocity - min_velocity
    for val in arr:
        note = val * span + min_velocity
        velocity_array.append(int(note))
    return velocity_array


def map_to_duration(arr):
    arr = [int(x * 63 + 1)/16 for x in arr]
    return arr
    
def map_to_spacing(arr):
    arr = [int(x * 63 + 1)/16 for x in arr]
    return arr

def pattern_gen(pattern_length=16, part_length=150):
    vals = []
    for i in range(pattern_length):
        val = np.random.uniform(0, 1)
        vals.append(val)
    n_repeats = part_length // pattern_length 
    remainder = part_length % pattern_length
    arr = vals*n_repeats + vals[0:remainder]
    return arr
    
def varied_pattern_gen(pattern_length=16, part_length=150, n_variations=2):
    """
    call pattern_gen multiple times to create a more varied texture 
    """
    variations_length = n_variations* pattern_length 
    n_repeats = part_length // variations_length 
    n_calls = n_repeats
    vals = []
    for i in range(n_variations):
        tmp = pattern_gen(pattern_length, pattern_length)
        vals += tmp
    for j in range(n_repeats):
        vals += vals
    vals = vals[0:part_length]
    return vals



if __name__ == '__main__':
    note_arr = []
    for i in range(4):
        arr = brownian_value_gen(100, 320)
        note_arr.append(arr)
    # arr = pattern_gen(4,300)
    arr = varied_pattern_gen(8,320,4)
    note_arr.append(arr)
    pitches = map_to_pitch(note_arr[4], 24, 96)
    velocities = map_to_velocity(note_arr[1], 40, 100)
    durations = map_to_duration(note_arr[2])
    spacings = map_to_spacing(note_arr[3])
    track    = 0
    channel  = 0
    start_time = 0   # In beats
    tempo    = 500   # In BPM 

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                          # automatically)
    MyMIDI.addTempo(track, start_time, tempo)

    duration_list = []
    elapsed_time = 0

    track_minutes = 2 

    data = zip(durations, spacings, pitches, velocities)

    for i, tup in enumerate(data):
        note_duration, note_spacing, pitch, velocity = tup
        elapsed_time += note_spacing
        MyMIDI.addNote(track, channel, pitch, start_time + elapsed_time, note_duration, velocity)
        duration_list += [note_duration]
        # if elapsed_time > track_minutes * tempo:
        #     print('BOING!')
        #     break
    

    
    with open("new_varied_pttrn_8_4-6-2018.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)


    # print(pitches)
    # print()
    # print(velocities)
    # print()
    # print(durations)
    # print()
    # print(spacings)










