import slot_machine_insides as smi

# calculating multiplier based on machine characteristics
MULTIPLIER = (len(smi.SYMBOLS))**(smi.REELS)


def add_credits(bet, MULTIPLIER):
    if smi.payline[1] == 'SEVEN':
        return bet * MULTIPLIER * 7
    else:
        return bet * MULTIPLIER

