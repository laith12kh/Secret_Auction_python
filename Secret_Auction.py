import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
flag = False
to_bid={}

#the function to find the biggest bid 
def max_bid(bid):
    max_bid_amount=0
    winner=""
    for n_bid in bid :
        d_amount = int(bid[n_bid])  
        if d_amount > max_bid_amount : 
            max_bid_amount = d_amount
            winner = n_bid
    print(f"{winner} has won the auction , who bid {max_bid_amount}")
# fill the dict with the names and the bid amount
while not flag:
    your_name = input("What is your name ? :\t")
    price_to_bid = input("What is your bid ? :\t")
    to_bid[your_name] =price_to_bid
    yes_or_no = input("Are there any other bidders ? Y / N .\t")
    if yes_or_no == 'n' :
        flag = True
        max_bid(to_bid)
    elif yes_or_no=='y' :
        clear_screen()
