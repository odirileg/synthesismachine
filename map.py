import random
from openpyxl import Workbook

def generate_excel(filename, datafile):
    """
    Generate an Excel file with 7 columns and 24 rows.
    Columns:
        - Reagent 1: Reagent names
        - Volume 1: Random values (0.5 to 3.5, step 0.5)
        - NaNO2: Fixed value (2)
        - Reagent 2: Reagent names
        - Volume 2: Computed as (4 - Volume 1)
        - NaOH: Fixed value (2)
        - HEX: Empty
    Also saves a separate file where reagents are stored as numbers.
    """

    wb = Workbook()
    ws = wb.active
    ws.title = "Reagent Data"

    headers = ['Reagent 1', 'Volume 1', 'NaNO2', 'Reagent 2', 'Volume 2', 'NaOH', 'HEX']
    ws.append(headers)

    # Reagents list with names
    reagents = ["Aniline", "Dimethylaniline", "Nitroaniline", "Naphthyamine"]
    
    # Reagent mapping (Name → Number)
    reagent_mapping = {
        "Aniline": 1,
        "Dimethylaniline": 2,
        "Nitroaniline": 3,
        "Naphthyamine": 4
    }

    # Open the second file to store numerical data
    with open(datafile, "w") as f:
        f.write("Reagent1_Num,Volume1,NaNO2,Reagent2_Num,Volume2,NaOH,HEX\n")  # CSV Header

        for _ in range(24):
            reagent1 = random.choice(reagents)
            reagent2 = random.choice(reagents)
            volume1 = round(random.uniform(0.5, 3.5), 1)
            volume2 = round(4 - volume1, 1)

            # Add to Excel with names
            ws.append([reagent1, volume1, 2, reagent2, volume2, 2, ''])

            # Add to text file with numbers
            f.write(f"{reagent_mapping[reagent1]},{volume1},2,{reagent_mapping[reagent2]},{volume2},2,\n")

    wb.save(filename)
    print(f"Excel file '{filename}' and data file '{datafile}' generated successfully!")

# Example usage
generate_excel("reagentdata.xlsx", "reagent_data_numbers.csv")
