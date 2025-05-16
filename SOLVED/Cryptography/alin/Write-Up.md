# alin
## Intechfest 2024

They provide some attachment (flag.enc & Matrix.class). First we need to decompile Matrix.class to see the content. I use online tool like [https://www.decompiler.com/](https://www.decompiler.com/).

Matrix.java :

```java
import java.util.Scanner;

public class Matrix {
   static Scanner input;

   public static int[][] multiply(int[][] var0, int[][] var1) {
      int var2 = var0.length;
      int var3 = var1[0].length;
      int var4 = var3;
      int[][] var5 = new int[var2][var3];

      for(int var6 = 0; var6 < var2; ++var6) {
         for(int var7 = 0; var7 < var3; ++var7) {
            for(int var8 = 0; var8 < var4; ++var8) {
               var5[var6][var7] += var0[var6][var8] * var1[var8][var7];
            }
         }
      }

      return var5;
   }

   public static int[][][] string_to_matrix(String var0) {
      int[][][] var1 = new int[var0.length() / 9][3][3];

      for(int var2 = 0; var2 < var0.length(); var2 += 9) {
         int[][] var3 = new int[3][3];

         for(int var4 = 0; var4 < 9; ++var4) {
            var3[var4 / 3][var4 % 3] = var0.charAt(var2 + var4);
         }

         var1[var2 / 9] = var3;
      }

      return var1;
   }

   public static void main(String[] var0) {
      System.out.print("plaintext: ");
      String var1 = input.nextLine();
      if (var1.length() % 9 != 0) {
         var1 = var1 + "?".repeat(9 - var1.length() % 9);
      }

      int[] var2 = new int[var1.length()];
      int[][][] var3 = string_to_matrix(var1);

      int var4;
      for(var4 = 0; var4 < var3.length; ++var4) {
         int[][] var5 = var3[var4];
         int[][] var6 = var3[0];
         int[][] var7 = multiply(var5, var6);

         for(int var8 = 0; var8 < 3; ++var8) {
            for(int var9 = 0; var9 < 3; ++var9) {
               var2[var4 * 9 + var8 * 3 + var9] = var7[var8][var9];
            }
         }
      }

      System.out.print("ciphertext: ");

      for(var4 = 0; var4 < var2.length; ++var4) {
         System.out.print(var2[var4] + " ");
      }

   }

   static {
      input = new Scanner(System.in);
   }
}
```

Program flow : 
1. user input a plaintext
2. add padding to plaintext so the length of plaintext become multiply of 9
3. convert each 9 character of plaintext to 3x3 matrix as ascii number
4. multiply each matrix with the first matrix
5. convert all matrix to an array
6. print the content of array (ciphertext)

We know the flag format is 'INTECHFEST{...}' so the first matrix created by 'INTECHFES' as key matrix.

C = P x K
P = C x K^-1

Solver flow :
1. create matrix 3x3 from ciphertext
2. multiply each matrix with inverse of key matrix
3. convert the result to text

solver.py :

```python
import numpy as np

result = ""

known_matrix = np.array([[ord("I"), ord("N"), ord("T")],
                         [ord("E"), ord("C"), ord("H")],
                         [ord("F"), ord("E"), ord("S")]])

known_inverse = np.linalg.inv(known_matrix)

print(f"Known Matrix:\n{known_matrix}")
print(f"Known Inverse:\n{known_inverse}")

ciphertext = np.array([16591, 16716, 18720, 14700, 14839, 16596, 15681, 15810, 17737, 
                       23089, 23142, 25955, 18377, 18305, 20521, 14746, 14738, 16272, 
                       19214, 19535, 21465, 22507, 22778, 25463, 19780, 19694, 22182, 
                       18507, 18417, 20641, 18043, 18278, 20120, 21986, 22215, 24733, 
                       19077, 19278, 21221, 23126, 23249, 26010, 19701, 19598, 22096, 
                       17963, 17903, 20089, 17817, 17747, 19921, 19586, 19894, 22442, 
                       16831, 16778, 18597, 13356, 13482, 15057, 13356, 13482, 15057])

reshaped_matrices = ciphertext.reshape(-1, 3, 3)

for i, matrix in enumerate(reshaped_matrices):
    print(f"\nMatrix {i + 1}:\n{matrix}")
    
    plaintext_matrix = np.matmul(matrix, known_inverse)
    
    plaintext_matrix = np.rint(plaintext_matrix).astype(int)
    
    print(f"Plaintext Matrix {i + 1} (rounded):\n{plaintext_matrix}")
    
    for row in plaintext_matrix:
        for value in row:
            result += chr(value)

print(f"\nDecoded Plaintext: {result}")
```

### Flag : INTECHFEST{y3t_4n0th3r_m4tr1x_ch4ll_bu7_wr1tt3n_1n_j4v4}
