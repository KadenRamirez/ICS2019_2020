public class StringsPractice{
	public static void main(String[] args){
		
		//String s=String.format("%5%5%5",4,5,6);
		// turns it into a string instead of putting it on the screen.
		String name1 = "Ryan";
		String name2 = "Ryan";

		
		name2 = "Jack Neel Waddell";
		name1 = "Dead";
		
	//	System.out.println(name2.substring(5,9));
		//name2 = name2.substring(5,9);
		System.out.println(name2.indexOf('e', 10));
	}
}
/*
	for(int i = name.length()-1; i >= 0; i--){
			System.out.println(name.charAt(i));
		}
		
		int countA = 0;
		for(char c: name.toCharArray()){
			System.out.println(c);
			if (c== 'a'){
				countA ++;
			}
		}
		System.out.println(countA);
	}*/

		/*
		System.out.printf("%s and %s\n", name1, name2);
		
		//when comparing strings use .equals()
		if(name1.equals(name2)){
			System.out.printf("%s and %s are the same.\n", name1, name2);
		}else{
			System.out.printf("%s and %s are different.\n", name1, name2);	
		}
		* */
