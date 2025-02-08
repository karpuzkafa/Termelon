
---

# Tertermelon Library

**Tertermelon Library** provides simple tools for creating terminal-based games.  
Currently, it includes 9 functions

---

# Features

### 1. Print a Beautiful Line  
No more manually using `=` or `-` symbols!  
```python
import termelon

termelon.whiteline()
```

---

### 2. Clear the Terminal  
Clear the terminal without the **os** library:  
```python
import termelon

termelon.clear()
```

---

### 3. Check if a Number is Odd  
Quickly check if a number is odd:  
```python
import termelon

termelon.is_odd(5)  # Output: True
termelon.is_odd(2)  # Output: False
```

---

### 4. Run a Python File  
A better way to run Python files:  

**Using subprocess:**  
```python
import termelon

subprocess.run(["python", "file.py"])
```

**Using Tertermelon Library:**  
```python
import termelon

termelon.run("file.py")
```

---

### 5. Generate a Random Number  
A simple alternative to the **random** library:  
```python
import termelon

termelon.randomize(1, 3)
```

---

# Colorizer
For using colorizer:
```python

from termelon import colorizer

colorizer.colorize("#ff0000", " this is a red text")

#or

import termelon

termelon.colorizer.colorize("#ff0000", " this is a red text")
```
colorizer prints colored texts or Lines using hex code(if your terminal dont support you see some number and text)

---
### 1.Colorize text

A colored printer(may not work on all terminals)

```python
from termelon import colorizer

termelon.colorize("#ee00ff", "this is a purple colored text")
```
Enter string values please

---
### 2. Colororize line
Print a colored line(shorter than whiteline because for an unknown bug)

```python
from termelon import colorizer

colorizer.coloredline("#ee00ff")
#output is a purple line
```

---
# Returner
You can use for colorful one line print:
```python
from termelon import returner

redpart = returner.rcolorize("#ff0000", "this text red,")

bluepart = returner.rcolorize("#0000ff", "but this one blue.")

print(redpart + bluepart)

```

---
### 1.rcolorize
returns colored text
```python
from termelon import returner
strvariable = returner.rcolorize("#ee00ff","purple text")
print(strvariable * 2)#print for 2 times if you want
#you can make more format how you want
```
---
### 2.rcoloredline
return coloredline as string
```python
from termelon import returner as r
coloredlinestring = r.rcoloredline("##333333")

#a gray line

print((coloredlinestring + "<< not colored text") * 2)
```

---
## Installation  
You cant download this library with "pip install termelon"
Follow these steps to install the library:  

1. Download as a ZIP file.  
2. Unzip the file to `/username123/termelon`.  
3. Open a terminal and run the following commands:
   
   ```bash
   python setup.py sdist bdist_wheel
   ``` 
   
   ```bash
   pip install .
   ```  
