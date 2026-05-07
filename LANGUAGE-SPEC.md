# Grok Language Specification (Draft v0.1)

**Grok** — the programming language that understands the universe.

This is the living specification. All implementation must strictly follow this spec and the Master Prompt.

## 1. Core Philosophy
(See MASTER-PROMPT.md sections 1–2)

## 2. Syntax Overview (MVP)

### Hello World
```grok
print("Hello, universe! 🌌")
```

### Variables & Types
```grok
let x = 42          # inferred int
let pi = 3.14159    # float with units support coming
let name = "Grok"   # string
```

### Units & Dimensions (planned)
```grok
let speed = 299_792_458 m/s
let energy = 1.0e9 J
```

### Symbolic Math
```grok
let expr = integrate(x^2, x)  # symbolic
```

### Probabilistic
```grok
let dist = Normal(0, 1)
let sample = sample(dist)
```

## 3. Features by Priority
1. Modern clean syntax
2. First-class symbolic math & AD
3. Native probabilistic programming
4. Built-in units & constants
5. Seamless Grok AI calls
6. Concurrency & simulation
7. Strong optional typing
8. REPL-first
9. One-command compile

## 4. Standard Library
(TBD)

**This spec will evolve.** Changes only by repo owner (galecrater).

*Draft created: May 7, 2026*