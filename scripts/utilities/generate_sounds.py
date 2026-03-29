import wave
import struct
import math
import os
import random

sample_rate = 44100

def generate_wav(filename, samples, volume=0.5):
    filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'sounds', filename)
    with wave.open(filepath, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        for sample in samples:
            v = int(sample * volume * 32767)
            v = max(-32768, min(32767, v))
            wav_file.writeframesraw(struct.pack('<h', v))

def make_spin_sound():
    # A pleasant, wooden/plastic peg click sound
    samples = []
    duration = 0.04
    num_samples = int(sample_rate * duration)
    for i in range(num_samples):
        t = i / sample_rate
        # Sharp envelope for the click
        env = math.exp(-t * 150)
        # Mix of 600Hz sine and some noise for the 'thwack'
        osc = math.sin(2 * math.pi * 600 * t) * 0.7 + random.uniform(-1, 1) * 0.3
        samples.append(osc * env)
    generate_wav('spin.wav', samples, volume=0.6)

def make_tick_sound():
    # A clean, subtle tick for the countdown
    samples = []
    duration = 0.05
    num_samples = int(sample_rate * duration)
    for i in range(num_samples):
        t = i / sample_rate
        # Envelope
        env = math.exp(-t * 80)
        # High-pitched pure sine wave
        osc = math.sin(2 * math.pi * 1200 * t)
        samples.append(osc * env)
    generate_wav('tick.wav', samples, volume=0.4)

if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'sounds'), exist_ok=True)
    make_spin_sound()
    make_tick_sound()
    print('Sounds generated.')
