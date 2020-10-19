#Sharer/Coder/Listener: David Wei, Gerald Arocena, Matthew Quesada

# Exercise 1

| Trace Position | Current Operation | Function Value | Derivative | Derivative Value (x) | Derivative Value (y) |
|----------------|-------------------|----------------|------------|----------------------|----------------------|
| x              | pi/2              | 1.571          | x'         | 1                    | 0                    |
| y              | pi/3              | 1.047          | y'         | 0                    | 1                    |
| v1             | sin(x)            | 1.0            | cos(x)x'   | 0                    | 0                    |
| v2             | cos(y)            | 0.5            | -sin(y )y' | 0                    | -0.866               |
| v3             | -v2               | -0.5           | -v2'       | 0                    | 0.866                |
| v4             | v1 + v3           | 0.5            | v1' + v3'. | 0                    | 0.866                
| v5             | v4^2              | 0.25           | 2v4'(v4).  | 0                    | 0.866
| v6             | -v5               | -0.25          | -v5'       | 0                    | -0.866
| v7             | exp(v6)           | 0.7788         | v6'exp(v6) | 0                    | -0.674
