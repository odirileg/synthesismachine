from openpyxl import Workbook
import random

def generate_excel(filename='output.xlsx'):
    # Create a new workbook and select the active sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Reagent Data"

    # Define the column headers
    headers = ['Reagent 1', 'Volume 1', 'NaNO2', 'Reagent 2', 'Volume 2', 'NaOH', 'HEX']
    ws.append(headers)

    # Generate 24 rows of data
    for _ in range(24):
        # Generate Reagent 1 and Reagent 2 values (1-4)
        reagent1 = random.randint(1, 4)
        reagent2 = random.randint(1, 4)

        # Generate Volume 1 (random value between 0.5 and 3.5 with 0.5 steps)
        volume1 = random.choice([round(i, 1) for i in range(5, 36, 5)]) / 10
        # Calculate Volume 2
        volume2 = round(4 - volume1, 1)

        # Fixed values for NaNO2 and NaOH
        na_no2 = 2
        na_oh = 2

        # Empty value for HEX
        hex_value = ''

        # Append the row to the worksheet
        ws.append([reagent1, volume1, na_no2, reagent2, volume2, na_oh, hex_value])

    # Save the workbook to a file
    wb.save(filename)
    print(f"Excel file '{filename}' generated successfully!")

# Call the function to generate the Excel file
generate_excel('reagent_data.xlsx')
