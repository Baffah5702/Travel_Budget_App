import csv
import json
import re
from datetime import datetime
from typing import Dict, List, Optional


# --- Custom Exceptions ---
class ExpenseError(Exception):
    """Base exception class for expense-related errors."""

    pass


class InvalidAmountError(ExpenseError):
    """Raised when an expense amount is invalid or negative."""

    pass


class InvalidCurrencyError(ExpenseError):
    """Raised when a currency code doesn't match the 3-letter ISO format."""

    pass


# --- Expense Class ---
class Expense:
    """Represents a single financial expense."""

    def __init__(
        self,
        amount: float,
        category: str,
        currency: str = "USD",
        description: str = "",
        date: Optional[str] = None,
    ):
        self.amount = self._validate_amount(amount)
        self.currency = self._validate_currency(currency)
        self.category = category.strip().title()
        self.description = description.strip()
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def _validate_amount(amount: float) -> float:
        try:
            val = float(amount)
            if val < 0:
                raise InvalidAmountError("Expense amount cannot be negative.")
            return round(val, 2)
        except (ValueError, TypeError):
            raise InvalidAmountError(
                f"Invalid numerical amount provided: {amount}"
            )

    @staticmethod
    def _validate_currency(currency: str) -> str:
        # Regex for standard 3-letter uppercase ISO currency codes (e.g., USD, NGN, GBP)
        if not re.fullmatch(r"[A-Z]{3}", currency.strip().upper()):
            raise InvalidCurrencyError(
                f"Invalid currency code format: '{currency}'. Must be 3 uppercase letters."
            )
        return currency.strip().upper()

    def to_dict(self) -> dict:
        """Serializes the expense object into a dictionary for JSON/CSV storage."""
        return {
            "amount": self.amount,
            "currency": self.currency,
            "category": self.category,
            "description": self.description,
            "date": self.date,
        }

    def __str__(self) -> str:
        return f"[{self.date}] {self.currency} {self.amount:.2f} ({self.category}) - {self.description}"


# --- ExpenseTracker Manager Class ---
class ExpenseTracker:
    """Manages a collection of Expense objects with file persistence and search features."""

    def __init__(self):
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense) -> None:
        """Adds an Expense instance to the tracker."""
        self.expenses.append(expense)

    def parse_and_add_from_text(
        self, text_input: str, category: str, currency: str = "USD"
    ) -> Expense:
        """Uses Regular Expressions to extract a price figure from messy user text

        Example text: 'I spent around $125.50 on hotel booking'
        """
        # Regex to find currency symbols/codes and numeric prices (e.g., $125.50, 45, 1,200.00)
        price_pattern = r"(?:[A-Z]{3}|\$|€|£|₦)?\s*([0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]+)?|[0-9]+(?:\.[0-9]+)?)"
        match = re.search(price_pattern, text_input)

        if not match:
            raise InvalidAmountError(
                f"Could not extract a valid numerical price from text: '{text_input}'"
            )

        # Clean commas from matched number string
        raw_price_str = match.group(1).replace(",", "")
        amount = float(raw_price_str)

        expense = Expense(
            amount=amount,
            category=category,
            currency=currency,
            description=text_input,
        )
        self.add_expense(expense)
        return expense

    def total_spent(self) -> float:
        """Calculates total cumulative spending."""
        return sum(exp.amount for exp in self.expenses)

    def filter_by_category(self, category: str) -> List[Expense]:
        """Returns expenses belonging to a specific category."""
        target = category.strip().title()
        return [exp for exp in self.expenses if exp.category == target]

    def save_to_json(self, filename: str = "expenses.json") -> None:
        """Saves all tracked expenses to a JSON file (File Handling)."""
        try:
            data = [exp.to_dict() for exp in self.expenses]
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            print(f"Successfully saved expenses to {filename}")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

    def load_from_json(self, filename: str = "expenses.json") -> None:
        """Loads expenses from a JSON file (File Handling & Exception Handling)."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.expenses = [
                    Expense(
                        amount=item["amount"],
                        category=item["category"],
                        currency=item["currency"],
                        description=item["description"],
                        date=item["date"],
                    )
                    for item in data
                ]
            print(f"Successfully loaded expenses from {filename}")
        except FileNotFoundError:
            print(
                f"File {filename} not found. Starting with an empty expense list."
            )
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing file data from {filename}: {e}")


# --- Demonstration Block ---
if __name__ == "__main__":
    tracker = ExpenseTracker()

    # 1. Standard Additions with Exception Handling checks
    try:
        tracker.add_expense(
            Expense(
                450.0,
                category="Transport",
                currency="USD",
                description="Flight ticket",
            )
        )
        tracker.add_expense(
            Expense(
                85.5,
                category="Food",
                currency="EUR",
                description="Dinner downtown",
            )
        )
    except ExpenseError as err:
        print(f"Validation Error: {err}")

    # 2. Regex Natural Language Extraction Test
    try:
        tracker.parse_and_add_from_text(
            "Just paid roughly $350.00 for hotel room service",
            category="Accommodation",
            currency="USD",
        )
    except ExpenseError as err:
        print(f"Parsing Error: {err}")

    # 3. Print Results and Totals
    print("\n--- Current Expense Log ---")
    for exp in tracker.expenses:
        print(exp)

    print(f"\nTotal Spent: ${tracker.total_spent():.2f}")

    # 4. File Handling Test
    tracker.save_to_json("my_trip_expenses.json")