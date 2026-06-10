Scenario:  A movie theater has rules that determine whether a person is allowed to enter the theater.

# 1. Input Conditions:


 The inputs required for the system are:

User's age
Is the user accompanied by an adult? (Yes/No)
Does the user have a valid ticket? (Yes/No)

---

   
# 2. the Process?
The system checks the user's eligibility by applying the admission rules:

Check if the user is 13 years old or older OR accompanied by an adult.
Check if the user has a valid ticket.
If both conditions are satisfied, the user is allowed to enter.
Otherwise, the user is not allowed to enter.

Logical expression:


(Age >= 13 OR Accompanied by Adult) AND Valid Ticket


---

# 3. the Output?

The output of the system is:

"Entry Allowed" if the user meets the admission requirements.
"Entry Denied" if the user does not meet the requirements.

---


# 4. Design the Algorithm

⁠ text
START
   |
   V
Input Age
Input Adult Status
Input Ticket Status
   |
   V
(Age >= 13 OR Adult Present)?
   |
  YES
   |
Valid Ticket?
   |
YES ------> ENTRY APPROVED
   |
NO
   |
ENTRY DENIED

If first condition = NO
   |
ENTRY DENIED
   |
END
 ⁠
---

# 5. Truth Table

| Age ≥ 13 | Accompanied by Adult | Valid Ticket | Entry |
|----------|----------------------|--------------|-------|
| True | True | True | Allowed |
| True | True | False | Denied |
| True | False | True | Allowed |
| True | False | False | Denied |
| False | True | True | Allowed |
| False | True | False | Denied |
| False | False | True | Denied |
| False | False | False | Denied |

---

# 6. Step-by-Step Algorithm

1 Start the program.
2 Input the user's age.
3 Input whether the user is accompanied by an adult.
4 Input whether the user has a valid ticket.
5 Check if the user is 13 years old or older OR accompanied by an adult.
6 Check if the user has a valid ticket.
7 If all required conditions are true, display "Entry Allowed".
8 Otherwise, display "Entry Denied".
9 End the program.

---

# 7. Pseudocode

⁠ text
START

INPUT Age
INPUT IsAccompaniedByAdult
INPUT HasValidTicket

IF (Age >= 13 OR IsAccompaniedByAdult = YES) 
AND HasValidTicket = YES THEN

    DISPLAY "Entry Allowed"

ELSE

    DISPLAY "Entry Denied"

END IF

END
 ⁠

---
# 8. Evaluate Expression

 Test with Input Samples


Test Case 1:
Age: 15  
Accompanied by Adult: No  
Valid Ticket: Yes  

Result: Entry Allowed



Test Case 2:
Age: 10  
Accompanied by Adult: Yes  
Valid Ticket: Yes  

Result: Entry Allowed



Test Case 3:
Age: 10  
Accompanied by Adult: No  
Valid Ticket: Yes  

Result: Entry Denied



Test Case 4:
Age: 18  
Accompanied by Adult: No  
Valid Ticket: No  

Result: Entry Denied

---