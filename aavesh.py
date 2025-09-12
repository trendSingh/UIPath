import numpy as np

# NumPy library added to aavesh.py
# This file now includes NumPy for numerical computing

def main():
    # Example NumPy operations
    print("NumPy library imported successfully!")
    
    # Create a simple array
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    
    # Basic operations
    print(f"Array sum: {np.sum(arr)}")
    print(f"Array mean: {np.mean(arr)}")
    print(f"Array max: {np.max(arr)}")
    
    # Create a 2D array
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Matrix:\n{matrix}")
    print(f"Matrix shape: {matrix.shape}")

if __name__ == "__main__":
    main()