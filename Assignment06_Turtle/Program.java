import java.util.Scanner;

public class Program{
	public static void main(String[] args){
		
		int numberOfSides;
		
		Scanner in = new Scanner(System.in);
		System.out.println("How many sides would you like on your polygon (only enter integers please)?");
		numberOfSides = in.nextInt();
		int N_TO_SHAPE = (numberOfSides-2)*180/numberOfSides;
		int N_TO_INSIDE = 180 - N_TO_SHAPE;
		Turtle don;
		don = new Turtle();
		drawShape(numberOfSides, N_TO_INSIDE, don);
		
	}
	
	public static void drawShape( int numberOfSides, int N_TO_INSIDE, Turtle don){
		
		if (numberOfSides > 0){
			
			don.forward(50);
			don.left(N_TO_INSIDE);
			drawShape(numberOfSides-1, N_TO_INSIDE, don);
		}
		
		
	}
}
