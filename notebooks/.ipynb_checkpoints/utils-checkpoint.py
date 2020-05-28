import mido


def mido_setup():
    mido.set_backend('mido.backends.rtmidi')
    # mido.open_output()
    mido.open_output(name='foo', virtual=True)


def get_instrument_type(instrument):
    if instrument < 0:
        return "None"
    # if instrument < 1:
    #     return "0"
    if instrument < 9:
        return "Piano"
    if instrument < 17:
        return "Percussion"
    if instrument < 25:
        return "Organ"
    if instrument < 33:
        return "Guitar"
    if instrument < 41:
        return "Bass"
    if instrument < 49:
        return "Strings"
    if instrument < 57:
        return "Ensemble"
    if instrument < 65:
        return "Brass"
    if instrument < 73:
        return "Reed"
    if instrument < 81:
        return "Pipe"
    if instrument < 105:
        return "Synth"
    if instrument < 113:
        return "Ethnic"
    if instrument < 121:
        return "Percussive"
    if instrument < 129:
        return "Effect"
    return "Other"


def get_track_instrument_type(track):
    for msg in track:
        if msg.type == "program_change":
            return get_instrument_type(msg.program)