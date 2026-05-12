# Import validation functions, UI helpers, and emojis
from utils import (
    get_valid_amount,
    get_valid_date,
    get_valid_title,
    get_valid_category,
    success_message,
    error_message,
    warning_message,
    print_heading,
    CATEGORY_EMOJIS
)


# =========================================
# ADD EXPENSE FUNCTION
# Adds new expense into expense list
# =========================================
def add_expense(expenses):

    # Print section heading
    print_heading("➕ Add New Expense")

    # Get validated expense title
    title = get_valid_title()

    # Get validated amount
    amount = get_valid_amount()

    # Get validated category
    category = get_valid_category()

    # Get validated date
    date = get_valid_date()

    # Create expense dictionary
    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    # Add expense into expenses list
    expenses.append(expense)

    # Display success message
    success_message("✅ Expense Added Successfully")


# =========================================
# VIEW EXPENSES FUNCTION
# Displays all expenses
# =========================================
def view_expenses(expenses):

    # Print section heading
    print_heading("📋 All Expenses")

    # Check if expenses list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Traverse all expenses
    for expense in expenses:

        # Get emoji based on category
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
# SEARCH EXPENSE FUNCTION
# Searches expense using title
# =========================================
def search_expense(expenses):

    # Print section heading
    print_heading("🔍 Search Expense")

    # Check if expenses list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Take search input from user
    search_title = input(
        "Enter expense title to search: "
    ).strip()

    # Variable to track search result
    found = False

    # Traverse all expenses
    for expense in expenses:

        # Compare titles using case-insensitive matching
        if expense["title"].lower() == search_title.lower():

            # Get category emoji
            emoji = CATEGORY_EMOJIS.get(
                expense["category"],
                "📌"
            )

            # Display matching expense
            print("=" * 40)

            print(f"📝 Title     : {expense['title']}")

            print(f"💰 Amount    : ₹{expense['amount']}")

            print(
                f"📂 Category  : {emoji} {expense['category']}"
            )

            print(f"📅 Date      : {expense['date']}")

            print("=" * 40)

            # Update found status
            found = True

    # If expense not found
    if not found:

        error_message("❌ Expense Not Found")


# =========================================
# SEARCH BY CATEGORY FUNCTION
# Finds expenses using category
# =========================================
def search_by_category(expenses):

    # Print section heading
    print_heading("📂 Search By Category")

    # Check if expenses list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Take category input
    category_input = input(
        "Enter category: "
    ).strip()

    # Variable to track matching results
    found = False

    # Traverse all expenses
    for expense in expenses:

        # Compare categories using case-insensitive matching
        if expense["category"].lower() == category_input.lower():

            # Get category emoji
            emoji = CATEGORY_EMOJIS.get(
                expense["category"],
                "📌"
            )

            # Display matching expense
            print("=" * 40)

            print(f"📝 Title     : {expense['title']}")

            print(f"💰 Amount    : ₹{expense['amount']}")

            print(
                f"📂 Category  : {emoji} {expense['category']}"
            )

            print(f"📅 Date      : {expense['date']}")

            print("=" * 40)

            # Update found status
            found = True

    # If no expense found
    if not found:

        error_message("❌ No Expenses Found")


# =========================================
# SORT EXPENSES DESCENDING
# Sorts expenses highest to lowest
# =========================================
def sort_expenses_desc(expenses):

    # Print section heading
    print_heading("📈 Highest Spending First")

    # Check if expenses list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Sort expenses in descending order
    sorted_expenses = sorted(
        expenses,
        key=lambda expense: expense["amount"],
        reverse=True
    )

    # Traverse sorted expenses
    for expense in sorted_expenses:

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
# SORT EXPENSES ASCENDING
# Sorts expenses lowest to highest
# =========================================
def sort_expenses_asc(expenses):

    # Print section heading
    print_heading("📉 Lowest Spending First")

    # Check if expenses list is empty
    if len(expenses) == 0:

        warning_message("⚠️ No Expenses Found")

        return

    # Sort expenses in ascending order
    sorted_expenses = sorted(
        expenses,
        key=lambda expense: expense["amount"]
    )

    # Traverse sorted expenses
    for expense in sorted_expenses:

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