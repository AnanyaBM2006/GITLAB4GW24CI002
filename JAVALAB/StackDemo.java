package p2;

import java.util.Scanner;


	public class StackDemo {
		public static void main(String[] args) {
		Stack stack = new Stack();
		Scanner sc = new Scanner(System.in);
		int choice,value;
		do {
		System.out.println("\n====Stack Operations Menu======");
		System.out.println("1.Push");
		System.out.println("2.Pop");
		System.out.println("3.Display");
		System.out.println("4.Exit");
		System.out.println("Enter your choice(1-4):");
		choice = sc.nextInt();
		switch(choice) {
		case 1:
			System.out.print("Enter value to push:");
			value=sc.nextInt();
			stack.push(value);
			break;
		case 2:
			stack.pop();
			break;
		case 3:
			stack.display();
			break;
		case 4:
			System.out.println("Exiting the program...");
			break;
		default:
			System.out.println("Invalid choice!Please enter between 1 to 4.");
			}







		}
		while(choice!=4);
		sc.close();
				
			}
		}



