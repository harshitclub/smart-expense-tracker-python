# Import json module for reading and writing JSON data
import json

# Import UI helper functions
from utils import (
    success_message,
    error_message,
    info_message,
    warning_message
)


# =========================================
# SAVE EXPENSES FUNCTION
# Saves expenses into JSON file
# =========================================
def save_expenses(expenses):

    try:

        # Open data.json file in write mode
        with open("data.json", "w") as file:

            # Convert Python list into JSON format
            json.dump(
                expenses,
                file,
                indent=4
            )

        # Display success message
        success_message(
            f"💾 {len(expenses)} Expenses Saved Successfully"
        )

    # Handle unexpected saving errors
    except Exception as e:

        error_message(
            f"❌ Error Saving Expenses: {e}"
        )


# =========================================
# LOAD EXPENSES FUNCTION
# Loads saved expenses from JSON file
# =========================================
def load_expenses():

    try:

        # Display loading message
        info_message(
            "📂 Loading Saved Expenses..."
        )

        # Open JSON file in read mode
        with open("data.json", "r") as file:

            # Convert JSON data into Python list
            expenses = json.load(file)

            # Display success message
            success_message(
                "✅ Expenses Loaded Successfully"
            )

            # Return loaded expenses
            return expenses

    # Handle missing file error
    except FileNotFoundError:

        warning_message(
            "⚠️ No Existing Data Found"
        )

        return []

    # Handle invalid JSON format error
    except json.JSONDecodeError:

        error_message(
            "❌ Invalid JSON File Detected"
        )

        return []

    # Handle unexpected errors
    except Exception as e:

        error_message(
            f"❌ Unexpected Error: {e}"
        )

        return []