from random import getrandbits

PAYN__END = "\033[0m"
PAYN__BOLD = "\033[1m"
PAYN__RED = "\033[91m"
PAYN__GREEN = "\033[92m"
PAYN__YELLOW = "\033[93m"
PAYN__BLUE = "\033[94m"

PAYN__K= [20, 10, 8, 5, 3]
PAYN__GiveUpN = 30

PAYN__Vars = "List of (case insensitive) accepted answers:\n\ttrue, yes, t, y, 1\n\tfalse, no, f, n, 0\n"
PAYN__Request = "Please insert a valid keyword\n"
PAYN__DontCare = "Ok, you're doing it on purpose, I don't care anymore.\n"
PAYN__GiveUpText = "Listen, I don't have time for this, bye\n"
PAYN__Message = "y/n "

def TextForm(N, K1 = PAYN__K[1], K2 = PAYN__K[2]):
	return PAYN__RED+PAYN__BOLD if N > K1 else PAYN__BOLD if N > K2 else PAYN__END
def Text(String, N,  K0 = PAYN__K[0], K3 = PAYN__K[3], K4 = PAYN__K[4]):
    return PAYN__END+PAYN__DontCare if N > K0 else String.upper() if N > K3 else String if N > K4 else PAYN__Request

def PAYN(Msg = PAYN__Message, K0 = PAYN__K[0], K1 = PAYN__K[1], K2 = PAYN__K[2], K3 = PAYN__K[3], K4 = PAYN__K[4], GiveUp = False, GiveUpN = PAYN__GiveUpN):
    Counter = 0
    Vars = PAYN__Vars
    B = input (Msg+" ")
    while not GiveUp or Counter < GiveUpN:
        if isinstance(B, bool):
           return B
        if B.lower() in ("yes", "true", "t", "y", "1"):
            return True
        elif B.lower() in ("no", "false", "f", "n", "0"):
            return False
        else:
            Counter += 1
            print(TextForm(Counter, K1, K2), Text(Vars, Counter, K0, K3, K4), PAYN__END, sep = "", end ="")
            B = input()
    print(PAYN__GiveUpText)
    return bool(getrandbits(1))