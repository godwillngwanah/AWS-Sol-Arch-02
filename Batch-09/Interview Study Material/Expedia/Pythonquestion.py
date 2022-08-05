"""
Assume two lists that contain the old (op) and new (np) password of users.
There is a one-to-one mapping between these two lists, i.e. op[i] will be updated to np[i].
Also, assume a list of banned words (bw) (words that shouldn't been part of any password), and a lower (l) and upper (u) limit for passwords length.
Your task is to check whether each new password (np[i]) is valid or not.

For a new password (npi) to be valid it should:

1. Contain at least `l` characters but no more than `u` characters
2. Contain at least 1 lowercase character
3. Contain at least 1 uppercase character
4. Contain at least one number [0-9]
5. Not include any banned words from bw (case-sensitive)
6. Differ from the associated old password (opi)


Example

Input:
op = ["ValidPwd1", "ValidPwd2", "Password1"]
np = ["ValidPwd3", "expediapass", "Password1"]
bw = ["expedia", "password"]
l = 8
u = 14

Output:
VALID
INVALID 3 4 5
INVALID 6
"""

def solve(op, np, bw, l, u):
  for new_pwd in np:
    if len(new_pwd) >= l:
    	