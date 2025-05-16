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

### Flag : 
