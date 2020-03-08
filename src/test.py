

# outport = open_output()

times = []
mid = MidiFile('./songs/bohemian_rhapsody.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
        times.append(msg.time)

print(len(times))
print(sum(times)/len(times))

plt.hist(times)
plt.show()
