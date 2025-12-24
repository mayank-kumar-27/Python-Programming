# Global Keyword

x = 10

def modify_global():
    global x
    x = 20

modify_global()
print("Modified global x:", x)