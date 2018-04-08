import midi_scales
import string
import numpy as np
import matplotlib.pyplot as plt

# print(dir(midi_scales))

# for item in dir(midi_scales):
#     if not item.startswith('_'):
#         print('.'.join(['midi_scales',item]))
#         print(eval('.'.join(['midi_scales',item])))
        
        
scale_degrees = {0:'unison',1:'min2',2:'maj2',3:'min3',4:'maj3',5:'fourth',6:'tritone', 7:'fifth',8:'min6',9:'maj6',10:'min7',11:'maj7'}

def normalize(arr):
    arr_min = min(arr)
    arr_max = max(arr)
    span = arr_max - arr_min
    if abs(arr_max) > abs(arr_min):
        return [x/arr_max for x in arr]
    return [x / abs(arr_min) for x in arr]

def get_scale(key, mode):
    key_offset = midi_scales.keys[key]
    base_scale = midi_scales.c_scales[mode]
    scale = [x + key_offset for x in base_scale if (x + key_offset) <= 127]
    return scale

def get_scale_degrees_dict(key, mode):
    key_offset = midi_scales.keys[key]
    base_scale = midi_scales.c_scales[mode]
    scale = [x + key_offset for x in base_scale if (x + key_offset) <= 127]
    scale_dict = {}
    for i, note in enumerate(scale):
        scale_dict[note] = scale_degrees[i % 12]
    return scale_dict
    
def get_note_distances(note, scale):
    note_distances = []
    for n in scale:
        distance = n - note
        note_distances.append(distance)
    return note_distances

# def get_scale_distances(note, scale):
#     """
#     How far is each scale note from a given 'center' note
#     """
#     note_distances = []
#     for n in scale:
#         distance = abs(note - n)
#         # distance = note - n
#         note_distances.append(distance)
#     min_distance = min(note_distances)
#     note_index = scale.index(note + min_distance)
#     scale_distances = []
#     for i in range(len(scale)):
#         distance = abs(i - note_index)
#         scale_distances.append(distance)
#     print("scale_distances = ",scale_distances, "\n")
#     return scale_distances
    

def normal_dist(x, mu, std):
    p = (1 / (std * np.sqrt(2*np.pi)))*(np.e**((-(x-mu)**2)/(2*std**2)))
    return p

def get_note_probabilities(note, scale, std):
    """
    Generate a gaussian probability array for np.choice. 'note' parameter is the tonal center.
    probabilities are based on the distance from the tonal center. std values of ~.05 limit notes to          around an octave. larger std values allow for more range.
    """
    scale_distances = normalize(get_note_distances(note, scale))
    neg = [x/(-min(scale_distances)) for x in scale_distances if x < 0]
    pos = [x/(max(scale_distances)) for x in scale_distances if x >= 0]
    scale_distances = neg + pos
    probabilities = []
    for val in scale_distances:
        p = normal_dist(val, 0, std)
        probabilities.append(p)
    probabilities = [x/sum(probabilities) for x in probabilities]
    return probabilities
    

def choose_note(note, scale, std):
    p = get_note_probabilities(note, scale, std)
    choice = np.random.choice(scale, p=p)
    return choice
        
if __name__ == '__main__':
    # print(midi_scales.__doc__)
    # scale = get_scale_degrees_dict('C','MAJOR')
#     print(scale, '\n')
    # scale = get_scale_degrees_dict('C#','MAJOR')
    # print(scale, '\n')
    # scale = get_scale_degrees_dict('F#','DORIAN')
    # print(scale, '\n')
    
    scale = get_scale('C','MAJOR')
    notes = []
    for i in range(2500):
        notes.append(choose_note(64, scale, .25))
    plt.hist(notes, bins = 127)
    plt.show()
    # foo = get_note_probabilities(64, scale)
    # print(foo)
    # plt.plot(foo)
    # plt.show()
    # print(np.e**100)
    # print(choose_note(57, scale))
    # print(list(get_note_choice_array(60, scale)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    