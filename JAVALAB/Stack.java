package p2;
import java.util.Scanner;

public class Stack {
int maxSize = 10;
private int[] StackArray;
private int top;
public Stack() {
StackArray = new int[maxSize];
top = -1;
}
public void push(int value) {
if(top == maxSize - 1) {
 System.out.println("Stack Overflow! Cannot push"+ value);
}else {
StackArray[++top]= value;
System.out.println(value+"pushed to stack.");
}
}
public int pop() {
if(top == -1) {
System.out.println("Stack Underflow!Stack is empty");
return -1;
} else {
int value = StackArray[top--];
System.out.println(value +"popped from stack.");
return value;
}
}
public void display() {
		if(top == -1) {
			System.out.println("Stack is empty.");
		}else {
			System.out.println("Stack elements are(Top to bottom)");
			for(int i =top;i>=0;i--) {
				System.out.println(StackArray[i]);
			}
		}
}
}
