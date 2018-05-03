

# ![logo](https://github.com/dougolson/Algorithmic-Music/logo_small.png) Algorithmic Music

This is my attempt at generative or algorithmic music. Early efforts just used random number generators and I found the results to be uninteresting. Modeling brownian motion by accumulating random numbers into a buffer and mapping the result to pitch, duration, spacing and velocity gave more interesting results. The musical attributes wander rather than skip around. Of course there are many ways to generate sequences that can be mapped to musical parameters, and there are many ways to perform the mapping. 

The sounds I've come up with thus far still lack many elements I would like to hear - a stronger sense of key, chords/harmony, repeated patterns, structure in general. These are a little harder to generate.


I use the [midiutil](https://github.com/MarkCWirt/MIDIUtil) library by Mark C Wirt to generate midi files.

[Gustavo Diaz Jerez](http://www.gustavodiazjerez.com/?page_id=54&lang=en) has written a lot about the subject of algorithmic music, number sequences, mappings etc.

Thanks to Nuno Jesus for the cool logo!