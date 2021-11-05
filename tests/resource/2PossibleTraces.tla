------------------------------------ MODULE 2PossibleTraces -----------------------------
(*
There should be only two possible paths for x to reach 3
0 -> 1 -> 3
0 -> 2 -> 3
*)

EXTENDS Integers, FiniteSets, Sequences, TLC

VARIABLES
    \* @type: Int;
    x

\* @type: () => Bool;
Init == x = 0

ZeroToOne == x = 0 /\ x' = 1
ZeroToTwo == x = 0 /\ x' = 2
OneToThree == x = 1 /\ x' = 3
TwoToThree == x = 2 /\ x' = 3

ThreePlus == 2 < x /\ x' = x + 1

Next ==
    \/ ZeroToOne
    \/ ZeroToTwo
    \/ OneToThree
    \/ TwoToThree
    \/ ThreePlus

IsThree ==
    LET Desired == x = 3
    IN ~Desired


(*
# Ok
apalache-mc check --view=View --inv=IsThree 2PossibleTraces.tla

# Ok
apalache-mc check --max-error=2 --view=View --inv=IsThree --config=2PossibleTraces.cfg 2PossibleTracesTests.tla

# Misleading log message
apalache-mc check --max-error=3 --view=View --inv=IsThree 2PossibleTraces.tla
*)

===============================================================================
