import slot_machine_insides as smi

# calculating multiplier based on machine characteristics
multiplier = (len(smi.symbols))**(smi.reels)


def winning(bet, multiplier):
    if smi.payline[1] == 'SEVEN':
        return bet * multiplier * 7
    else:
        return bet * multiplier


def losing(bet):
    return bet; 'lost'
