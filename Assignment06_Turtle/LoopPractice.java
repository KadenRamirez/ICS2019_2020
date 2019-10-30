//continue skips lines and goes to top of loop
//break the loop

//import java.util.Math;
import java.util.Scanner;
import java.util.Random;
import java.awt.Color;
import java.util.Arrays;

public class LoopPractice{
	
		public static void main(String[] args){
			int[] a = {1,2,3,4,5};
			//int[] b = a; //alias
			//int[] b = Arrays.copyOf(a, a.length);
			int[] b = copy(a);
			printArr(a);
			printArr(b);
			
			System.out.println(a);
			
			a[2] = 7;
			printArr(a);
			printArr(b);
			System.out.println(b);
			b[4] = 100;
			printArr(a);
			printArr(b);
		}
		
		public static void printArr(int[] arr){
			for(int i:arr){
				System.out.printf("%4d", i);
			}
			System.out.println();
		}
		
		public static int[] copy(int[] a){
			int len = a.length;
			int[] b = new int[len];
			for(int i= 0; i<len; i++){
				b[i] = a[i];
			}
			return b;
		}
}

/*
			// nums.length gets the length of the array.
			int[] nums = new int[10];
			
			Random rand = new Random();
			
			System.out.println("The length of the array is " + nums.length);
			
			
			
			
			for(int i = 0; i < nums.length; i++){
				nums [i] = i*3;
				nums[i] = rand.nextInt(10);
			}
			//for each integer num in the array nums do this loop
			for(int num : nums){
				System.out.println(num);
				*/
