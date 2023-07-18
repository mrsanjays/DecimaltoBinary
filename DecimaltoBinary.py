def DecimaltoBinary(num,B):
    s=""
    while num:
        s=str(num%B)+s
        num//=B
    return s
if __name__ == '__main__':
    A=int(input())
    B=int(input())
    print(DecimaltoBinary(A,B))
"""
Given a decimal number A and a base B, convert it into its equivalent number in base B.
"""