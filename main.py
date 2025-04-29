# main.py

import pandas as pd

def get_cab_fare(pickup, drop):
    try:
        df = pd.read_csv('cab_data.csv')

        # Filter trips starting and ending in correct cities
        match = df[
            (df['pickup_city'].str.lower() == pickup.lower()) &
            (df['drop_city'].str.lower() == drop.lower())
        ]

        if not match.empty:
            avg_fare = match['fare_amount'].mean()
            return int(avg_fare)
        else:
            return None
    except Exception as e:
        print(f"Error fetching cab fare: {e}")
        return None

def get_train_fare(pickup, drop):
    try:
        df = pd.read_csv('train_data.csv')

        match = df[
            (df['source_city'].str.lower() == pickup.lower()) &
            (df['destination_city'].str.lower() == drop.lower())
        ]

        if not match.empty:
            avg_fare = match['fare'].mean()
            return int(avg_fare)
        else:
            return None
    except Exception as e:
        print(f"Error fetching train fare: {e}")
        return None

def get_flight_fare(pickup, drop):
    try:
        df = pd.read_csv('flight_data.csv')

        match = df[
            (df['source_city'].str.lower() == pickup.lower()) &
            (df['destination_city'].str.lower() == drop.lower())
        ]

        if not match.empty:
            avg_fare = match['price'].mean()
            return int(avg_fare)
        else:
            return None
    except Exception as e:
        print(f"Error fetching flight fare: {e}")
        return None

def suggest_transport(pickup, drop):
    print(f"\nFetching transport options from {pickup} to {drop}...\n")

    cab_fare = get_cab_fare(pickup, drop)
    train_fare = get_train_fare(pickup, drop)
    flight_fare = get_flight_fare(pickup, drop)

    fares = {
        "Cab": cab_fare,
        "Train": train_fare,
        "Flight": flight_fare
    }

    print("\nAvailable Options and Fares:")
    for mode, fare in fares.items():
        if fare is not None:
            print(f"{mode}: ₹{fare}")
        else:
            print(f"{mode}: Not Available")

    valid_fares = {k: v for k, v in fares.items() if v is not None}
    if valid_fares:
        best_mode = min(valid_fares, key=valid_fares.get)
        print(f"\n✅ Recommended Travel Mode: {best_mode} (₹{valid_fares[best_mode]})")
    else:
        print("\n❌ No travel options available for this route.")

if __name__ == "__main__":
    pickup = input("Enter Pickup City: ").strip()
    drop = input("Enter Drop City: ").strip()

    suggest_transport(pickup, drop)
