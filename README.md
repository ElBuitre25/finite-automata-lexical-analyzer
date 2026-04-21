## initial commit
# Finite Automata Implementation – Assignment 2

## 📌 Overview

This project implements two deterministic finite automata (DFA) to simulate part of a lexical analyzer.

The program classifies an input string as:

* a **reserved keyword**, or
* an **identifier (variable)**, or
* an **invalid string**.

---

## ⚙️ Automata Description

### 🔹 Automaton 1 – Identifier Validation

This automaton verifies if a string is a valid identifier.

**Rules:**

* The first character must be a letter.
* The remaining characters must be letters or digits.

If the string does not satisfy these rules, it is rejected.

---

### 🔹 Automaton 2 – Keyword Recognition (`then`)

This automaton checks if the string corresponds to the reserved word:

```text
then
```

**Important detail in the implementation:**

The program evaluates:

```text
string[:-1]
```

This means the last character of the input is ignored when checking the keyword.

This simulates the behavior of a lexical analyzer, where a delimiter (such as a space or symbol) may follow the keyword.

---

## 🧠 Algorithm Explanation

The program works in two steps:

1. The input string is first processed by **Automaton 1**:

   * If it fails → the string is invalid.
2. If it passes:

   * The substring `string[:-1]` is evaluated by **Automaton 2**.
   * If it matches `"then"` → it is classified as a **keyword**.
   * Otherwise → it is classified as an **identifier**.

Each automaton uses:

* A state variable (`current_state`)
* A loop over the input string
* A `match-case` structure to simulate transitions

---

## 🧪 Examples

| Input    | Output         |
| -------- | -------------- |
| `then;`  | Keyword        |
| `then `  | Keyword        |
| `thenx`  | Variable       |
| `var123` | Variable       |
| `1abc`   | Invalid string |

---

## 💻 Technologies Used

* **Language:** Python 3.14.3
* **OS:** (Linux/windows)
* **Editor:** (VS Code )

---

## ▶️ How to Run

1. Open a terminal in the project folder
2. Run:

```bash
python main.py
```

3. Enter a string when prompted

---

## 📊 Program Behavior

* The program first validates the structure of the string.
* Then it determines whether the string corresponds to a reserved keyword (`then`) or a variable name.

---

## 🎯 Conclusion

This project demonstrates how deterministic finite automata can be used to recognize lexical patterns such as identifiers and reserved keywords, following strict transition rules.

---

## 👥 Authors

* Miguel Angel Alzate C
* Mathias Velez L

---
