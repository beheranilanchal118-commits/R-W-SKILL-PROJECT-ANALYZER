import numpy as np


def press_enter():
    input("\nPress Enter to continue...")


class DataAnalytics:

    def __init__(self):
        self.array = None

    

    def create_array(self):

        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            values = input("Enter elements separated by space: ")
            numbers = [int(x) for x in values.split()]

            self.array = np.array(numbers)

        elif choice == 2:

            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))

            values = input(
                f"Enter {rows * columns} elements separated by space: "
            )

            numbers = [int(x) for x in values.split()]

            if len(numbers) == rows * columns:
                self.array = np.array(numbers).reshape(rows, columns)
            else:
                print("Wrong number of elements.")
                return

        elif choice == 3:

            layers = int(input("Enter number of layers: "))
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))

            total = layers * rows * columns

            values = input(
                f"Enter {total} elements separated by space: "
            )

            numbers = [int(x) for x in values.split()]

            if len(numbers) == total:
                self.array = np.array(numbers).reshape(
                    layers, rows, columns
                )
            else:
                print("Wrong number of elements.")
                return

        else:
            print("Invalid choice.")
            return

        print("\nArray created successfully:")
        print(self.array)

    

    def indexing_slicing(self):

        if self.array is None:
            print("Please create an array first.")
            return

        while True:

            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                if self.array.ndim == 1:

                    index = int(input("Enter index: "))

                    if -len(self.array) <= index < len(self.array):
                        print("Value:", self.array[index])
                    else:
                        print("Invalid index.")

                elif self.array.ndim == 2:

                    row = int(input("Enter row index: "))
                    column = int(input("Enter column index: "))

                    if (
                        -self.array.shape[0] <= row < self.array.shape[0]
                        and
                        -self.array.shape[1] <= column < self.array.shape[1]
                    ):
                        print("Value:", self.array[row, column])
                    else:
                        print("Invalid index.")

                elif self.array.ndim == 3:

                    layer = int(input("Enter layer index: "))
                    row = int(input("Enter row index: "))
                    column = int(input("Enter column index: "))

                    if (
                        -self.array.shape[0] <= layer < self.array.shape[0]
                        and
                        -self.array.shape[1] <= row < self.array.shape[1]
                        and
                        -self.array.shape[2] <= column < self.array.shape[2]
                    ):
                        print(
                            "Value:",
                            self.array[layer, row, column]
                        )
                    else:
                        print("Invalid index.")

                press_enter()

            elif choice == 2:

                if self.array.ndim == 1:

                    start = int(input("Enter start index: "))
                    end = int(input("Enter end index: "))

                    print("\nSliced Array:")
                    print(self.array[start:end])

                elif self.array.ndim == 2:

                    row_range = input(
                        "Enter row range (start:end): "
                    )

                    column_range = input(
                        "Enter column range (start:end): "
                    )

                    row = row_range.split(":")
                    column = column_range.split(":")

                    start_row = int(row[0])
                    end_row = int(row[1])

                    start_column = int(column[0])
                    end_column = int(column[1])

                    print("\nSliced Array:")
                    print(
                        self.array[
                            start_row:end_row,
                            start_column:end_column
                        ]
                    )

                else:

                    print("\n3D Array:")
                    print(self.array)

                press_enter()

            elif choice == 3:
                break

            else:
                print("Invalid choice.")
                press_enter()

   

    def mathematical_operations(self):

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = int(input("Enter your choice: "))

        if choice in [1, 2, 3, 4]:

            values = input(
                f"Enter {self.array.size} elements separated by space: "
            )

            numbers = [int(x) for x in values.split()]

            if len(numbers) != self.array.size:
                print("Wrong number of elements.")
                return

            second_array = np.array(numbers).reshape(
                self.array.shape
            )

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(second_array)

            if choice == 1:

                result = self.array + second_array
                print("\nResult of Addition:")
                print(result)

            elif choice == 2:

                result = self.array - second_array
                print("\nResult of Subtraction:")
                print(result)

            elif choice == 3:

                result = self.array * second_array
                print("\nResult of Multiplication:")
                print(result)

            elif choice == 4:

                if np.any(second_array == 0):
                    print("Division by zero is not allowed.")
                else:
                    result = self.array / second_array
                    print("\nResult of Division:")
                    print(result)

        elif choice == 5:

            if self.array.ndim != 1:
                print("Dot product is available for 1D arrays.")
                return

            values = input(
                f"Enter {self.array.size} elements separated by space: "
            )

            numbers = [int(x) for x in values.split()]

            if len(numbers) != self.array.size:
                print("Wrong number of elements.")
                return

            second_array = np.array(numbers)

            result = np.dot(
                self.array,
                second_array
            )

            print("\nFirst Array:")
            print(self.array)

            print("\nSecond Array:")
            print(second_array)

            print("\nDot Product:")
            print(result)

        elif choice == 6:

            if self.array.ndim != 2:
                print("Matrix multiplication needs a 2D array.")
                return

            rows = int(input("Enter rows of second matrix: "))
            columns = int(input("Enter columns of second matrix: "))

            if self.array.shape[1] != rows:
                print("Matrix multiplication is not possible.")
                return

            values = input(
                f"Enter {rows * columns} elements separated by space: "
            )

            numbers = [int(x) for x in values.split()]

            if len(numbers) != rows * columns:
                print("Wrong number of elements.")
                return

            second_array = np.array(numbers).reshape(
                rows, columns
            )

            result = np.matmul(
                self.array,
                second_array
            )

            print("\nFirst Matrix:")
            print(self.array)

            print("\nSecond Matrix:")
            print(second_array)

            print("\nMatrix Multiplication:")
            print(result)

        else:
            print("Invalid choice.")

    

    def combine_split(self):

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            if self.array.ndim != 2:
                print("Combine is available for 2D arrays.")
                return

            values = input(
                f"Enter {self.array.size} elements separated by space: "
            )

            numbers = [int(x) for x in values.split()]

            if len(numbers) != self.array.size:
                print("Wrong number of elements.")
                return

            second_array = np.array(numbers).reshape(
                self.array.shape
            )

            result = np.vstack(
                (self.array, second_array)
            )

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(second_array)

            print("\nCombined Array:")
            print(result)

        elif choice == 2:

            parts = int(
                input("Enter number of parts: ")
            )

            if parts <= 0:
                print("Invalid number of parts.")
                return

            if self.array.size % parts != 0:
                print("Array cannot be divided equally.")
                return

            result = np.array_split(
                self.array,
                parts
            )

            print("\nSplit Arrays:")

            for i in range(len(result)):
                print("\nPart", i + 1)
                print(result[i])

        else:
            print("Invalid choice.")

   

    def search_sort_filter(self):

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            value = int(
                input("Enter value to search: ")
            )

            positions = np.where(
                self.array == value
            )

            if positions[0].size > 0:
                print("Value found.")
                print("Position:", positions)
            else:
                print("Value not found.")

        elif choice == 2:

            print("\nOriginal Array:")
            print(self.array)

            order = input(
                "Enter order (asc/desc): "
            ).lower()

            if order == "asc":

                result = np.sort(
                    self.array,
                    axis=-1
                )

                print("\nSorted Array:")
                print(result)

            elif order == "desc":

                result = np.sort(
                    self.array,
                    axis=-1
                )

                if self.array.ndim == 1:
                    result = result[::-1]
                elif self.array.ndim == 2:
                    result = result[:, ::-1]
                else:
                    result = result[:, :, ::-1]

                print("\nSorted Array:")
                print(result)

            else:
                print("Enter only asc or desc.")

        elif choice == 3:

            value = int(
                input("Enter value: ")
            )

            result = self.array[
                self.array > value
            ]

            print(
                "\nValues greater than",
                value,
                ":"
            )

            print(result)

        else:
            print("Invalid choice.")

    

    def statistics(self):

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nChoose an operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("\nOriginal Array:")
            print(self.array)

            print("Sum:", np.sum(self.array))

        elif choice == 2:

            print("\nOriginal Array:")
            print(self.array)

            print("Mean:", np.mean(self.array))

        elif choice == 3:

            print("\nOriginal Array:")
            print(self.array)

            print("Median:", np.median(self.array))

        elif choice == 4:

            print("\nOriginal Array:")
            print(self.array)

            print(
                "Standard Deviation:",
                np.std(self.array)
            )

        elif choice == 5:

            print("\nOriginal Array:")
            print(self.array)

            print(
                "Variance:",
                np.var(self.array)
            )

        elif choice == 6:

            print(
                "Minimum Value:",
                np.min(self.array)
            )

        elif choice == 7:

            print(
                "Maximum Value:",
                np.max(self.array)
            )

        elif choice == 8:

            percentage = float(
                input("Enter percentile (0-100): ")
            )

            if percentage >= 0 and percentage <= 100:

                result = np.percentile(
                    self.array,
                    percentage
                )

                print(
                    f"{percentage}th Percentile:",
                    result
                )

            else:
                print(
                    "Percentile must be between 0 and 100."
                )

        else:
            print("Invalid choice.")




def main():

    analyzer = DataAnalytics()
    print("======================================")
    print("   Welcome to the NumPy Analyzer!     ")
    print("======================================")

    while True:

        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Indexing and Slicing")
        print("3. Perform Mathematical Operations")
        print("4. Combine or Split Arrays")
        print("5. Search, Sort, or Filter Arrays")
        print("6. Compute Aggregates and Statistics")
        print("7. Exit")

        choice = int(
            input("Enter your choice: ")
        )

        if choice == 1:

            analyzer.create_array()
            press_enter()

        elif choice == 2:

            analyzer.indexing_slicing()
            press_enter()

        elif choice == 3:

            analyzer.mathematical_operations()
            press_enter()

        elif choice == 4:

            analyzer.combine_split()
            press_enter()

        elif choice == 5:

            analyzer.search_sort_filter()
            press_enter()

        elif choice == 6:

            analyzer.statistics()
            press_enter()

        elif choice == 7:
            print("======================================")
            print("Thank you for using the NumPy Analyzer!")
            print("              Goodbye!                ")
            print("======================================")
            break

        else:

            print("Invalid choice. Please try again.")
            press_enter()


if __name__ == "__main__":
    main()