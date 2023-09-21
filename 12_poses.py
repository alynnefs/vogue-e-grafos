from visual_automata.fa.dfa import VisualDFA

dfa = VisualDFA(
    states={"q0", "q1", "q2"},
    input_symbols={"A", "B"},
    transitions={
        "q0": {"A": "q1", "B": "q2"},
        "q1": {"A": "q2", "B": "q0"},
        "q2": {"A": "q0", "B": "q1"},
    },
    initial_state="q0",
    final_states={"q1", "q2"},
)

dfa.show_diagram(view=True)

print(dfa.input_check("AAA"))
# print(dfa.input_check("ABA"))
# print(dfa.input_check("AA"))
# print(dfa.input_check("ABBAAA"))
