from health_app.health import Health
from health_app import data



def main():
    records = data.load_records()

    while True:
        print("\n--- Health App Menu ---")
        print("1. Add Health Record")
        print("2. View All Records")
        print("3. View Statistics")
        print("4. Save & Quit")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            try:
                name = input("Enter name: ").strip()
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (m): "))
                person = Health(name, weight, height)
                records.append(person)
                data.save_records(records)
                print(f"Added {person.name}: BMI {person.bmi} ({person.category})")
                print(f"Ideal weight: {person.get_ideal_weight()} kg")
                print(f"Advice: {person.get_health_advice()}")
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == "2":
            if not records:
                print("No records yet.")
            else:
                for h in records:
                    delta = round(h.weight_kg - h.get_ideal_weight(), 1)
                    print(f"{h.name}: BMI {h.bmi} ({h.category}) | Δ {delta} kg")

        elif choice == "3":
            stats = data.get_statistics()
            print("\nStatistics:")
            print(f"Total records: {stats['total_records']}")
            print(f"Average BMI:   {stats['avg_bmi']}")
            print(f"Most common:   {stats['most_common_category']}")
            print("Category distribution:")
            for k, v in stats["category_distribution"].items():
                print(f"  {k}: {v}")

        elif choice == "4":
            data.save_records(records)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
            

if __name__ == "__main__":
    main()
