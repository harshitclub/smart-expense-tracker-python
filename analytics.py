from datetime import datetime, timedelta

# Import helper UI functions and category emojis
from utils import (
    print_heading,
    success_message,
    warning_message,
    CATEGORY_EMOJIS
)


# =========================================
# HIGHEST EXPENSE FUNCTION
# Finds the expense with maximum amount
# =========================================
def highest_expense(expenses):

    # Print section heading
    print_heading("💸 Highest Spending Expense")

    # Check if expense list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Find highest expense using max()
    highest = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    # Get emoji based on category
    emoji = CATEGORY_EMOJIS.get(
        highest["category"],
        "📌"
    )

    # Display highest expense details
    print("=" * 40)

    print(f"📝 Title     : {highest['title']}")

    print(f"💰 Amount    : ₹{highest['amount']}")

    print(
        f"📂 Category  : {emoji} {highest['category']}"
    )

    print(f"📅 Date      : {highest['date']}")

    print("=" * 40)


# =========================================
# MONTHLY SUMMARY FUNCTION
# Shows total and category-wise spending
# =========================================
def monthly_summary(expenses):

    # Print section heading
    print_heading("📊 Monthly Summary")

    # Check if expense list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Variable to store total spending
    total_spending = 0

    # Dictionary for category-wise totals
    category_summary = {}

    # Traverse all expenses
    for expense in expenses:

        # Add amount to total spending
        total_spending += expense["amount"]

        # Get category name
        category = expense["category"]

        # Create category if not exists
        if category not in category_summary:

            category_summary[category] = 0

        # Add amount to category total
        category_summary[category] += expense["amount"]

    # Display total spending
    print(f"\n💰 Total Spending: ₹{total_spending}")

    print("\n📂 Category Wise Spending:\n")

    # Traverse category summary dictionary
    for category, amount in category_summary.items():

        # Get category emoji
        emoji = CATEGORY_EMOJIS.get(
            category,
            "📌"
        )

        # Print category spending
        print(f"{emoji} {category}: ₹{amount}")


# =========================================
# HIGHEST SPENDING CATEGORY FUNCTION
# Finds category with highest spending
# =========================================
def highest_spending_category(expenses):

    # Print section heading
    print_heading("🏆 Highest Spending Category")

    # Check if expense list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Dictionary for category totals
    category_summary = {}

    # Traverse all expenses
    for expense in expenses:

        category = expense["category"]

        # Create category if not exists
        if category not in category_summary:

            category_summary[category] = 0

        # Add amount to category
        category_summary[category] += expense["amount"]

    # Find category with highest spending
    highest_category = max(
        category_summary,
        key=category_summary.get
    )

    # Get emoji for category
    emoji = CATEGORY_EMOJIS.get(
        highest_category,
        "📌"
    )

    # Print result
    print(
        f"\n{emoji} {highest_category}: ₹{category_summary[highest_category]}"
    )


# =========================================
# AVERAGE SPENDING FUNCTION
# Calculates average expense amount
# =========================================
def average_spending(expenses):

    # Print section heading
    print_heading("📈 Average Spending")

    # Check if expense list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Variable for total amount
    total = 0

    # Traverse all expenses
    for expense in expenses:

        total += expense["amount"]

    # Calculate average
    average = total / len(expenses)

    # Print average spending
    print(f"\n💰 Average Expense: ₹{average:.2f}")


# =========================================
# RECENT TRANSACTIONS FUNCTION
# Shows last 5 transactions
# =========================================
def recent_transactions(expenses):

    # Print section heading
    print_heading("🕒 Recent Transactions")

    # Check if expense list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Get last 5 expenses using slicing
    recent = expenses[-5:]

    # Traverse recent expenses
    for expense in recent:

        # Get category emoji
        emoji = CATEGORY_EMOJIS.get(
            expense["category"],
            "📌"
        )

        # Display expense details
        print("=" * 40)

        print(f"📝 Title     : {expense['title']}")

        print(f"💰 Amount    : ₹{expense['amount']}")

        print(
            f"📂 Category  : {emoji} {expense['category']}"
        )

        print(f"📅 Date      : {expense['date']}")

        print("=" * 40)


# =========================================
# WEEKLY SPENDING FUNCTION
# Calculates spending of last 7 days
# =========================================
def weekly_spending(expenses):

    # Print section heading
    print_heading("📅 Weekly Spending Analytics")

    # Check if expense list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Get today's date
    today = datetime.today()

    # Calculate last 7 days date
    last_7_days = today - timedelta(days=7)

    # Variable to store weekly total
    total = 0

    # Traverse all expenses
    for expense in expenses:

        # Convert string date to datetime object
        expense_date = datetime.strptime(
            expense["date"],
            "%Y-%m-%d"
        )

        # Check if expense belongs to last 7 days
        if expense_date >= last_7_days:

            # Add amount to total
            total += expense["amount"]

    # Display weekly spending
    print(f"\n💰 Last 7 Days Spending: ₹{total}")


# =========================================
# SMART SPENDING INSIGHTS FUNCTION
# Generates spending insights
# =========================================
def spending_insights(expenses):

    # Print section heading
    print_heading("🤖 Smart Spending Insights")

    # Check if expense list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Variable for total spending
    total = 0

    # Traverse all expenses
    for expense in expenses:

        total += expense["amount"]

    # Calculate average expense
    average = total / len(expenses)

    # Print average spending
    print(f"\n📊 Average Spending: ₹{average:.2f}")

    # Generate smart insight based on spending
    if average > 1000:

        warning_message(
            "⚠️ High Spending Pattern Detected"
        )

        print(
            "💡 Suggestion: Try reducing unnecessary expenses."
        )

    else:

        success_message(
            "✅ Spending Looks Balanced"
        )

        print(
            "🎯 Great job maintaining your spending habits!"
        )