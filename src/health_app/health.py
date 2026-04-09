class Health:
    def __init__(self, name: str, weight_kg: float, height_m: float):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if weight_kg <= 0 or height_m <= 0:
            raise ValueError("Weight and height must be positive numbers")

        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.bmi = round(self.weight_kg / (self.height_m ** 2), 2)
        self.category = self._categorize_bmi()

    def _categorize_bmi(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def get_health_advice(self) -> str:
        if self.category == "Underweight":
            return "You are underweight. Aim for a calorie-rich balanced diet with regular exercise."
        elif self.category == "Normal":
            return "You have a healthy weight. Maintain a balanced diet and consistent physical activity."
        elif self.category == "Overweight":
            return "You are slightly overweight. Increase activity and focus on nutrition."
        else:
            return "You are in the obese range. Seek professional guidance for a structured weight program."

    def get_ideal_weight(self) -> float:
        """Returns ideal weight based on BMI 22 formula."""
        return round(22 * (self.height_m ** 2), 1)
