import random

# Functions to process audio.
# For COMP1010, written by David E. Johnson.

# You may not use a Python list comprehension in any of the following problems. If
# you don't know what that is, we will learn it eventually. If you do know,
# stick to using loops to solve the following problems.

# 1. Write a function to make a new list with the elements in reversed order.
# If original_samples is [1,2,3], then this should return a new_list [3,2,1].
# You may not use the Python reversed function, or original_samples[::-1].
# Loop over the items in the list and build up a new list in the desired order.
# This function has been started for you.
def make_reversed_samples(original_samples):
    new_samples = [] # start with an empty new list
    length = len(original_samples)

    for num in original_samples:
        length = length - 1
        new_samples.append(original_samples[length])

    return new_samples

# 2. Write a function to make a new list with each element of the old list
# multiplied by volume. This will have the effect of making the sound louder.
# If original_samples is [1,2,3] and volume is 2, then this should return a new list
# [2,4,6]. You must use a loop to get the elements in the original list and build
# up a new list in that loop. Return the new list.
def make_louder_samples(original_samples, volume):
    new_vol_list = []
    for i in original_samples:
        i = i * volume
        new_vol_list.append(i)
    return new_vol_list # Replace this line with your own code

# 3. Write a function to make a new list made up of every nth element in the
# original list. When saving sound on a computer we can choose how many samples
# to save. More samples means higher quality. The function will shrink the number
# of samples but also reduce the quality.
# If the original list is [1,2,3,4,5,6,7,8] and skip is 3, the new list should be
# [1,4,7].
# You may not use original_list[::skip], you must use a loop to find the desired
# elements and build up a new list. As a hint, this is a problem best solved
# using a loop over the index numbers of the list rather than the elements of the
# list.  Return the new list.
def make_reduced_samples(original_samples, skip):
    new_reduced_list = []

    for i in range(0, len(original_samples), skip):
        new_reduced_list.append(original_samples[i])
        #loop based on index of list, not elements
    return new_reduced_list # Replace this line with your own code


    return second_values
# 4. Write a function to make a new list made up of every element in the
# original list with the value of new elements set to be within a certain range.
# If an element is greater than clip_level, then the element should be set to clip_level.
# If an element is less than -clip_level, then the element should be set to -clip_level.
# This means that all the new element values should be -clip_level <= value <= clip_level.
# For example, if original_samples is [-5, -1, 2, 5, 10] and clip_level is 4, then
# the new list would be [-4, -1, 2, 4, 4] (-5 5 and 10 were clipped to the allowed range.
# As a hint, use if statements to see if a value is too high or too low.
# Return the new list.
# Clipping happens in sound when recording equipment cannot capture the full range
# of volume the sound makes. The loudest sound gets clipped, or set to that maximum
# volume. This function makes the original sound become clipped to an artificially low
# level.
def make_clipped_samples(original_samples, clip_level):
    new_clipped_list = []
    for i in original_samples:
        if i > clip_level:
            i = clip_level
            new_clipped_list.append(i)
        elif i < -clip_level:
            i = -clip_level
            new_clipped_list.append(i)
        else:
            new_clipped_list.append(i)
    # Add code to make the function work as specified.
    return new_clipped_list # Replace this line with your own code

# 5. Write a function to make a new list made up of every element in the original list
# with some noise added to each value. To each element add a random int that can go
# from -noise_level to noise_level. Use a loop to access each element in the
# original list and then add this noise value to it and add it to the new list.
# As an example, if the original list is [10,20,30] and noise_level is 2, then a
# new_list might be [8, 21, 29] if the random ints picked happened to be -2, 1, -1.
# Return the new list.
# Noise is typically small rapid changes to the audio. Adding a small random
# value mimics real noise.
def make_noisy_samples(original_samples, noise_level):
    new_noisy_list = []
    for i in original_samples:
        i = i + random.randint(-noise_level, noise_level)
        new_noisy_list.append(i)
    return new_noisy_list


# 6. Write a function to make a tone. A tone is a repeating pattern of sample
# values. You are to make what is called a sawtooth pattern. A music synthesizer
# is basically doing the same thing as this but with a wider variety of patterns.
# There is not original_samples list. You are to make and return a list with the
# following structure.
# Each "sawtooth" should be values going from -10000 to 10000 counting by 1000. So
# the elements should go -10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000.
# Then, there should be 1000 sawtooths - the above pattern should repeat 1000 times.
# This should all be in a single list.
# You must use loops to make the sawtooth and the copies of the sawtooth. You
# may not write out by hand the needed elements or use loop multiplication to make copies.
def make_tone():
    tone_list = []
    i = -10000
    for x in range(100):
        i += 1000
        if i <= 10000:
            tone_list.append(i)
        for y in range(100):
            i += 1000
            if i <= 10000:
                tone_list.append(i)
            else:
                i = -10000
            tone_list.append(i)
    return tone_list # Replace this line with your own code

# You can add small test examples here and see results from running this file instead
# of the SoundApp. An example of testing the reversed_samples function is shown.
if __name__ == "__main__":
    sample_list = [1,2,3]
    print("Original:", sample_list, "Reversed:", make_reversed_samples(sample_list))

