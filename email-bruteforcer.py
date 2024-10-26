"""
································································
: _  .-')     ('-.     _ .-') _  _ .-') _     ('-.  _ .-') _   :
:( \( -O )   ( OO ).-.( (  OO) )( (  OO) )  _(  OO)( (  OO) )  :
: ,------.   / . --. / \     .'_ \     .'_ (,------.\     .'_  :
: |   /`. '  | \-.  \  ,`'--..._),`'--..._) |  .---',`'--..._) :
: |  /  | |.-'-'  |  | |  |  \  '|  |  \  ' |  |    |  |  \  ' :
: |  |_.' | \| |_.'  | |  |   ' ||  |   ' |(|  '--. |  |   ' | :
: |  .  '.'  |  .-.  | |  |   / :|  |   / : |  .--' |  |   / : :
: |  |\  \   |  | |  | |  '--'  /|  '--'  / |  `---.|  '--'  / :
: `--' '--'  `--' `--' `-------' `-------'  `------'`-------'  :
································································
                        this is mine!!
                      thanks for using :3
                   27/10/2024  @  12:50 A.M.
"""

import itertools
import string

def generate_emails(template_email, use_all_chars=True, allowed_chars=None):
    prefix, domain = template_email.split("@")
    masked_portion = ''.join([ch if ch == '*' else '' for ch in prefix])
    num_asterisks = masked_portion.count('*')
    
    # use all lowercase letters if set to True, otherwise use allowed_chars
    # you can also replace the       lowercase    right below the text to 'letters' if u wish to
    characters_to_use = string.ascii_lowercase if use_all_chars else allowed_chars
    # if u do, itll use all possible letters, lower and upper case
    
    possible_combinations = itertools.product(characters_to_use, repeat=num_asterisks)
    email_variations = []
    
    for combination in possible_combinations:
        email_prefix = list(prefix)
        combo_idx = 0
        
        for i, ch in enumerate(email_prefix):
            if ch == '*':
                email_prefix[i] = combination[combo_idx]
                combo_idx += 1
                
        email_variations.append("".join(email_prefix) + "@" + domain)
        
    return email_variations

# configs
use_all_chars = False  # change to True to use all lowercase letters
allowed_chars = ['a', 'i', 'n']  # specify the allowed characters here
emails = generate_emails("i*****n@gmail.com", use_all_chars, allowed_chars)

# output
with open("emailvariations.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print(f"generated {len(emails)} variations. check 'emailvariations.txt'")
