#Sharer/Coder/Listener: David Wei, Gerald Arocena, Matthew Quesada

#Exercise 2

Entry 1
| Trace Position | Current Operation | Function Value | Derivative         | Derivative Value (x) | Derivative Value (y) |
|----------------|-------------------|----------------|--------------------|----------------------|----------------------|
| v1             | x^2               | 1              |2\cdot x\dot{x}     | 2                    | 0                    |
| v2             | y^2               | 1              |2\cdot y\dot{y}     | 0                    | 2                    |
| f1             | v1 + v2           | 2              |\dot{v1} + \dot{v2} | 2                    | 2                    |
Entry 2
| Trace Position | Current Operation | Function Value | Derivative         | Derivative Value (x) | Derivative Value (y) |
|----------------|-------------------|----------------|--------------------|----------------------|----------------------|
| v1             | x + y             | 2              |\dot{x} + \dot{y}   | 1                    | 1                    |
| f2             | exp(v1)           | e^2            |exp(v1)\cdot\dot{v1}| e^2                  | e^2                  |