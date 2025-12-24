# Keywords Identifiers

import keyword
print("Keywords:", keyword.kwlist[:5])  # show first 5
identifier = input("Enter an identifier: ")
print("Is valid identifier:", identifier.isidentifier())