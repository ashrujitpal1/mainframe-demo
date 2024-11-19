# main.py
import asyncio

from workflow import create_workflow

async def main():
    topic = "Credit Card Bill Payment from Savings/Current Account with Conditional Balance Check\n\nPre-Conditions\nUser has a Savings Account and a Current Account.\nUser has a Credit Card Bill with a Due Amount and a Minimum Bill Pay Amount.\nSystem has permissions to access account balances and perform transactions.\n\nSteps\n1. Check Account Balances\n\n   - Retrieve the balance of the Savings Account (savings_balance).\n   - Retrieve the balance of the Current Account (current_balance).\n\n2. Determine Payment Account\n\n   - Compare savings_balance and current_balance.\n   - Select the account with the higher balance as the primary_account for the transaction.\n\n3. Check Due Amount and Deduct Funds\n\n   - If the primary_account balance is greater than or equal to the Due Amount:\n       - Deduct the Due Amount from primary_account.\n       - Record a transaction for the Credit Card Bill Payment for the Due Amount.\n\n4. Handle Insufficient Balance in Both Accounts\n\n   - If neither the Savings nor Current Account has a sufficient balance to cover the Due Amount:\n       - Check if the primary_account balance is greater than or equal to the Minimum Bill Pay Amount.\n       - If yes:\n           - Deduct the Minimum Bill Pay Amount from primary_account.\n           - Record a transaction for the Credit Card Bill Payment for the Minimum Bill Pay Amount.\n       - If no:\n           - Record an Insufficient Funds status and notify the user.\n\n5. Post-Transaction Update\n\n   - Update the balances of Savings and Current Account in the system.\n   - Notify the user of the transaction status:\n       - Success: Indicate amount paid and account used.\n       - Insufficient Funds: Notify of failure to meet even the minimum payment."
    result = await create_workflow(topic)
    print("Workflow completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
