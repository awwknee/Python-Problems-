"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Matt Toivonen (mtoiv4007)
"""

def main():
    print("How many customers does your company have?", end=" ")
    customer_count = int(input())
    print("How much do you anticipate an average claim costing?", end=" ")
    avg_claim_amount = float(input())
    print("What percentage of customers do you anticipate making a claim?", end=" ")
    percent_claims = float(input())

    premium = insurancePremiumCalc(customer_count, avg_claim_amount, percent_claims)

    format_str = "Average premium should be ${:.2f} in order to make $1,000,000 annually."
    print(format_str.format(premium))

def insurancePremiumCalc(n_customers, claim_cost, claim_percentage):
    premium = (1000000 + (claim_percentage/100)*(n_customers)*(claim_cost))/n_customers
    return premium

main()
