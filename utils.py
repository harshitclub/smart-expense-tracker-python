from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Category Emojis
CATEGORY_EMOJIS = {
    "Food": "🍔",
    "Travel": "🚌",
    "Shopping": "🛒",
    "Bills": "💡",
    "Health": "💊",
    "Entertainment": "🎬",
    "Others": "📦"
}


# =========================================
# UI HELPER FUNCTIONS
# =========================================

def print_heading(title):

    print("\n" + "=" * 50)

    print(
        Fore.CYAN +
        Style.BRIGHT +
        title.center(50)
    )

    print("=" * 50)


def success_message(message):

    print(
        Fore.GREEN +
        Style.BRIGHT +
        message
    )


def error_message(message):

    print(
        Fore.RED +
        Style.BRIGHT +
        message
    )


def info_message(message):

    print(
        Fore.CYAN +
        Style.BRIGHT +
        message
    )


def warning_message(message):

    print(
        Fore.YELLOW +
        Style.BRIGHT +
        message
    )


def pause():

    input(
        Fore.MAGENTA +
        "\nPress Enter To Continue..."
    )


# =========================================
# VALIDATION FUNCTIONS
# =========================================

def get_valid_amount():

    while True:

        try:

            amount = float(
                input("💰 Enter amount: ₹")
            )

            if amount <= 0:

                warning_message(
                    "⚠️ Amount must be greater than 0"
                )

            else:

                return amount

        except ValueError:

            error_message(
                "❌ Invalid Amount. Please enter a number."
            )


def get_valid_date():

    while True:

        date = input(
            "📅 Enter date (YYYY-MM-DD): "
        ).strip()

        try:

            datetime.strptime(date, "%Y-%m-%d")

            return date

        except ValueError:

            error_message(
                "❌ Invalid Date Format"
            )


def get_valid_title():

    while True:

        title = input(
            "📝 Enter expense title: "
        ).strip()

        if title == "":

            warning_message(
                "⚠️ Title cannot be empty"
            )

        else:

            return title


def get_valid_category():

    categories = [
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Health",
        "Entertainment",
        "Others"
    ]

    while True:

        print_heading("📂 Available Categories")

        for category in categories:

            emoji = CATEGORY_EMOJIS.get(
                category,
                "📌"
            )

            print(f"{emoji} {category}")

        user_category = input(
            "\n📌 Enter category: "
        ).strip()

        if user_category in categories:

            return user_category

        else:

            error_message(
                "❌ Invalid Category"
            )