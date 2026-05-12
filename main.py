from expense_manager import (
    add_expense,
    view_expenses,
    search_expense,
    search_by_category,
    sort_expenses_desc,
    sort_expenses_asc
)

from analytics import (
    highest_expense,
    monthly_summary,
    highest_spending_category,
    average_spending,
    recent_transactions,
    weekly_spending,
    spending_insights
)

from storage import (
    save_expenses,
    load_expenses
)

from utils import (
    pause,
    error_message,
    success_message,
    info_message,
    print_heading
)

# =========================================
# LOAD EXPENSES
# =========================================

info_message("📂 Loading Expenses...")

expenses = load_expenses()

success_message("✅ Expenses Loaded Successfully")


# =========================================
# STARTUP BANNER
# =========================================

print("""
==================================================
💰        SMART EXPENSE TRACKER        💰
==================================================
Track • Analyze • Improve Your Spending
==================================================
""")


# =========================================
# MENU FUNCTION
# =========================================

def show_menu():

    print("\n" + "=" * 50)

    print_heading("💰 SMART EXPENSE TRACKER 💰")

    print("1.  ➕ Add Expense")

    print("2.  📋 View Expenses")

    print("3.  🔍 Search Expense")

    print("4.  📂 Search by Category")

    print("5.  📈 Sort Highest Spending")

    print("6.  📉 Sort Lowest Spending")

    print("7.  📊 Monthly Summary")

    print("8.  💸 Highest Expense")

    print("9.  🏆 Highest Spending Category")

    print("10. 📈 Average Spending")

    print("11. 🕒 Recent Transactions")

    print("12. 📅 Weekly Spending")

    print("13. 🤖 Spending Insights")

    print("14. ❌ Exit")

    print("=" * 50)


# =========================================
# MAIN APPLICATION LOOP
# =========================================

while True:

    show_menu()

    choice = input(
        "\n👉 Enter your choice: "
    ).strip()

    # =====================================
    # INPUT VALIDATION
    # =====================================

    if not choice.isdigit():

        error_message(
            "❌ Please Enter Valid Number"
        )

        pause()

        continue

    # =====================================
    # MENU OPTIONS
    # =====================================

    if choice == "1":

        add_expense(expenses)

        save_expenses(expenses)

        success_message(
            "💾 Expense Saved Successfully"
        )

        pause()

    elif choice == "2":

        view_expenses(expenses)

        pause()

    elif choice == "3":

        search_expense(expenses)

        pause()

    elif choice == "4":

        search_by_category(expenses)

        pause()

    elif choice == "5":

        sort_expenses_desc(expenses)

        pause()

    elif choice == "6":

        sort_expenses_asc(expenses)

        pause()

    elif choice == "7":

        monthly_summary(expenses)

        pause()

    elif choice == "8":

        highest_expense(expenses)

        pause()

    elif choice == "9":

        highest_spending_category(expenses)

        pause()

    elif choice == "10":

        average_spending(expenses)

        pause()

    elif choice == "11":

        recent_transactions(expenses)

        pause()

    elif choice == "12":

        weekly_spending(expenses)

        pause()

    elif choice == "13":

        spending_insights(expenses)

        pause()

    elif choice == "14":

        print("""
==================================================
🙏 Thank You For Using
💰 SMART EXPENSE TRACKER 💰
==================================================
Keep Tracking • Keep Improving
==================================================
""")

        break

    else:

        error_message(
            "❌ Invalid Choice"
        )

        pause()