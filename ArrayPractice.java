public class ArrayPractice{
	public static void main(String[] args){
		
		int[] nums = {1,2,6};
		firstLast6(nums);
	}
	
	public static boolean firstLast6(int[] nums) {
		if(nums[nums.length-1] == 6 || nums[0] == 6){
			return true;
		}else{
			return false;

		}
	}
}

//from math import sin
