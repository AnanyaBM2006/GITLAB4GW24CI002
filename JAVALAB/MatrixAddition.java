package Lab_p1;
import java.util.Scanner;

public class MatrixAddition {

	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	System.out.print("enter the order N of the Matrices:");
	int n=sc.nextInt();
	int[][]matrix1 =new int[n][n];
	int[][]matrix2 =new int[n][n];
	int[][]result =new int[n][n];
	System.out.println("enter the elements of matrix1:");
	for(int i=0;i<n;i++) {
	for(int j=0;j<n;j++) {
		System.out.print("elements ["+i+"]["+j+"]");
		matrix1[i][j]=sc.nextInt();
	}
	}
	System.out.println("enter the elements for Matrix2:");
	for(int i=0;i<n;i++) {
		for(int j=0;j<n;j++) {
			System.out.print("elements["+i+"]["+j+"]:");
			matrix2[i][j]=sc.nextInt();
		}
	}
	for(int i=0;i<n;i++) {
	for(int j=0;j<n;j++) {
			result[i][j]=matrix1[i][j]+matrix2[i][j];
			
		}
	}
	System.out.println("\n Resultant Matrix after addition:");
	for(int i=0;i<n;i++) {
		for(int j=0;j<n;j++) {
			System.out.print(result[i][j]+"\t");
		}
		System.out.println();
		
	}
	sc.close();
	
		// TODO Auto-generated method stub

	}

}
