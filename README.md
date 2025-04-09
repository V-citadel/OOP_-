# OOP_-
Object oriented programing 
---

Computer Hierarchy - Python OOP Example
Features

1. Base Class: `Computer`
- Attributes: `_color` (device color), `_brand` (device brand).
  Methods:
  - `power_on`: Simulates turning on the device.
  - `get_details`: Returns device details.
  - 
2. Subclasses
- Laptop
  - Additional Attribute: `_screen_size` (in inches).
  - Overridden Methods: Custom `power_on` and `get_details`.
  Desktop
  - Additional Attribute: `_tower_size` (in liters).
  - Overridden Methods: Custom `power_on` and `get_details`.

---

Key OOP Concepts
1. Encapsulation: Attributes like `_color`, `_brand`, `_screen_size`, and `_tower_size` are private (prefixed with `_`).
2. Inheritance: Subclasses (`Laptop`, `Desktop`) inherit common functionality from `Computer`.
3. Polymorphism: Both `Laptop` and `Desktop` override `power_on` and `get_details` to exhibit specific behaviors.

---

How to Run the Code
1. Install Python 3.x
2. Save the code in a file 
3. Execute the file:
   

Output:
plaintext
Laptop - Color: white, Brand: HP, Screen size: 15.6 inches
Laptop is powering on...
Screen size: 15.6 inches
Desktop - Color: black, Brand: Dell, Tower size: 25 liters
Desktop is powering on...
Tower size: 25 liters

